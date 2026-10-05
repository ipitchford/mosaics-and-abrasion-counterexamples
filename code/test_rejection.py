#!/usr/bin/env python3
"""Positive control and exact-certificate corruption tests.

These are rejection smoke tests, not an exhaustive adversarial audit. Each
mutation changes a valid mathematical datum and must raise AssertionError.
A subprocess is used so none of the verifier's internal state is shared.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("Run without -O: verification assertions must remain enabled.")
import copy
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    started = time.perf_counter()
    original = json.loads((ROOT / 'evidence/mosaic_certificate.json').read_text())
    results = []
    with tempfile.TemporaryDirectory(prefix='ep-mosaic-rejection-') as td:
        work = Path(td)
        cert = work / 'certificate.json'
        report = work / 'report.json'
        command = [sys.executable, str(ROOT / 'code/verify_mosaic.py'),
                   '--certificate', str(cert), '--output', str(report)]
        cert.write_text(json.dumps(original))
        proc = subprocess.run(command, text=True, capture_output=True, timeout=90)
        if proc.returncode or json.loads(report.read_text())['status'] != 'PASS':
            raise RuntimeError(f'Positive control failed: {proc.stderr}')
        results.append({'test': 'unaltered certificate', 'expected': 'PASS', 'actual': 'PASS'})

        def coordinate(d):
            d['initial']['vertices'][0][0] = str(Fraction(d['initial']['vertices'][0][0]) + Fraction(1, 100))
        def facet(d):
            d['initial']['facets'][0] = d['initial']['facets'][0][1:]
        def missing_support(d):
            d['initial']['facets'].pop()
            d['initial']['halfspaces'].pop()
        def projection(d):
            d['template']['vertices'][10][0] = str(Fraction(d['template']['vertices'][10][0]) + Fraction(1, 100))
        def height(d):
            d['template']['regular_heights'][10] = str(Fraction(d['template']['regular_heights'][10]) + Fraction(1, 100))
        def incidence(d):
            d['periodic_counts']['I'] += 1

        for name, mutate in [('initial coordinate', coordinate), ('facet equality set', facet),
                             ('missing facet and support', missing_support), ('Schlegel coordinate', projection),
                             ('regular height', height), ('incidence total', incidence)]:
            changed = copy.deepcopy(original)
            mutate(changed)
            cert.write_text(json.dumps(changed))
            proc = subprocess.run(command, text=True, capture_output=True, timeout=90)
            if proc.returncode == 0 or 'AssertionError' not in proc.stderr:
                raise RuntimeError(f'Mutation {name!r} was not mathematically rejected: {proc.stderr}')
            results.append({'test': name, 'expected': 'REJECT', 'actual': 'REJECT',
                            'failure_class': 'AssertionError'})

    weighted = json.loads((ROOT/'evidence/weighted_sites_certificate.json').read_text())
    with tempfile.TemporaryDirectory(prefix='ep-weighted-rejection-') as td:
        cert = Path(td)/'weighted.json'
        def weight(d):
            d['sites'][0]['weight'] = str(Fraction(d['sites'][0]['weight']) + 1)
        def translate(d):
            d['Delaunay_cells'][0][0]['lattice_translate'][0] += 1
        def reference(d):
            d['Delaunay_cells'][0][0]['site'] = (d['Delaunay_cells'][0][0]['site'] + 1) % len(d['sites'])
        for name, mutate in [('positive weighted control', None), ('site weight', weight),
                             ('lattice translation', translate), ('cell reference', reference)]:
            changed = copy.deepcopy(weighted)
            if mutate:
                mutate(changed)
            cert.write_text(json.dumps(changed))
            before = cert.read_bytes()
            proc = subprocess.run([sys.executable, str(ROOT/'code/check_weighted_certificate.py'),
                                   '--certificate', str(cert)], capture_output=True, text=True, timeout=90)
            if cert.read_bytes() != before:
                raise RuntimeError('Weighted checker changed its input')
            if mutate and (proc.returncode == 0 or 'ValueError' not in proc.stderr):
                raise RuntimeError(f'Weighted mutation not rejected: {name}')
            if mutate is None and proc.returncode:
                raise RuntimeError(f'Weighted positive control failed: {proc.stderr}')
            outcome = 'REJECT' if mutate else 'PASS'
            results.append({'test': name, 'expected': outcome, 'actual': outcome, 'input_unchanged': True})

    for script in ('build_mosaic.py', 'verify_mosaic.py', 'verify_regular_realization.py', 'verify_abrasion.py', 'check_weighted_certificate.py'):
        proc = subprocess.run([sys.executable, '-O', str(ROOT/'code'/script)],
                              text=True, capture_output=True, timeout=30)
        if proc.returncode == 0 or 'Run without -O' not in proc.stderr:
            raise RuntimeError(f'Optimized-execution guard failed: {script}')
        results.append({'test': f'{script} under -O', 'expected': 'REJECT', 'actual': 'REJECT'})
    result = {'status': 'PASS', 'positive_controls': 2, 'corrupted_certificates_rejected': 9,
              'optimized_execution_guards': 5, 'tests': results,
              'wall_seconds': round(time.perf_counter()-started, 3),
              'scope': 'Bounded smoke tests; not an exhaustive mutation campaign or an independent human audit.'}
    (ROOT/'evidence/rejection_tests.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
