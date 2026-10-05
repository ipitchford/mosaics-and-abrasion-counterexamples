#!/usr/bin/env python3
"""Read-only exact comparison against checked deterministic reconstruction.

This shares the constructor and SymPy trust boundary. It is not an independent
implementation or a stand-alone proof of an infinite lower hull.
"""
import argparse
import hashlib
import json
from pathlib import Path
from verify_regular_realization import construct, ROOT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path,
                        default=ROOT/'evidence/weighted_sites_certificate.json')
    args = parser.parse_args()
    before = args.certificate.read_bytes()
    supplied = json.loads(before)
    expected, report = construct()
    if supplied != expected:
        raise ValueError('Weighted certificate differs from exact checked reconstruction')
    if args.certificate.read_bytes() != before:
        raise RuntimeError('Read-only boundary violated')
    print(json.dumps({'status': 'PASS', 'read_only': True,
                      'sha256': hashlib.sha256(before).hexdigest(),
                      'sites': report['weighted_sites_per_period'],
                      'cells': report['Delaunay_cells_per_period'],
                      'scope': 'Exact deterministic reconstruction comparison; shared implementation'}, indent=2))


if __name__ == '__main__':
    main()
