"""Quality handling: pure, versioned mask operators (WP-1).

All operators are pure functions of their inputs. Seeded randomness appears
only where an explicit seed argument is passed (none of the WP-1 operators
use RNG; the seed channel exists in TransformRecord for later phases).
Contract: WP-1-REQ-013; Sec-6 quality block.
"""
from __future__ import annotations

import numpy as np
import sys

# WP-1 STEP 03: Fix versioned quality-mask operators.
print("[WP-1][STEP 03] Fixing versioned quality-mask operators",
      file=sys.stderr)

QUALITY_MASK_VERSION = "1.0.0"
FINITE_MASK_OP = "FINITE_v1"
OUTLIER_MASK_OP = "MAD_v1"
GAP_SUMMARY_OP = "GAP_v1"
CONTAMINATION_OP = "CONTAM_v1"


def finite_mask(time: np.ndarray, flux: np.ndarray) -> np.ndarray:
    """Boolean mask of finite (time, flux) samples. Pure."""
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float32)
    if t.shape != f.shape:
        raise ValueError("shape mismatch")
    return np.isfinite(t) & np.isfinite(f)


def outlier_mask(flux: np.ndarray, finite: np.ndarray,
                 k: float = 5.0) -> np.ndarray:
    """Median-absolute-deviation outlier flag (MAD_v1). Pure, deterministic.

    Flags finite samples with |x - median| > k * 1.4826 * MAD. k must be
    positive and explicit (no silent default regime beyond the signature).
    """
    if not (k > 0):
        raise ValueError("k must be positive")
    f = np.asarray(flux, dtype=np.float64)
    fin = np.asarray(finite, dtype=bool)
    if f.shape != fin.shape:
        raise ValueError("shape mismatch")
    out = np.zeros(f.shape, dtype=bool)
    vals = f[fin]
    if vals.size == 0:
        return out
    med = float(np.median(vals))
    mad = float(np.median(np.abs(vals - med)))
    if mad == 0:
        return out
    thresh = k * 1.4826 * mad
    flagged = fin & (np.abs(f - med) > thresh)
    out[flagged] = True
    return out


def gap_summary(time: np.ndarray, finite: np.ndarray,
                expected_cadence_days: float,
                gap_multiple: float = 5.0) -> dict:
    """Summarize gaps > gap_multiple * expected cadence. Pure.

    expected_cadence_days is required and explicit (no silent default):
    the caller must state the sampling it assumes.
    """
    if not (expected_cadence_days > 0):
        raise ValueError("expected_cadence_days must be positive")
    if not (gap_multiple > 1):
        raise ValueError("gap_multiple must exceed 1")
    t = np.asarray(time, dtype=np.float64)[np.asarray(finite, dtype=bool)]
    if t.size < 2:
        return {"op": GAP_SUMMARY_OP, "ngaps": 0, "gaps": [],
                "span_days": 0.0, "duty_cycle": 1.0}
    dt = np.diff(np.sort(t))
    thresh = gap_multiple * expected_cadence_days
    gaps = [(float(t[i]), float(t[i + 1]))
            for i in range(t.size - 1) if dt[i] > thresh]
    span = float(t[-1] - t[0])
    return {"op": GAP_SUMMARY_OP, "ngaps": len(gaps), "gaps": gaps,
            "span_days": span,
            "duty_cycle": float(1 - sum(b - a for a, b in gaps) / span)
            if span > 0 else 1.0}


def contamination_flags(neighbor_metric=None) -> dict:
    """Contamination assessment from an explicit neighbor metric.

    neighbor_metric None means UNEVALUATED (never fabricated clear).
    A numeric dilution estimate in [0, 1] yields EVALUATED.
    """
    if neighbor_metric is None:
        return {"op": CONTAMINATION_OP, "status": "UNEVALUATED",
                "basis": "no neighbor metric supplied"}
    d = float(neighbor_metric)
    if not (0.0 <= d <= 1.0):
        raise ValueError("neighbor metric outside [0, 1]")
    return {"op": CONTAMINATION_OP, "status": "EVALUATED",
            "dilution_estimate": d,
            "contaminated": bool(d > 0.01),
            "basis": "supplied neighbor metric"}
