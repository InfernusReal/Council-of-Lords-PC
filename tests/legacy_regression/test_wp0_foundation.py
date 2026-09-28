"""WP-0 legacy regression scaffolding.

WP0-T01 fixture-label policy | WP0-T02 manifest integrity |
WP0-T03 pin check (delegates to pin_foundation --check) |
WP0-T04 hygiene (no binaries/secrets/.env) |
WP0-T05 determinism (byte-identical regeneration).
Full behavioral suite runs in WP-8; this scaffolding enforces the
fixture import policy and foundation integrity from WP-0 onward.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
BINARY_SUFFIXES = {".h5", ".hdf5", ".pkl", ".pickle", ".pt", ".pth",
                   ".onnx", ".joblib", ".bin"}


def test_wp0_t01_fixture_labels():
    """Every indexed fixture is LEGACY_HISTORICAL/CONTAMINATED_DEVELOPMENT, none fresh, none binary; index is complete vs live zip scan."""
    import zipfile
    index = json.loads((REPO / "audits" / "legacy"
                        / "FIXTURE_SAMPLE_INDEX.json").read_text())
    assert index["count"] == len(index["entries"]) > 0
    for e in index["entries"]:
        assert e["label"] in ("LEGACY_HISTORICAL", "CONTAMINATED_DEVELOPMENT"), e
        assert "FRESH" not in e["label"].replace("HISTORICAL", ""), e
        assert Path(e["name"]).suffix.lower() not in BINARY_SUFFIXES, e
    foundation = json.loads((REPO / "FOUNDATION_MANIFEST.json").read_text())
    zip_path = foundation["legacy"].get("zip_source_path", "")
    with zipfile.ZipFile(zip_path) as z:
        live = sorted(i.filename for i in z.infolist() if not i.is_dir()
                      and any(p in i.filename.lower() for p in
                              ("brutal_reality_test/", "clean_ultimate_test/",
                               "supreme_telescope_converter",
                               "nasa_catalog_data_generator", "_train.py",
                               "readme", "instructions-for-use")))
    assert sorted(e["name"] for e in index["entries"]) == live


def test_wp0_t02_manifest_integrity():
    """Recomputed pins equal recorded pins; counts match."""
    foundation = json.loads((REPO / "FOUNDATION_MANIFEST.json").read_text())
    spec = REPO / "IMPLEMENTATION_SPEC.md"
    data = spec.read_bytes()
    assert hashlib.sha256(data).hexdigest() == foundation["operative_spec"]["sha256"]
    assert foundation["operative_spec"]["lines"] == data.decode().count("\n") + 1
    legacy_files = json.loads((REPO / "audits" / "legacy"
                               / "LEGACY_FILE_MANIFEST.json").read_text())
    assert legacy_files["count"] == len(legacy_files["entries"])
    assert foundation["legacy"]["entries"] == legacy_files["count"]


def test_wp0_t03_pin_check():
    """Producer self-check passes on the committed tree."""
    r = subprocess.run([sys.executable, "scripts/pin_foundation.py", "--check"],
                       cwd=REPO, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert "FOUNDATION_CHECK = PASS" in r.stdout


def test_wp0_t04_hygiene():
    """No binaries, secrets, .env, or __pycache__ tracked outside .git."""
    bad = []
    for f in REPO.rglob("*"):
        if ".git" in f.parts or not f.is_file():
            continue
        if f.suffix.lower() in BINARY_SUFFIXES:
            bad.append(str(f))
        if f.name == ".env" or f.name == "__pycache__":
            bad.append(str(f))
    assert bad == []
    env_example = (REPO / ".env.example").read_text()
    assert "OPENCODE_API_KEY=" in env_example
    assert "sk-" not in env_example


def test_wp0_t05_determinism(tmp_path):
    """Two manifest regenerations are byte-identical."""
    r1 = subprocess.run(
        [sys.executable, "scripts/pin_foundation.py"], cwd=REPO,
        capture_output=True, text=True)
    assert r1.returncode == 0, r1.stderr
    first = {p: (REPO / p).read_bytes() for p in
             ("FOUNDATION_MANIFEST.json", "PC_PARENT_MANIFEST.json",
              "audits/legacy/LEGACY_FILE_MANIFEST.json")}
    r2 = subprocess.run(
        [sys.executable, "scripts/pin_foundation.py"], cwd=REPO,
        capture_output=True, text=True)
    assert r2.returncode == 0, r2.stderr
    for p, b in first.items():
        assert (REPO / p).read_bytes() == b, p
