"""Detrending interfaces and first pure implementations (WP-1).

MEDIAN_FILTER_v1 (pure NumPy) and SPLINE_v1 (SciPy, explicit knots) both
record full provenance. Interfaces are explicit: every variant declares its
parameters up front; nothing is tuned to labels. Contract: WP-1-REQ-014.
"""
from __future__ import annotations

import hashlib
import sys

import numpy as np

from council.data.provenance import TransformRecord

# WP-1 STEP 06: Fix detrending interfaces and pure variants.
print("[WP-1][STEP 06] Fixing detrending interfaces and pure variants",
      file=sys.stderr)

MEDIAN_FILTER_OP = "MEDIAN_FILTER_v1"
SPLINE_OP = "SPLINE_v1"


def _array_hash(a: np.ndarray) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(a).tobytes()).hexdigest()


def detrend_median_filter(time: np.ndarray, flux: np.ndarray,
                          finite: np.ndarray, window_days: float):
    """Rolling-median detrend over explicit window_days. Pure.

    Returns (trend, detrended, TransformRecord). Windows with fewer than 3
    finite samples reuse the global median (declared, not silent).
    """
    if not (window_days > 0):
        raise ValueError("window_days must be positive")
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float64)
    fin = np.asarray(finite, dtype=bool)
    if not (t.shape == f.shape == fin.shape):
        raise ValueError("shape mismatch")
    gmed = float(np.median(f[fin])) if fin.any() else float("nan")
    trend = np.full(t.shape, np.nan)
    for i in range(t.size):
        if not fin[i]:
            continue
        sel = fin & (np.abs(t - t[i]) <= window_days / 2)
        trend[i] = float(np.median(f[sel])) if sel.sum() >= 3 else gmed
    detrended = np.full(t.shape, np.nan)
    detrended[fin] = f[fin] / trend[fin]
    rec = TransformRecord(
        producer="council.preprocessing.detrending",
        version=MEDIAN_FILTER_OP,
        parameters={"window_days": window_days,
                    "fallback": "global-median-below-3-samples"},
        input_hash=_array_hash(f.astype(np.float32)),
        output_hash=_array_hash(detrended.astype(np.float32)),
        quality_mask="finite-input", units="relative")
    print(f"[WP-1][STEP 06] MEDIAN_FILTER window={window_days}d",
          file=sys.stderr)
    return trend, detrended, rec


def detrend_spline(time: np.ndarray, flux: np.ndarray, finite: np.ndarray,
                   knots: np.ndarray, penalty: float):
    """Penalized cubic B-spline (P-spline) detrend. Pure interface.

    knots (interior, explicit) and penalty (second-difference ridge weight,
    explicit, >= 0) are required arguments. Solves
    (B'B + penalty * D'D) c = B'y on finite samples; trend = B c.
    penalty = 0 reduces to ordinary least squares on the fixed knot basis.
    """
    from scipy.interpolate import BSpline
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float64)
    fin = np.asarray(finite, dtype=bool)
    k = np.asarray(knots, dtype=np.float64)
    if not (t.shape == f.shape == fin.shape):
        raise ValueError("shape mismatch")
    if k.ndim != 1 or k.size == 0:
        raise ValueError("knots must be a non-empty 1-D array")
    if not (penalty >= 0):
        raise ValueError("penalty must be nonnegative")
    if fin.sum() < k.size + 4:
        raise ValueError("insufficient finite samples for knot count")
    tf = t[fin]
    if not (tf[0] < k[0] and k[-1] < tf[-1]):
        raise ValueError("knots must lie strictly inside the time span")
    full_knots = np.concatenate(([tf[0]] * 4, k, [tf[-1]] * 4))
    B = BSpline.design_matrix(tf, full_knots, 3).toarray()
    ncoef = B.shape[1]
    D = np.zeros((ncoef - 2, ncoef))
    for i in range(ncoef - 2):
        D[i, i:i + 3] = (1.0, -2.0, 1.0)
    lhs = B.T @ B + penalty * (D.T @ D)
    coef = np.linalg.solve(lhs, B.T @ f[fin])
    trend = np.full(t.shape, np.nan)
    trend[fin] = BSpline(full_knots, coef, 3)(tf)
    detrended = np.full(t.shape, np.nan)
    detrended[fin] = f[fin] / trend[fin]
    rec = TransformRecord(
        producer="council.preprocessing.detrending", version=SPLINE_OP,
        parameters={"knots": [float(x) for x in k],
                    "penalty": penalty},
        input_hash=_array_hash(f.astype(np.float32)),
        output_hash=_array_hash(detrended.astype(np.float32)),
        quality_mask="finite-input", units="relative")
    print(f"[WP-1][STEP 06] SPLINE knots={k.size} penalty={penalty}",
          file=sys.stderr)
    return trend, detrended, rec
