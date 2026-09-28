"""Raw light-curve type with byte/unit/provenance preservation (WP-1).

Ingestion is explicit: no silent interpolation, no unit defaults for unknown
units, deterministic stable time ordering. Contract: WP-1-REQ-012; Sec-15/16.
"""
from __future__ import annotations

import hashlib
import sys
from dataclasses import dataclass

import numpy as np

# WP-1 STEP 01: Fix the LightCurve type and ingestion contract.
print("[WP-1][STEP 01] Fixing LightCurve type and ingestion contract",
      file=sys.stderr)

ALLOWED_TIME_SYSTEMS = ("BJD", "BKJD", "BTJD")
ALLOWED_FLUX_DEFINITIONS = ("e-/s", "ppm", "relative")
LIGHTCURVE_SCHEMA_VERSION = "1.0.0"


@dataclass(frozen=True)
class LightCurve:
    """Immutable raw observation product (float64 time, float32 flux)."""
    time: np.ndarray
    flux: np.ndarray
    flux_err: object
    quality: np.ndarray
    mission: str
    target_id: str
    sector_or_quarter: str
    cadence: str
    time_system: str
    flux_definition: str
    raw_hash: str
    source_manifest_ref: str
    schema_version: str = LIGHTCURVE_SCHEMA_VERSION


def _canonical_ingest_bytes(time_f8: np.ndarray, flux_f4: np.ndarray,
                            quality_i4: np.ndarray, meta: str) -> bytes:
    return (time_f8.tobytes() + flux_f4.tobytes() + quality_i4.tobytes()
            + meta.encode("utf-8"))


def ingest_lightcurve(time, flux, flux_err=None, quality=None, *,
                      mission: str, target_id: str,
                      sector_or_quarter: str = "",
                      cadence: str = "",
                      time_system: str = "BJD",
                      flux_definition: str = "relative",
                      source_manifest_ref: str = "") -> LightCurve:
    """Ingest raw arrays into an immutable LightCurve.

    Failure behavior: unknown time_system/flux_definition raises ValueError
    (never a silent default); shape/dtype violations raise ValueError;
    NaN is preserved (never interpolated) for quality.py to mask.
    Deterministic: stable ascending time sort, O(n log n).
    """
    if time_system not in ALLOWED_TIME_SYSTEMS:
        raise ValueError(f"unknown time_system {time_system!r}; "
                         f"allowed {ALLOWED_TIME_SYSTEMS}")
    if flux_definition not in ALLOWED_FLUX_DEFINITIONS:
        raise ValueError(f"unknown flux_definition {flux_definition!r}; "
                         f"allowed {ALLOWED_FLUX_DEFINITIONS}")
    if not mission or not target_id:
        raise ValueError("mission and target_id are required")
    t = np.asarray(time, dtype=np.float64)
    f = np.asarray(flux, dtype=np.float32)
    if t.ndim != 1 or f.ndim != 1 or t.shape != f.shape:
        raise ValueError("time and flux must be matching 1-D arrays")
    if t.size == 0:
        raise ValueError("empty light curve")
    if flux_err is not None:
        fe = np.asarray(flux_err, dtype=np.float32)
        if fe.shape != t.shape:
            raise ValueError("flux_err shape mismatch")
    else:
        fe = None
    q = (np.asarray(quality, dtype=np.int32) if quality is not None
         else np.zeros(t.shape, dtype=np.int32))
    order = np.argsort(t, kind="stable")
    t, f, q = t[order], f[order], q[order]
    fe = fe[order] if fe is not None else None
    meta = "|".join([mission, target_id, sector_or_quarter, cadence,
                     time_system, flux_definition, source_manifest_ref])
    raw_hash = hashlib.sha256(
        _canonical_ingest_bytes(t, f, q, meta)).hexdigest()
    print(f"[WP-1][STEP 01] Ingested {target_id} n={t.size} "
          f"hash={raw_hash[:16]}", file=sys.stderr)
    return LightCurve(time=t, flux=f, flux_err=fe, quality=q,
                      mission=mission, target_id=target_id,
                      sector_or_quarter=sector_or_quarter, cadence=cadence,
                      time_system=time_system,
                      flux_definition=flux_definition, raw_hash=raw_hash,
                      source_manifest_ref=source_manifest_ref)
