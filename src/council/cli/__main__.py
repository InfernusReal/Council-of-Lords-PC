"""Deterministic Council CLI skeleton: data verbs (WP-1).

`col data ingest` builds a LightCurve from CSV columns + manifest.
`col data build` emits a dataset release manifest (skeleton).
`col data audit` verifies a manifest sidecar hash (and registry closure).
JSON to stdout; manifests to data/manifests/. Contract: WP-1-REQ-017.
Run from repo root with PYTHONPATH=src (stdlib + numpy only).
"""
from __future__ import annotations

import csv
import json
import sys

# WP-1 STEP 15: Fix deterministic data CLI verbs.
print("[WP-1][STEP 15] Fixing deterministic data CLI verbs", file=sys.stderr)


def _read_csv_numbers(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    cols = rows[0].keys() if rows else []
    get = lambda c: [float(r[c]) for r in rows] if c in cols else None
    return {"time": get("time"), "flux": get("flux"),
            "flux_err": get("flux_err"), "quality": get("quality")}


def cmd_ingest(args) -> int:
    """col data ingest --csv PATH --mission M --target T [--sector S]."""
    import argparse
    ap = argparse.ArgumentParser(prog="col data ingest")
    ap.add_argument("--csv", required=True)
    ap.add_argument("--mission", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--sector", default="")
    ns = ap.parse_args(args)
    from council.data.lightcurve import ingest_lightcurve
    from forge.datasets.manifests import manifest_hash
    cols = _read_csv_numbers(ns.csv)
    if cols["time"] is None or cols["flux"] is None:
        print("CLI-FAIL csv requires time,flux columns", file=sys.stderr)
        return 2
    lc = ingest_lightcurve(cols["time"], cols["flux"], cols["flux_err"],
                           cols["quality"], mission=ns.mission,
                           target_id=ns.target,
                           sector_or_quarter=ns.sector)
    out = {"target_id": lc.target_id, "n": int(lc.time.size),
           "raw_hash": lc.raw_hash, "time_system": lc.time_system,
           "flux_definition": lc.flux_definition}
    out["manifest_hash"] = manifest_hash(out)
    print("[WP-1][STEP 15] Ingested via CLI "
          f"{lc.target_id} n={out['n']}", file=sys.stderr)
    print(json.dumps(out, sort_keys=True, indent=2))
    return 0


def cmd_build(args) -> int:
    """col data build --task T --version V --entries JSON (skeleton)."""
    import argparse
    ap = argparse.ArgumentParser(prog="col data build")
    ap.add_argument("--task", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--entries", required=True)
    ns = ap.parse_args(args)
    from forge.datasets.factory import create_dataset_release
    from forge.datasets.manifests import write_manifest
    from pathlib import Path
    entries = json.loads(ns.entries)
    release = create_dataset_release(ns.task, ns.version, entries)
    path = Path("data/manifests") / (release["release_id"] + ".json")
    write_manifest(release, path)
    print(f"[WP-1][STEP 15] Built release {release['release_id']}",
          file=sys.stderr)
    print(json.dumps(release, sort_keys=True, indent=2))
    return 0


def cmd_audit(args) -> int:
    """col data audit --manifest PATH | --registry."""
    import argparse
    ap = argparse.ArgumentParser(prog="col data audit")
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--registry", action="store_true")
    ns = ap.parse_args(args)
    if ns.registry:
        import hashlib
        from forge.datasets.source_registry import closure_audit
        from forge.datasets.manifests import verify_manifest
        from pathlib import Path
        base = Path("data/manifests")
        reg_path = base / "SOURCE_REGISTRY_v1.json"
        led_path = base / "SOURCE_STATUS_LEDGER.json"
        clo_path = Path("audits/WP1_SOURCE_CLOSURE.json")
        ok_files = all(p.is_file() for p in (reg_path, led_path, clo_path))
        ok_hashes = (verify_manifest(reg_path) and verify_manifest(led_path)
                     and verify_manifest(clo_path))
        reg = json.loads(reg_path.read_text(encoding="utf-8")) if ok_files else {"entries": []}
        verdict = closure_audit(reg.get("entries"))
        recorded = json.loads(clo_path.read_text(encoding="utf-8")) if ok_files else {}
        ledger = json.loads(led_path.read_text(encoding="utf-8")) if ok_files else {}
        reg_sha = hashlib.sha256(reg_path.read_bytes()).hexdigest() if ok_files else ""
        led_sha = hashlib.sha256(led_path.read_bytes()).hexdigest() if ok_files else ""
        bound = (recorded.get("registry_sha256") == reg_sha
                 and recorded.get("ledger_sha256") == led_sha
                 and recorded.get("verdict") == "CLOSED"
                 and ledger.get("statuses")
                 == {e.get("source_family"): e.get("acquisition_status")
                     for e in reg.get("entries", [])})
        verdict = {**verdict, "files_present": ok_files,
                   "hashes_match": ok_hashes, "closure_bound": bool(bound)}
        if verdict["verdict"] == "CLOSED" and not (ok_files and ok_hashes and bound):
            verdict = {**verdict, "verdict": "OPEN",
                       "problems": verdict.get("problems", [])
                       + ["closure evidence unbound"]}
            verdict["all_terminal"] = False
        print(json.dumps(verdict, sort_keys=True, indent=2))
        print(f"[WP-1][STEP 15] Registry audit {verdict['verdict']}",
              file=sys.stderr)
        return 0 if verdict["verdict"] == "CLOSED" else 3
    if not ns.manifest:
        print("CLI-FAIL --manifest or --registry required", file=sys.stderr)
        return 2
    from forge.datasets.manifests import verify_manifest
    ok = verify_manifest(ns.manifest)
    print(json.dumps({"manifest": ns.manifest, "valid": ok},
                     sort_keys=True, indent=2))
    print(f"[WP-1][STEP 15] Manifest audit valid={ok}", file=sys.stderr)
    return 0 if ok else 3


COMMANDS = {"ingest": cmd_ingest, "build": cmd_build, "audit": cmd_audit}


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) < 2 or argv[0] != "data" or argv[1] not in COMMANDS:
        print("usage: col data {ingest|build|audit} ...", file=sys.stderr)
        return 2
    return COMMANDS[argv[1]](argv[2:])


if __name__ == "__main__":
    raise SystemExit(main())
