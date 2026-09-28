"""WP-1 named test: unknown units and silent fallbacks are rejected.

Semantic lock: no silent solar-default substitution; no unit coercion;
catalog stubs return provenance only and never payloads.
"""
import pytest

from council.data.catalogs import (CatalogQuery, CatalogUnavailableError,
                                   fetch_catalog_payload,
                                   query_neighbor_catalog,
                                   query_stellar_catalog)
from council.data.lightcurve import ingest_lightcurve
from council.data.quality import contamination_flags


def test_no_silent_unit_default():
    with pytest.raises(ValueError):
        ingest_lightcurve([1.0], [1.0], mission="TESS",
                          target_id="TOI-1", time_system="MJD")


def test_no_silent_stellar_fallback():
    q = query_stellar_catalog("KIC-1")
    assert isinstance(q, CatalogQuery)
    assert q.status == "NOT_QUERIED_IN_WP1"
    with pytest.raises(CatalogUnavailableError):
        fetch_catalog_payload(q)


def test_neighbor_query_requires_radius():
    with pytest.raises(ValueError):
        query_neighbor_catalog("KIC-1", 0.0)
    q = query_neighbor_catalog("KIC-1", 21.0)
    assert q.parameters["radius_arcsec"] == 21.0


def test_contamination_unevaluated_without_metric():
    r = contamination_flags()
    assert r["status"] == "UNEVALUATED"
    assert r["basis"] == "no neighbor metric supplied"
    with pytest.raises(ValueError):
        contamination_flags(1.5)
