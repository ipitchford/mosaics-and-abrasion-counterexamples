#!/usr/bin/env python3
"""Rebuild the certificates and run all exact checks, without network access.

Run from any directory with Python 3.10+ and SymPy installed. Existing local
certificate/report files in this package are regenerated. No external service,
repository, or publication destination is modified.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('Run without -O: verification assertions must remain enabled.')
import importlib.metadata
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
STEPS = (
    ('build_mosaic.py', 'build_mosaic.log'),
    ('verify_mosaic.py', 'mosaic_verification.log'),
    ('verify_regular_realization.py', 'regular_realization_verification.log'),
    ('check_weighted_certificate.py', 'weighted_readonly_verification.log'),
    ('verify_abrasion.py', 'abrasion_verification.log'),
    ('test_rejection.py', 'rejection_tests.log'),
)


def main() -> None:
    evidence = ROOT / 'evidence'
    evidence.mkdir(exist_ok=True)
    records = []
    for script, logfile in STEPS:
        started = time.perf_counter()
        result = subprocess.run([sys.executable, str(ROOT/'code'/script)],
                                cwd=ROOT, capture_output=True, text=True, timeout=600)
        (evidence/logfile).write_text(result.stdout + result.stderr)
        records.append({'script': script, 'exit_code': result.returncode,
                        'wall_seconds': round(time.perf_counter()-started, 3), 'log': logfile})
        print(f'{script}: {"PASS" if result.returncode == 0 else "FAIL"}', flush=True)
        if result.returncode:
            raise RuntimeError(f'{script} failed. Read evidence/{logfile}.')
    receipt = {'status': 'PASS', 'python': sys.version, 'platform': platform.platform(),
               'sympy': importlib.metadata.version('sympy'), 'steps': records,
               'arithmetic': 'rational and exact symbolic; no geometric floating-point tolerances',
               'network_access_required_for_replay': False,
               'scope': 'Finite computational checks. Infinite tiling, family limits, and PDE theorems are proved in the manuscripts.'}
    (evidence/'reproduction_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')

if __name__ == '__main__':
    main()
