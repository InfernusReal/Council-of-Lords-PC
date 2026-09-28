"""Transform provenance records and hash chaining (COL-PC-v1.0 WP-1).

Every derived array carries a TransformRecord binding producer, version,
parameters, input/output hashes, seed, mask, and units back to its source.
Contract: WP-1-REQ-014/018; Sec-16 transform ledger.
"""
from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass, field

# WP-1 STEP 02: Fix the provenance record contract (declared-seed RNG only).
print("[WP-1][STEP 02] Fixing transform provenance record contract",
      file=sys.stderr)

PROVENANCE_VERSION = "1.0.0"


def canonical_bytes(obj) -> bytes:
    """Deterministic UTF-8 encoding of a JSON-serializable object."""
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False) + "\n").encode("utf-8")


def canonical_hash(obj) -> str:
    """SHA-256 over the canonical encoding (64-hex)."""
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


@dataclass(frozen=True)
class TransformRecord:
    """Immutable transform ledger entry (Sec-16 fields)."""
    producer: str
    version: str
    parameters: dict = field(default_factory=dict)
    input_hash: str = ""
    output_hash: str = ""
    random_seed_if_any: object = None
    quality_mask: str = ""
    units: str = ""

    def __post_init__(self):
        if not self.producer or not self.version:
            raise ValueError("producer and version are required")
        for h in (self.input_hash, self.output_hash):
            if h and (len(h) != 64 or set(h) - set("0123456789abcdef")):
                raise ValueError(f"malformed hash: {h!r}")

    def as_dict(self) -> dict:
        return {"producer": self.producer, "version": self.version,
                "parameters": self.parameters, "input_hash": self.input_hash,
                "output_hash": self.output_hash,
                "random_seed_if_any": self.random_seed_if_any,
                "quality_mask": self.quality_mask, "units": self.units,
                "provenance_version": PROVENANCE_VERSION}


def chain_verify(records) -> bool:
    """Verify a transform chain links output->input without gaps."""
    recs = list(records)
    for prev, nxt in zip(recs, recs[1:]):
        if not prev.output_hash or prev.output_hash != nxt.input_hash:
            return False
    return True
