#!/data/data/com.termux/files/usr/bin/bash
set -e
cd "$(dirname "$0")/.."
test -f app.py
test -f agent/planner.py
test -f agent/coder.py
test -f agent/sandbox.py
test -f ui/index.html
python -m py_compile app.py agent/*.py tools/*.py
echo "✅ NANOAI TEST FINAL RÉUSSI"
