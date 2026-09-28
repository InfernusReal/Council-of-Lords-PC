"""Object-level grouping: protected identities never split (WP-1).

Deterministic hash-based assignment (no RNG): sha256(object_id) decides the
split, so all windows/sectors/augmentations of one identity land together.
COL-T01/T02 control. Contract: WP-1-REQ-015/018.
"""
from __future__ import annotations

import hashlib
import sys

# WP-1 STEP 08: Fix object-level grouping (continuation of manifest step).
print("[WP-1][STEP 08] Fixing object-level grouping", file=sys.stderr)


def _bucket(object_id: str) -> int:
    return int(hashlib.sha256(object_id.encode("utf-8")).hexdigest(), 16) % 1000


def object_group_split(object_ids, mission_of, test_size: float = 0.2) -> dict:
    """Split identities into train/test with zero cross-split overlap.

    object_ids: iterable of unique protected identity strings.
    mission_of: callable object_id -> mission label (strata bookkeeping).
    test_size: fraction in [0, 1) assigned to test by hash bucket.
    Every identity appears exactly once overall (exactness by construction).
    """
    if not (0 <= test_size < 1):
        raise ValueError("test_size must lie in [0, 1)")
    ids = list(dict.fromkeys(object_ids))
    if not ids:
        raise ValueError("empty identity list")
    if any(not i for i in ids):
        raise ValueError("blank identity")
    cutoff = int(test_size * 1000)
    train, test = [], []
    strata = {}
    for oid in ids:
        mission = mission_of(oid)
        if not mission:
            raise ValueError(f"missing mission for {oid!r}")
        side = "test" if _bucket(oid) < cutoff else "train"
        (test if side == "test" else train).append(oid)
        cell = strata.setdefault(mission, {"train": 0, "test": 0})
        cell[side] += 1
    print(f"[WP-1][STEP 08] Split {len(ids)} identities "
          f"train={len(train)} test={len(test)}", file=sys.stderr)
    return {"train": sorted(train), "test": sorted(test),
            "strata": strata, "test_size": test_size}


def leakage_report(train, test, mission_of) -> dict:
    """Independent overlap audit: overlap must be exactly empty."""
    s_train, s_test = set(train), set(test)
    overlap = sorted(s_train & s_test)
    strata = {}
    for oid in s_train | s_test:
        cell = strata.setdefault(mission_of(oid), {"train": 0, "test": 0})
        cell["train" if oid in s_train else "test"] += 1
    report = {"overlap": overlap, "overlap_count": len(overlap),
              "disjoint": len(overlap) == 0, "strata": strata,
              "n_train": len(s_train), "n_test": len(s_test)}
    print(f"[WP-1][STEP 08] Leakage audit overlap={len(overlap)}",
          file=sys.stderr)
    return report
