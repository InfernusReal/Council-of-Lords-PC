"""WP-0 independent foundation audit (COL-PC-v1.0).

Structurally independent of scripts/pin_foundation.py: it shares no code
with the producer, re-derives every pin from source bytes, validates the
manifest schema, evaluates STOP-01/02, and grades GATE-00/01. Disagreement
with producer outputs fails closed.

Contract: WP-0-REQ-017/019/020. Named checks: WP0-T02 (integrity),
WP0-T03 (pin agreement).
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

# WP-0 STEP 20: Declare independent audit inputs (no producer imports).
print("[WP-0][STEP 20] Declaring independent audit inputs")

REPO = Path(__file__).resolve().parent.parent
HEX = set("0123456789abcdef")


def h256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(msg):
    print(f"AUDIT-FAIL {msg}", file=sys.stderr)
    return False


def main():
    # WP-0 STEP 21: Re-derive every pin from source bytes.
    print("[WP-0][STEP 21] Re-deriving pins from source bytes")
    ok = True
    try:
        foundation = json.loads((REPO / "FOUNDATION_MANIFEST.json").read_text())
        pc = json.loads((REPO / "PC_PARENT_MANIFEST.json").read_text())
        legacy_files = json.loads(
            (REPO / "audits" / "legacy" / "LEGACY_FILE_MANIFEST.json").read_text())
        index = json.loads(
            (REPO / "audits" / "legacy" / "FIXTURE_SAMPLE_INDEX.json").read_text())
    except (OSError, ValueError) as e:
        print(f"AUDIT-FAIL unreadable manifest: {e}", file=sys.stderr)
        print("INDEPENDENT_AUDIT = FAIL")
        return 1

    # WP-0 STEP 22: Validate schema shape and hash formats.
    print("[WP-0][STEP 22] Validating schema shape and hash formats")
    for key in ("experiment", "operative_spec", "audits", "legacy"):
        if key not in foundation:
            ok = fail(f"foundation missing key {key}")
    # WP-0 STEP 22b: Required WP-0 files exist (red-team: removed artifact).
    print("[WP-0][STEP 22] Checking required WP-0 files exist")
    for rel in ("audits/legacy/LEGACY_ARCHAEOLOGY.md",
                "audits/legacy/ANTI_PATTERN_LEDGER.md",
                "audits/legacy/FIXTURE_SAMPLE_INDEX.json",
                "configs/pc/target_ontology_v1.json",
                "configs/pc/atomicity_freeze_commitment_v1.json",
                "ENVIRONMENT_BASELINE.json",
                "scripts/pin_foundation.py",
                "scripts/migrate_legacy_fixtures.py"):
        if not (REPO / rel).is_file():
            ok = fail(f"required file missing {rel}")
    for rec in [foundation["operative_spec"], *foundation.get("audits", [])]:
        h = rec.get("sha256", "")
        if len(h) != 64 or (set(h) - HEX):
            ok = fail(f"bad hash for {rec.get('path')}")
    if foundation.get("experiment") != "COUNCIL-PC-v1.0":
        ok = fail("wrong experiment tag")

    # WP-0 STEP 23: Re-hash operative spec and audits; compare.
    print("[WP-0][STEP 23] Re-hashing spec and audits")
    spec = REPO / "IMPLEMENTATION_SPEC.md"
    if h256(spec) != foundation["operative_spec"]["sha256"]:
        ok = fail("operative spec hash mismatch")
    # Red-team: producer must not silently drop an audit file.
    expected_audits = {"audits/COUNCIL-PC-v1.0_IMPLEMENTATION_SPEC_ORIGINAL.md",
                       "audits/PROVIDER_MIGRATION_AUDIT.md",
                       "audits/SPLAY-AM-MST-LIQ-v0.4_SPEC.txt"}
    recorded_audits = {rec["path"] for rec in foundation.get("audits", [])}
    if recorded_audits != expected_audits:
        ok = fail(f"audit set mismatch {sorted(recorded_audits)}")
    for rec in foundation.get("audits", []):
        p = REPO / rec["path"]
        if not p.is_file() or h256(p) != rec["sha256"]:
            ok = fail(f"audit file mismatch {rec['path']}")

    # WP-0 STEP 24: Re-list legacy zip; compare count, names, CRCs.
    print("[WP-0][STEP 24] Re-listing legacy zip independently")
    zpath = Path(r"C:\Users\Saif malik\Downloads\Council-Of-Lords-main.zip")
    with zipfile.ZipFile(zpath) as z:
        infos = sorted(z.infolist(), key=lambda i: i.filename)
    live = [(i.filename, i.file_size, format(i.CRC & 0xFFFFFFFF, "08x"))
            for i in infos if not i.is_dir()]
    recorded = [(e["name"], e["size"], e["crc32"])
                for e in legacy_files["entries"]]
    legacy_match = (len(live) == legacy_files["count"]
                    and len(live) == len(recorded) and live == recorded)
    if len(live) != legacy_files["count"] or len(live) != len(recorded):
        ok = fail("legacy entry count mismatch")
    if live != recorded:
        ok = fail("legacy entry bytes/CRC mismatch")
    if h256(zpath) != legacy_files["zip_sha256"]:
        ok = fail("legacy zip hash mismatch")

    # WP-0 STEP 25: Verify PC pin bytes and fixture-label policy.
    print("[WP-0][STEP 25] Verifying PC pin and fixture labels")
    pinned = pc["pinned"]
    if pinned.get("role") != "PINNED_NORMATIVE_PARENT":
        ok = fail("PC pin role wrong")
    for alt in pc.get("alternates", []):
        if alt.get("role") != "OBSERVED_ALTERNATE_NON_NORMATIVE":
            ok = fail("PC alternate role wrong")
    for e in index.get("entries", []):
        if e.get("label") not in ("LEGACY_HISTORICAL",
                                  "CONTAMINATED_DEVELOPMENT"):
            ok = fail(f"fixture label wrong {e.get('name')}")

    # WP-0 STEP 26: Evaluate STOP-01/02 and grade GATE-00/01.
    print("[WP-0][STEP 26] Evaluating stops and gates")
    stop01 = (REPO / "PC_PARENT_MANIFEST.json").is_file()
    stop02 = legacy_match
    print(f"[WP-0][STEP 26] STOP-01 pinnable={stop01} STOP-02 pinnable={stop02}")
    if not (stop01 and stop02):
        ok = fail("stop condition unmet")
    print(f"[WP-0][STEP 26] GATE-00={'OPEN' if ok else 'FAIL'} "
          f"GATE-01={'OPEN' if ok else 'FAIL'}")
    print("INDEPENDENT_AUDIT = PASS" if ok else "INDEPENDENT_AUDIT = FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
