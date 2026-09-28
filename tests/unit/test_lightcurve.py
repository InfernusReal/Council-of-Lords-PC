"""WP-1 named test: LightCurve preservation, dtypes, ordering, failures.

Semantic lock: raw bytes/units preserved; float64 time / float32 flux /
int32 quality; stable ascending time order; unknown units rejected;
NaN preserved (never interpolated); raw_hash binds content.
"""
import numpy as np
import pytest

from council.data.lightcurve import ingest_lightcurve


def _lc(**kw):
    base = dict(time=[3.0, 1.0, 2.0], flux=[30.0, 10.0, 20.0],
                mission="Kepler", target_id="KIC-1")
    base.update(kw)
    return ingest_lightcurve(**base)


def test_preservation_and_hash_binding():
    lc = _lc()
    assert lc.raw_hash and len(lc.raw_hash) == 64
    lc2 = _lc(flux=[30.0, 10.0, 21.0])
    assert lc2.raw_hash != lc.raw_hash  # content change changes hash


def test_dtypes_and_stable_order():
    lc = _lc()
    assert lc.time.dtype == np.float64
    assert lc.flux.dtype == np.float32
    assert lc.quality.dtype == np.int32
    assert list(lc.time) == [1.0, 2.0, 3.0]
    assert list(lc.flux) == [10.0, 20.0, 30.0]


def test_unknown_units_rejected():
    with pytest.raises(ValueError):
        _lc(time_system="JD")
    with pytest.raises(ValueError):
        _lc(flux_definition="counts")


def test_nan_preserved_not_interpolated():
    lc = _lc(flux=[10.0, float("nan"), 20.0])
    assert int(np.isnan(lc.flux).sum()) == 1


def test_shape_and_empty_rejected():
    with pytest.raises(ValueError):
        _lc(time=[1.0], flux=[1.0, 2.0])
    with pytest.raises(ValueError):
        _lc(time=[], flux=[])
    with pytest.raises(ValueError):
        _lc(mission="")
