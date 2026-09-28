"""WP-1 factory skeleton tests: release identity, hash binding, admission
allowlist (scratch-field mutant rejected), vocabulary enforcement."""
import pytest

from forge.datasets.factory import create_dataset_release


def _entry(**kw):
    base = {"object_id": "KIC-1", "source_class": "CATALOG_LABELLED",
            "label_confidence": "CATALOG_CANDIDATE", "mission": "Kepler"}
    base.update(kw)
    return base


def test_release_identity_and_hash():
    r = create_dataset_release("demo", "0.1.0", [_entry()])
    assert r["release_id"] == "COL-DATASET-demo-v0.1.0"
    assert len(r["manifest_hash"]) == 64
    r2 = create_dataset_release("demo", "0.1.0", [_entry()])
    assert r2["manifest_hash"] == r["manifest_hash"]
    r3 = create_dataset_release("demo", "0.1.0",
                                [_entry(object_id="KIC-2")])
    assert r3["manifest_hash"] != r["manifest_hash"]


def test_scratch_fields_rejected():
    """Unadmitted scratch fields never enter a release (admission analogue)."""
    with pytest.raises(ValueError):
        create_dataset_release("demo", "0.1.0",
                               [_entry(secret_score=0.99)])
    with pytest.raises(ValueError):
        create_dataset_release("demo", "0.1.0",
                               [_entry(source_class="OBSERVED")])
    with pytest.raises(ValueError):
        create_dataset_release("demo", "0.1.0",
                               [_entry(label_confidence="CONFIRMED_X")])
    with pytest.raises(ValueError):
        create_dataset_release("demo", "0.1.0",
                               [_entry(object_id="KIC-1"),
                                _entry(object_id="KIC-1")])
