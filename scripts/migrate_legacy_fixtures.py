"""WP-0 legacy fixture migration skeleton (COL-PC-v1.0).

Lists candidate legacy fixtures from the legacy zip namelist, assigns each
the LEGACY_HISTORICAL label, and enforces the binary gate: fixture entries
that are model binaries (h5/pkl/pt/onnx/joblib/bin) are REJECTED from the
index. Full materialization lives in WP-1/WP-8; this skeleton establishes
the import policy. Missing zip fails closed with nonzero exit.

Contract: WP-0-REQ-014/016/018.
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path

# WP-0 STEP 10: Declare skeleton inputs and binary gate.
print("[WP-0][STEP 10] Declaring legacy migration skeleton inputs")

REPO = Path(__file__).resolve().parent.parent
LEGACY_ZIP_DEFAULT = (
    Path(r"C:\Users\Saif malik\Downloads\Council-Of-Lords-main.zip"))
OUT_INDEX = REPO / "audits" / "legacy" / "FIXTURE_SAMPLE_INDEX.json"
BINARY_SUFFIXES = {".h5", ".hdf5", ".pkl", ".pickle", ".pt", ".pth",
                   ".onnx", ".joblib", ".bin"}
SIZE_GATE_BYTES = 5 * 1024 * 1024
FIXTURE_PATTERNS = ("brutal_reality_test/", "clean_ultimate_test/",
                    "supreme_telescope_converter", "nasa_catalog_data_generator",
                    "_train.py", "README", "instructions-for-use")


def scan(zip_path):
    """Return candidate fixture entries (metadata only, no extraction)."""
    # WP-0 STEP 11: Scan zip namelist for candidate fixtures.
    print("[WP-0][STEP 11] Scanning zip namelist for candidate fixtures")
    if not zip_path.is_file():
        print(f"BLOCKED missing legacy zip: {zip_path}", file=sys.stderr)
        raise SystemExit(2)
    with zipfile.ZipFile(zip_path) as z:
        infos = sorted(z.infolist(), key=lambda i: i.filename)
    cands = [i for i in infos
             if not i.is_dir()
             and any(p.lower() in i.filename.lower()
                     for p in FIXTURE_PATTERNS)]
    return cands


def build_index(zip_path, out_path):
    # WP-0 STEP 12: Build labeled fixture index, rejecting binaries.
    print("[WP-0][STEP 12] Building labeled fixture index")
    rejected = []
    entries = []
    for i in scan(zip_path):
        suffix = Path(i.filename).suffix.lower()
        if suffix in BINARY_SUFFIXES:
            rejected.append(i.filename)
            continue
        entries.append({"name": i.filename, "size": i.file_size,
                        "label": "LEGACY_HISTORICAL",
                        "note": "archaeological reference only; "
                        "never observational, never fresh, never qualified"})
    index = {"experiment": "COUNCIL-PC-v1.0",
             "policy": "Every indexed fixture is LEGACY_HISTORICAL. "
             "Binaries are rejected from the index. "
             "Historical models enter only as LEGACY_UNQUALIFIED wrappers.",
             "binary_gate": sorted(BINARY_SUFFIXES),
             "size_gate_bytes": SIZE_GATE_BYTES,
             "count": len(entries),
             "rejected_binaries": len(rejected),
             "entries": entries}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(index, sort_keys=True, indent=2) + "\n",
                        encoding="utf-8", newline="\n")
    print(f"[WP-0][STEP 12] indexed {len(entries)} fixtures, "
          f"rejected {len(rejected)} binaries -> {out_path.name}")
    return index


def check(zip_path, out_path):
    """Verify index labels and gates against the live zip."""
    # WP-0 STEP 13: Verify fixture labels and gates.
    print("[WP-0][STEP 13] Verifying fixture labels and gates")
    if not out_path.is_file():
        print(f"MISMATCH missing index: {out_path}", file=sys.stderr)
        return 1
    index = json.loads(out_path.read_text(encoding="utf-8"))
    ok = True
    live = {i.filename for i in scan(zip_path)}
    for e in index.get("entries", []):
        if e.get("label") not in ("LEGACY_HISTORICAL",
                                  "CONTAMINATED_DEVELOPMENT"):
            print(f"LABEL-FAIL {e.get('name')}", file=sys.stderr)
            ok = False
        if e.get("name") not in live:
            print(f"STALE-ENTRY {e.get('name')}", file=sys.stderr)
            ok = False
        if Path(e.get("name", "")).suffix.lower() in BINARY_SUFFIXES:
            print(f"BINARY-LEAK {e.get('name')}", file=sys.stderr)
            ok = False
    fresh = [e for e in index.get("entries", [])
             if "FRESH" in str(e.get("label", "")).upper()
             and "HISTORICAL" not in str(e.get("label", "")).upper()]
    if fresh:
        print(f"FRESH-LABEL-FAIL {fresh}", file=sys.stderr)
        ok = False
    print("MIGRATION_CHECK = PASS" if ok else "MIGRATION_CHECK = FAIL")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--legacy-zip", default=str(LEGACY_ZIP_DEFAULT))
    args = ap.parse_args(argv)
    if args.check:
        raise SystemExit(check(Path(args.legacy_zip), OUT_INDEX))
    build_index(Path(args.legacy_zip), OUT_INDEX)
    print("MIGRATION_BUILD = DONE")


if __name__ == "__main__":
    main()
