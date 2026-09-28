"""Deterministic window extraction (WP-1).

Windows are pure index selections with recorded parentage. No resampling,
no interpolation, no silent edge extension. Contract: WP-1-REQ-005.
"""
from __future__ import annotations

import hashlib
import sys

import numpy as np

# WP-1 STEP 07: Fix deterministic window operators.
print("[WP-1][STEP 07] Fixing deterministic window operators",
      file=sys.stderr)

WINDOWS_VERSION = "1.0.0"


def extract_window(time: np.ndarray, flux: np.ndarray,
                   quality: np.ndarray, t_start: float, t_end: float) -> dict:
    """Extract [t_start, t_end] samples. Raises on empty selection."""
    if not (t_end > t_start):
        raise ValueError("t_end must exceed t_start")
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float32)
    q = np.asarray(quality, dtype=np.int32)
    sel = (t >= t_start) & (t <= t_end)
    if not sel.any():
        raise ValueError("empty window selection")
    block = {"time": t[sel], "flux": f[sel], "quality": q[sel],
             "t_start": float(t_start), "t_end": float(t_end),
             "n": int(sel.sum()), "windows_version": WINDOWS_VERSION}
    block["window_hash"] = hashlib.sha256(
        t[sel].tobytes() + f[sel].tobytes()).hexdigest()
    print(f"[WP-1][STEP 07] Window [{t_start}, {t_end}] n={int(sel.sum())}",
          file=sys.stderr)
    return block


def select_transit_windows(time: np.ndarray, flux: np.ndarray,
                           quality: np.ndarray, epoch: float,
                           period_days: float, duration_days: float,
                           n_transits: int,
                           half_windows: float = 2.0) -> list:
    """Deterministic transit-centered windows: epoch + k*period, k=0..n-1.

    half_windows scales duration_days on each side; must be positive.
    Window hashes cover the real time/flux bytes (no dummy arrays).
    """
    if not (period_days > 0 and duration_days > 0 and half_windows > 0):
        raise ValueError("period/duration/half_windows must be positive")
    if n_transits < 1:
        raise ValueError("n_transits must be >= 1")
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float32)
    q = np.asarray(quality, dtype=np.int32)
    wins = []
    half = half_windows * duration_days
    for k in range(n_transits):
        center = epoch + k * period_days
        try:
            wins.append(extract_window(
                t, f, q, center - half, center + half))
        except ValueError:
            continue
    print(f"[WP-1][STEP 07] Selected {len(wins)}/{n_transits} transit windows",
          file=sys.stderr)
    return wins
