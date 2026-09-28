"""WP-0 foundation pinning (COL-PC-v1.0).

Builds hash-bound foundation manifests deterministically (no timestamps,
sorted keys, UTF-8, LF) and verifies them with --check (rebuild to temp dir
+ byte comparison). Any missing source fails closed with nonzero exit.

Contract: WP-0-REQ-005/006/008/011/013/017.
"""
import argparse
import hashlib
import json
import sys
import tempfile
import zipfile
from pathlib import Path

# WP-0 STEP 01: Declare frozen foundation inputs.
print("[WP-0][STEP 01] Declaring frozen foundation inputs")

REPO = Path(__file__).resolve().parent.parent
SPEC = REPO / "IMPLEMENTATION_SPEC.md"
AUDITS = [
    REPO / "audits" / "COUNCIL-PC-v1.0_IMPLEMENTATION_SPEC_ORIGINAL.md",
    REPO / "audits" / "PROVIDER_MIGRATION_AUDIT.md",
    REPO / "audits" / "SPLAY-AM-MST-LIQ-v0.4_SPEC.txt",
]
LEGACY_ZIP_DEFAULT = (
    Path(r"C:\Users\Saif malik\Downloads\Council-Of-Lords-main.zip"))
PC_PINNED_DEFAULT = Path(
    r"C:\Users\Saif malik\OneDrive\Documents\Desktop\Perception Closure"
    r"\Perceptive Closure Identifying Authorization-Resource Counterfactuals.pdf")
PC_ALTERNATES_DEFAULT = [
    Path(r"C:\Users\Saif malik\Downloads\Perceptive_Closure_Identifying_Authorization_Resource_Counterfactuals.pdf"),
    Path(r"C:\Users\Saif malik\Downloads\Perceptive_Closure_Identifying_Authorization_Resource_Counterfactuals (1).pdf"),
    Path(r"C:\Users\Saif malik\Downloads\Perceptive_Closure_Identifying_Authorization_Resource_Counterfactuals (2).pdf"),
    Path(r"C:\Users\Saif malik\Downloads\Perceptive_Closure_FINAL.pdf"),
]

OUT_FOUNDATION = REPO / "FOUNDATION_MANIFEST.json"
OUT_PC = REPO / "PC_PARENT_MANIFEST.json"
OUT_LEGACY_FILES = REPO / "audits" / "legacy" / "LEGACY_FILE_MANIFEST.json"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()


def file_record(path):
    data = path.read_bytes()
    text = data.decode("utf-8")
    return {
        "path": path.name,
        "sha256": hashlib.sha256(data).hexdigest(),
        "bytes": len(data),
        "lines": text.count("\n") + 1,
    }


def dump_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(obj, sort_keys=True, indent=2,
                         ensure_ascii=False) + "\n"
    path.write_text(payload, encoding="utf-8", newline="\n")
    return payload


def build(legacy_zip, pc_pinned, pc_alternates, out_dir):
    """Build the three manifests into out_dir. Returns dict of name->bytes."""
    # WP-0 STEP 02: Verify every source exists before hashing (fail closed).
    print("[WP-0][STEP 02] Verifying every source exists before hashing")
    missing = []
    for p in [SPEC, *AUDITS, legacy_zip, pc_pinned, *pc_alternates]:
        if not p.is_file():
            missing.append(str(p))
    if missing:
        for m in missing:
            print(f"BLOCKED missing source: {m}", file=sys.stderr)
        print("SPEC_CONFLICT/BLOCKED: foundation pin impossible; "
              "WP-1..WP-8 NOT_REACHED", file=sys.stderr)
        raise SystemExit(2)

    # WP-0 STEP 03: Hash operative spec and audits.
    print("[WP-0][STEP 03] Hashing operative spec and audits")
    spec_rec = file_record(SPEC)
    spec_rec["path"] = "IMPLEMENTATION_SPEC.md"
    audit_recs = []
    for a in AUDITS:
        r = file_record(a)
        r["path"] = "audits/" + a.name
        audit_recs.append(r)

    # WP-0 STEP 04: List legacy zip entries (namelist only, no extraction).
    print("[WP-0][STEP 04] Listing legacy zip entries without extraction")
    with zipfile.ZipFile(legacy_zip) as z:
        infos = sorted(z.infolist(), key=lambda i: i.filename)
        entries = [{"name": i.filename, "size": i.file_size,
                    "crc32": format(i.CRC & 0xFFFFFFFF, "08x")}
                   for i in infos if not i.is_dir()]
    legacy_rec = {"zip_sha256": sha256_file(legacy_zip),
                  "zip_bytes": legacy_zip.stat().st_size,
                  "zip_source_path": str(legacy_zip),
                  "entries": len(entries)}

    # WP-0 STEP 05: Record PC parent (pinned copy + observed alternates).
    print("[WP-0][STEP 05] Recording PC parent pin and alternates")
    pc_pinned_rec = {"filename": pc_pinned.name,
                     "source_path": str(pc_pinned),
                     "sha256": sha256_file(pc_pinned),
                     "bytes": pc_pinned.stat().st_size,
                     "role": "PINNED_NORMATIVE_PARENT"}
    pc_alts = [{"filename": p.name, "source_path": str(p),
                "sha256": sha256_file(p),
                "bytes": p.stat().st_size,
                "role": "OBSERVED_ALTERNATE_NON_NORMATIVE"}
               for p in pc_alternates]

    # WP-0 STEP 06: Emit deterministic manifests.
    print("[WP-0][STEP 06] Emitting deterministic manifests")
    foundation = {
        "experiment": "COUNCIL-PC-v1.0",
        "producer": "scripts/pin_foundation.py",
        "operative_spec": spec_rec,
        "audits": audit_recs,
        "legacy": legacy_rec,
        "pc_parent_manifest": "PC_PARENT_MANIFEST.json",
        "legacy_file_manifest": "audits/legacy/LEGACY_FILE_MANIFEST.json",
    }
    pc_manifest = {
        "experiment": "COUNCIL-PC-v1.0",
        "conceptual_parent": "PERCEPTIVE CLOSURE: "
        "IDENTIFYING AUTHORIZATION-RESOURCE COUNTERFACTUALS",
        "pinned": pc_pinned_rec,
        "alternates": pc_alts,
        "policy": "Pinned copy is the normative parent version. "
        "Alternates are observed evidence only, never normative.",
    }
    legacy_files = {
        "experiment": "COUNCIL-PC-v1.0",
        "zip_sha256": legacy_rec["zip_sha256"],
        "count": len(entries),
        "entries": entries,
    }
    out = {}
    out["FOUNDATION_MANIFEST.json"] = dump_json(
        out_dir / "FOUNDATION_MANIFEST.json", foundation)
    out["PC_PARENT_MANIFEST.json"] = dump_json(
        out_dir / "PC_PARENT_MANIFEST.json", pc_manifest)
    (out_dir / "audits" / "legacy").mkdir(parents=True, exist_ok=True)
    out["audits/legacy/LEGACY_FILE_MANIFEST.json"] = dump_json(
        out_dir / "audits" / "legacy" / "LEGACY_FILE_MANIFEST.json",
        legacy_files)
    for name, payload in out.items():
        print(f"[WP-0][STEP 06] wrote {name} "
              f"sha256={hashlib.sha256(payload.encode()).hexdigest()}")
    return out


def check(legacy_zip, pc_pinned, pc_alternates):
    """Rebuild to temp dir and byte-compare against committed manifests."""
    # WP-0 STEP 07: Independent rebuild-and-compare verification.
    print("[WP-0][STEP 07] Rebuilding to temp dir for byte comparison")
    with tempfile.TemporaryDirectory() as tmp:
        fresh = build(legacy_zip, pc_pinned, pc_alternates, Path(tmp))
        committed = {
            "FOUNDATION_MANIFEST.json": OUT_FOUNDATION,
            "PC_PARENT_MANIFEST.json": OUT_PC,
            "audits/legacy/LEGACY_FILE_MANIFEST.json": OUT_LEGACY_FILES,
        }
        ok = True
        for name, payload in fresh.items():
            disk = committed[name].read_bytes().decode("utf-8")
            if disk != payload:
                print(f"MISMATCH {name}", file=sys.stderr)
                ok = False
            else:
                print(f"[WP-0][STEP 07] match {name}")
        # WP-0 STEP 08: Inline schema validation (keys present, 64-hex).
        print("[WP-0][STEP 08] Validating manifest schema")
        for name in committed:
            obj = json.loads(fresh[name])
            if not isinstance(obj, dict) or "experiment" not in obj:
                print(f"SCHEMA-FAIL {name}", file=sys.stderr)
                ok = False
        for rec in [json.loads(fresh["FOUNDATION_MANIFEST.json"])["operative_spec"]] + \
                json.loads(fresh["FOUNDATION_MANIFEST.json"])["audits"]:
            h = rec.get("sha256", "")
            if len(h) != 64 or any(c not in "0123456789abcdef" for c in h):
                print(f"HASH-FORMAT-FAIL {rec.get('path')}", file=sys.stderr)
                ok = False
        if not ok:
            print("FOUNDATION_CHECK = FAIL", file=sys.stderr)
            return 1
    print("FOUNDATION_CHECK = PASS")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--legacy-zip", default=str(LEGACY_ZIP_DEFAULT))
    ap.add_argument("--pc-pinned", default=str(PC_PINNED_DEFAULT))
    ap.add_argument("--pc-alt", action="append", default=None)
    args = ap.parse_args(argv)
    alts = [Path(p) for p in args.pc_alt] if args.pc_alt \
        else PC_ALTERNATES_DEFAULT
    if args.check:
        raise SystemExit(check(Path(args.legacy_zip), Path(args.pc_pinned),
                               alts))
    build(Path(args.legacy_zip), Path(args.pc_pinned), alts, REPO)
    print("FOUNDATION_BUILD = DONE")


if __name__ == "__main__":
    main()
