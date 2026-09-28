"""WP-1 named test: object-level grouping is exact (zero leakage).

Semantic lock: every identity lands in exactly one split; train ∩ test is
empty (recomputed here with independent set logic); mission strata recorded;
blank/empty/missionless inputs rejected.
"""
import pytest

from forge.datasets.splits import leakage_report, object_group_split


def _missions(ids):
    return {i: ("Kepler" if i.startswith("KIC") else "TESS") for i in ids}


def test_grouping_exact_and_disjoint():
    ids = [f"KIC-{n}" for n in range(50)] + [f"TOI-{n}" for n in range(50)]
    mult = [x for oid in ids for x in (oid, oid)]  # windows/sectors duplicated
    s = object_group_split(mult, lambda o: _missions(mult)[o], test_size=0.2)
    assert sorted(s["train"] + s["test"]) == sorted(set(ids))
    assert set(s["train"]) & set(s["test"]) == set()  # independent recheck
    r = leakage_report(s["train"], s["test"], lambda o: _missions(mult)[o])
    assert r["disjoint"] and r["overlap_count"] == 0
    assert r["strata"]["Kepler"]["train"] + r["strata"]["Kepler"]["test"] == 50


def test_split_rejects_bad_inputs():
    with pytest.raises(ValueError):
        object_group_split([], lambda o: "X")
    with pytest.raises(ValueError):
        object_group_split(["", "A"], lambda o: "X")
    with pytest.raises(ValueError):
        object_group_split(["A"], lambda o: "")
    with pytest.raises(ValueError):
        object_group_split(["A"], lambda o: "X", test_size=1.0)


def test_split_deterministic_across_runs():
    ids = [f"KIC-{n}" for n in range(200)]
    a = object_group_split(ids, lambda o: "Kepler", test_size=0.2)
    b = object_group_split(ids, lambda o: "Kepler", test_size=0.2)
    assert a == b
