"""WP-1 named test: source registry schema, exactly-once terminal states,
no silent omission (COL-SRC-*, COL-GATE-22).

Semantic lock: 17 families present; 14 fields per entry (checked against
SourceRegistryEntrySchema_v1.json required list); every entry terminal
exactly once; non-INGESTED carries a reason; INGESTED carries hashes;
all 20 attempt sources covered; closure verdict CLOSED iff all terminal
(independent ledger scan here, not just the producer's verdict).
"""
import json
from pathlib import Path

import pytest

from forge.datasets.source_registry import (ENTRY_FIELDS, FROZEN_FAMILIES,
                                            TERMINAL_STATES, closure_audit)

REPO = Path(__file__).resolve().parent.parent.parent
ATTEMPT_NAMES = ["Kepler DR25", "Kepler KOIs", "Kepler TCEs",
                 "Kepler Certified False Positives", "Kepler Robovetter metrics",
                 "Kepler injection/recovery products",
                 "Kepler inverted/scrambled false-alarm products",
                 "Kepler eclipsing-binary catalogs", "Kepler light curves",
                 "K2 candidate/false-positive populations", "TESS TOIs",
                 "TESS TCE/DV products where eligible/available",
                 "TESS light curves", "TESS eclipsing-binary sources",
                 "MAST mission products", "NASA Exoplanet Archive products",
                 "Gaia stellar/neighbour/context products",
                 "mission-quality/systematics metadata",
                 "physically generated adversarial cases",
                 "Muse-proposed scenario specifications materialized "
                 "deterministically"]


def _registry():
    return json.loads((REPO / "data" / "manifests" / "SOURCE_REGISTRY_v1.json")
                      .read_text(encoding="utf-8"))


def test_seventeen_families_and_fourteen_fields():
    reg = _registry()
    assert [e["source_family"] for e in reg["entries"]] == list(FROZEN_FAMILIES)
    schema = json.loads((REPO / "configs" / "schemas"
                         / "SourceRegistryEntrySchema_v1.json")
                        .read_text(encoding="utf-8"))
    assert len(schema["required"]) == 14
    for e in reg["entries"]:
        assert set(e) - {"attempted_sources"} == set(ENTRY_FIELDS) == set(schema["required"])


def test_exactly_once_terminal_no_silent_omission():
    reg = _registry()
    entries = reg["entries"]
    assert len(entries) == 17
    for e in entries:
        assert entries.count(e) == 1
        assert e["acquisition_status"] in TERMINAL_STATES, e
        if e["acquisition_status"] != "INGESTED":
            assert e["acquisition_failure_reason"].strip(), e
        else:
            assert e["raw_hashes"], e
    fams = [e["source_family"] for e in entries]
    assert sorted(fams) == sorted(FROZEN_FAMILIES)  # independent omission scan


def test_attempt_sources_cover_all_twenty():
    reg = _registry()
    covered = [s for e in reg["entries"] for s in e["attempted_sources"]]
    for name in ATTEMPT_NAMES:
        assert name in covered, name
    assert "http" not in json.dumps(reg)  # no fabricated URLs


def test_closure_verdict_independent():
    reg = _registry()
    v = closure_audit(reg["entries"])
    assert v["verdict"] == "CLOSED" and v["all_terminal"]
    bad = [dict(reg["entries"][0], acquisition_status="STAGED")]
    v2 = closure_audit(bad + reg["entries"][1:])
    assert v2["verdict"] == "OPEN" and not v2["all_terminal"]
    missing = [e for e in reg["entries"]
               if e["source_family"] != "TCE_CATALOG"]
    v3 = closure_audit(missing)
    assert v3["verdict"] == "OPEN"  # silent omission detected
def test_closure_rejects_malformed_ledger():
    assert closure_audit({"not": "a list"})["verdict"] == "OPEN"
    assert closure_audit([{"source_family": "X"}])["verdict"] == "OPEN"
    assert closure_audit([])["verdict"] == "OPEN"  # silent omission of all


def test_gate_enforcement_end_to_end():
    """Tampered registry (non-terminal entry) fails `col data audit --registry`."""
    import os
    import subprocess
    import sys
    reg_path = REPO / "data" / "manifests" / "SOURCE_REGISTRY_v1.json"
    backup = reg_path.read_bytes()
    try:
        reg = json.loads(backup)
        reg["entries"][3]["acquisition_status"] = "STAGED"
        reg_path.write_text(json.dumps(reg, sort_keys=True, indent=2) + "\n",
                            encoding="utf-8")
        env = dict(os.environ, PYTHONPATH=str(REPO / "src"))
        r = subprocess.run([sys.executable, "-m", "council.cli", "data",
                            "audit", "--registry"], cwd=REPO,
                           capture_output=True, text=True, env=env)
        assert r.returncode == 3, r.stdout + r.stderr
        assert '"verdict": "OPEN"' in r.stdout
    finally:
        reg_path.write_bytes(backup)


def test_gate_enforcement_missing_ledger():
    """Removed STATUS_LEDGER breaks closure binding (red-team artifact removal)."""
    import os
    import subprocess
    import sys
    led = REPO / "data" / "manifests" / "SOURCE_STATUS_LEDGER.json"
    sidecar = led.with_suffix(led.suffix + ".sha256")
    led_b, side_b = led.read_bytes(), sidecar.read_bytes()
    try:
        led.unlink()
        env = dict(os.environ, PYTHONPATH=str(REPO / "src"))
        r = subprocess.run([sys.executable, "-m", "council.cli", "data",
                            "audit", "--registry"], cwd=REPO,
                           capture_output=True, text=True, env=env)
        assert r.returncode == 3, r.stdout + r.stderr
    finally:
        led.write_bytes(led_b)
        sidecar.write_bytes(side_b)
