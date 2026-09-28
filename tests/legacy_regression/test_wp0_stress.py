"""WP-0 stress + mutation/negative tests.

Every case damages inputs or artifacts and requires fail-closed behavior.
Backup/restore keeps the committed tree clean (asserted at the end).
"""
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
MANIFEST = REPO / "FOUNDATION_MANIFEST.json"
INDEX = REPO / "audits" / "legacy" / "FIXTURE_SAMPLE_INDEX.json"


def run(*args):
    return subprocess.run([sys.executable, *args], cwd=REPO,
                          capture_output=True, text=True)


def test_stress_missing_legacy_zip():
    r = run("scripts/pin_foundation.py", "--legacy-zip",
            str(REPO / "does-not-exist.zip"))
    assert r.returncode != 0
    assert "BLOCKED" in r.stderr


def test_stress_missing_pc_file():
    r = run("scripts/pin_foundation.py", "--pc-pinned",
            str(REPO / "does-not-exist.pdf"))
    assert r.returncode != 0
    assert "BLOCKED" in r.stderr


def test_stress_empty_zip():
    pinned = {p: (REPO / p).read_bytes() for p in
              ("FOUNDATION_MANIFEST.json", "PC_PARENT_MANIFEST.json",
               "audits/legacy/LEGACY_FILE_MANIFEST.json")}
    try:
        with tempfile.TemporaryDirectory() as tmp:
            zp = Path(tmp) / "empty.zip"
            with zipfile.ZipFile(zp, "w"):
                pass
            r = run("scripts/pin_foundation.py", "--legacy-zip", str(zp),
                    "--pc-alt", str(REPO / "LICENSE"))
            assert r.returncode == 0  # builds; count 0 is honest, not error
    finally:
        for p, b in pinned.items():
            (REPO / p).write_bytes(b)
    r = run("scripts/pin_foundation.py", "--check")
    assert r.returncode == 0  # committed manifests intact after restore


def test_mutation_corrupted_manifest_hash():
    backup = MANIFEST.read_bytes()
    try:
        obj = json.loads(backup)
        obj["operative_spec"]["sha256"] = "0" * 64
        MANIFEST.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")
        r = run("scripts/pin_foundation.py", "--check")
        assert r.returncode != 0
        assert "MISMATCH" in r.stderr or "FAIL" in r.stderr
    finally:
        MANIFEST.write_bytes(backup)


def test_mutation_malformed_manifest():
    backup = MANIFEST.read_bytes()
    try:
        MANIFEST.write_text("{not json", encoding="utf-8")
        r = run("scripts/pin_foundation.py", "--check")
        assert r.returncode != 0
    finally:
        MANIFEST.write_bytes(backup)


def test_mutation_unlabeled_fixture():
    backup = INDEX.read_bytes()
    try:
        obj = json.loads(backup)
        obj["entries"][0]["label"] = "OBSERVATIONAL_RAW"
        INDEX.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")
        r = run("scripts/migrate_legacy_fixtures.py", "--check")
        assert r.returncode != 0
    finally:
        INDEX.write_bytes(backup)


def test_mutation_binary_fixture():
    backup = INDEX.read_bytes()
    try:
        obj = json.loads(backup)
        obj["entries"].append({"name": "evil.h5", "size": 10,
                               "label": "LEGACY_HISTORICAL"})
        INDEX.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")
        r = run("scripts/migrate_legacy_fixtures.py", "--check")
        assert r.returncode != 0
    finally:
        INDEX.write_bytes(backup)


def test_mutation_fresh_labeled_fixture():
    backup = INDEX.read_bytes()
    try:
        obj = json.loads(backup)
        obj["entries"][0]["label"] = "FRESH_QUALIFICATION_HOLDOUT"
        INDEX.write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")
        r = run("scripts/migrate_legacy_fixtures.py", "--check")
        assert r.returncode != 0
    finally:
        INDEX.write_bytes(backup)


def test_redteam_removed_archaeology_doc():
    """Removing a required artifact must trip the independent auditor."""
    target = REPO / "audits" / "legacy" / "LEGACY_ARCHAEOLOGY.md"
    backup = target.read_bytes()
    try:
        target.unlink()
        r = run("scripts/audit_foundation.py")
        assert r.returncode != 0
        assert "LEGACY_ARCHAEOLOGY.md" in r.stderr
    finally:
        target.write_bytes(backup)


def test_post_stress_integrity():
    """After all backup/restore stress cases, committed pins still verify."""
    r = run("scripts/pin_foundation.py", "--check")
    assert r.returncode == 0
    r = run("scripts/migrate_legacy_fixtures.py", "--check")
    assert r.returncode == 0
    r = run("scripts/audit_foundation.py")
    assert r.returncode == 0
