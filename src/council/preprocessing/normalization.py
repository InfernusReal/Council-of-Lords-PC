"""Normalization variants as named pure ops with provenance (WP-1).

Contract: WP-1-REQ-014; Sec-6 preprocessing block. No fitting to hidden
labels: every op is a closed-form function of the input light curve.
"""
from __future__ import annotations

import hashlib
import sys

import numpy as np

from council.data.provenance import TransformRecord

# WP-1 STEP 05: Fix named normalization operators.
print("[WP-1][STEP 05] Fixing named normalization operators",
      file=sys.stderr)

MEDIAN_DIVIDE_OP = "MEDIAN_DIVIDE_v1"


def _array_hash(a: np.ndarray) -> str:
    return hashlib.sha256(
        np.ascontiguousarray(a).tobytes()).hexdigest()


def normalize_median_divide(time: np.ndarray, flux: np.ndarray,
                            finite: np.ndarray):
    """Divide finite flux by its median; non-finite preserved as NaN.

    Returns (normalized_flux, TransformRecord). Pure and deterministic.
    """
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float32)
    fin = np.asarray(finite, dtype=bool)
    if not (t.shape == f.shape == fin.shape):
        raise ValueError("shape mismatch")
    vals = f[fin].astype(np.float64)
    if vals.size == 0:
        raise ValueError("no finite samples")
    med = float(np.median(vals))
    if med == 0:
        raise ValueError("zero median flux")
    out = np.full(f.shape, np.nan, dtype=np.float32)
    out[fin] = (vals / med).astype(np.float32)
    in_h, out_h = _array_hash(f), _array_hash(out)
    rec = TransformRecord(
        producer="council.preprocessing.normalization",
        version=MEDIAN_DIVIDE_OP,
        parameters={"median": med, "n_finite": int(fin.sum())},
        input_hash=in_h, output_hash=out_h,
        quality_mask="finite-input",
        units="relative")
    print(f"[WP-1][STEP 05] MEDIAN_DIVIDE n={int(fin.sum())} median={med:.6g}",
          file=sys.stderr)
    return out, rec
