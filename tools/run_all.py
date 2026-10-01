#!/usr/bin/env python3
"""Run structural checks and gate self-tests; optionally check a candidate for release."""
from pathlib import Path
import argparse
import os
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--ship', type=int)
args = parser.parse_args()
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
for command in [[sys.executable, 'tools/verify.py'], [sys.executable, 'tools/selftest.py']]:
    result = subprocess.run(command, cwd=root, env=env)
    if result.returncode:
        raise SystemExit(result.returncode)
if args.ship is not None:
    raise SystemExit(subprocess.run([sys.executable, 'tools/verify.py', '--ship', str(args.ship)], cwd=root, env=env).returncode)
print('PROJECT CHECKS: PASS. This does not accept or publish any chapter.')
