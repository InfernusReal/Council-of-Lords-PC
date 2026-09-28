"""WP-1 named test: transforms are deterministic and hash-chained.

Semantic lock: repeated runs are byte-identical; TransformRecord binds
input/output hashes; chain_verify links records; provenance rejects
malformed hashes. Deterministic seeded sweep (fixed seeds, no hypothesis).
"""
import numpy as np

from council.data.provenance import (TransformRecord, canonical_hash,
                                     chain_verify)
from council.data.quality import finite_mask, gap_summary, outlier_mask
from council.preprocessing.detrending import (detrend_median_filter,
                                              detrend_spline)
from council.preprocessing.normalization import normalize_median_divide
from council.preprocessing.windows import extract_window


def _series(seed):
    rng = np.random.default_rng(seed)
    t = np.sort(rng.uniform(0, 30, 400))
    f = (1.0 + 0.001 * np.sin(t) + rng.normal(0, 0.002, t.size)).astype(np.float32)
    return t, f


def test_normalize_deterministic_and_chained():
    recs = []
    for _ in range(2):
        t, f = _series(7)
        fin = finite_mask(t, f)
        out, rec = normalize_median_divide(t, f, fin)
        recs.append((out, rec))
    assert recs[0][0].tobytes() == recs[1][0].tobytes()
    assert recs[0][1].input_hash == recs[1][1].input_hash
    assert recs[0][1].output_hash == recs[1][1].output_hash
    assert abs(float(np.nanmedian(recs[0][0])) - 1.0) < 1e-6


def test_detrend_variants_deterministic():
    for seed in (1, 2, 3):
        t, f = _series(seed)
        fin = finite_mask(t, f)
        _, d1, r1 = detrend_median_filter(t, f, fin, window_days=2.0)
        _, d2, r2 = detrend_median_filter(t, f, fin, window_days=2.0)
        assert np.array_equal(np.nan_to_num(d1), np.nan_to_num(d2))
        assert r1.output_hash == r2.output_hash
        knots = np.array([5.0, 10.0, 15.0, 20.0, 25.0])
        _, s1, q1 = detrend_spline(t, f, fin, knots, penalty=1.0)
        _, s2, q2 = detrend_spline(t, f, fin, knots, penalty=1.0)
        assert np.array_equal(np.nan_to_num(s1), np.nan_to_num(s2))
        assert q1.output_hash == q2.output_hash
        _, s3, q3 = detrend_spline(t, f, fin, knots, penalty=0.0)
        assert q3.output_hash != q1.output_hash  # penalty is real: changes output


def test_chain_and_quality_masks():
    t, f = _series(11)
    fin = finite_mask(t, f)
    out, r1 = normalize_median_divide(t, f, fin)
    fin2 = finite_mask(t, out)
    assert fin2.sum() == fin.sum()
    out2 = outlier_mask(out, fin2, k=5.0)
    assert out2.dtype == bool and out2.shape == out.shape
    g = gap_summary(t, fin, expected_cadence_days=0.02)
    assert g["ngaps"] >= 0 and g["duty_cycle"] <= 1.0
    w = extract_window(t, out, np.zeros(t.shape, dtype=np.int32), 0.0, 30.0)
    assert w["n"] == t.size and len(w["window_hash"]) == 64
    assert chain_verify([r1])
    bad = TransformRecord(producer="x", version="v", input_hash="0" * 64,
                          output_hash="1" * 64)
    assert not chain_verify([r1, bad])


def test_provenance_rejects_malformed():
    import pytest
    with pytest.raises(ValueError):
        TransformRecord(producer="x", version="v", input_hash="zzz")
    with pytest.raises(ValueError):
        TransformRecord(producer="", version="v")
    assert len(canonical_hash({"b": 1, "a": 2})) == 64
