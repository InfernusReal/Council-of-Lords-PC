"""Pytest path bootstrap: expose src/ (council) and repo root (forge)."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
for p in (REPO / "src", REPO):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
