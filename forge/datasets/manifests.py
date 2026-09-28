"""Canonical manifest hashing and sidecar verification (WP-1).

Manifests are canonical JSON (sorted keys, UTF-8, LF) with a .sha256
sidecar, so `sha256sum data/manifests/*` independently verifies them.
Contract: WP-1-REQ-006/018; WorkPlan WP-1 §H.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

# WP-1 STEP 08: Fix canonical manifest hashing (producer side).
print("[WP-1][STEP 08] Fixing canonical manifest hashing", file=sys.stderr)


def canonical_json(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False) + "\n").encode("utf-8")


def manifest_hash(obj) -> str:
    return hashlib.sha256(canonical_json(obj)).hexdigest()


def write_manifest(obj: dict, path) -> str:
    """Write pretty canonical JSON plus .sha256 sidecar. Returns hex hash."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pretty = json.dumps(obj, sort_keys=True, indent=2,
                        ensure_ascii=False) + "\n"
    path.write_text(pretty, encoding="utf-8", newline="\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix(path.suffix + ".sha256").write_text(
        digest + "\n", encoding="utf-8", newline="\n")
    print(f"[WP-1][STEP 08] Wrote manifest {path.name} sha={digest[:16]}",
          file=sys.stderr)
    return digest


def verify_manifest(path) -> bool:
    """Re-hash the file bytes and compare with the sidecar (independent)."""
    import hashlib as _hl
    path = Path(path)
    sidecar = path.with_suffix(path.suffix + ".sha256")
    if not path.is_file() or not sidecar.is_file():
        return False
    actual = _hl.sha256(path.read_bytes()).hexdigest()
    return actual == sidecar.read_text(encoding="utf-8").strip()
