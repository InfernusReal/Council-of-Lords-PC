"""External catalog stubs: provenance only, no target-leaking joins (WP-1).

WP-1 performs no network catalog queries. These stubs record query intent
(catalog, parameters, status) without returning data, so no catalog target
leakage is possible (COL-T03 control). Real queries arrive in later phases.
Contract: WP-1-REQ-004; Sec-6 spatial/stellar provenance.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import sys

# WP-1 STEP 04: Fix catalog stubs (provenance only, no data).
print("[WP-1][STEP 04] Fixing catalog stubs with provenance only",
      file=sys.stderr)

CATALOG_STATUS = "NOT_QUERIED_IN_WP1"


class CatalogUnavailableError(RuntimeError):
    """Raised when catalog data (not intent) is requested in WP-1 scope."""


@dataclass(frozen=True)
class CatalogQuery:
    """Provenance record of a catalog query intent (no payload)."""
    catalog: str
    parameters: dict = field(default_factory=dict)
    status: str = CATALOG_STATUS

    def __post_init__(self):
        if not self.catalog:
            raise ValueError("catalog name is required")
        if self.status != CATALOG_STATUS:
            raise ValueError("WP-1 stubs only record NOT_QUERIED intent")


def query_stellar_catalog(target_id: str, catalog: str = "UNDECLARED",
                          **params) -> CatalogQuery:
    """Record stellar-catalog intent. Returns provenance only; no data."""
    if not target_id:
        raise ValueError("target_id is required")
    print(f"[WP-1][STEP 04] Stellar intent {target_id} ({catalog}): no data",
          file=sys.stderr)
    return CatalogQuery(catalog=catalog,
                        parameters={"target_id": target_id, **params})


def query_neighbor_catalog(target_id: str, radius_arcsec: float,
                           catalog: str = "UNDECLARED",
                           **params) -> CatalogQuery:
    """Record neighbor-catalog intent. Returns provenance only; no data."""
    if not target_id:
        raise ValueError("target_id is required")
    if not (radius_arcsec > 0):
        raise ValueError("radius_arcsec must be positive")
    print(f"[WP-1][STEP 04] Neighbor intent {target_id}: no data",
          file=sys.stderr)
    return CatalogQuery(
        catalog=catalog,
        parameters={"target_id": target_id,
                    "radius_arcsec": radius_arcsec, **params})


def fetch_catalog_payload(query: CatalogQuery):
    """Always fails in WP-1 scope: payloads do not exist yet."""
    raise CatalogUnavailableError(
        f"catalog payload unavailable in WP-1 scope: {query.catalog}")
