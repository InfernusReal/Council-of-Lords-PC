"""Frozen source registry + status ledger + acquisition closure audit (WP-1).

Implements Sec-15.6: 17 required families, 14-field entries, exactly-one
terminal state per entry, identity reconciliation, and the COL-GATE-22
closure verdict (coverage closure, never "all downloaded"). No URLs, counts,
versions, or availability are fabricated: unavailable entries say so with
archived reasons; the single INGESTED entry cites measured hashes.
Framework + mechanism ship in WP-1; bulky materialization follows the frozen
registry later. Contract: WP-1-REQ-009/016; COL-SRC-*.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from .manifests import write_manifest

# WP-1 STEP 10: Fix the frozen source-registry doctrine tables.
print("[WP-1][STEP 10] Fixing frozen source-registry doctrine tables",
      file=sys.stderr)

REPO = Path(__file__).resolve().parent.parent.parent
POLICY = REPO / "configs" / "datasets" / "wp1_acquisition_policy_v1.json"
LEGACY_ZIP = Path(r"C:\Users\Saif malik\Downloads\Council-Of-Lords-main.zip")

FROZEN_FAMILIES = ("OBSERVATIONAL_LIGHTCURVE", "PLANET_CANDIDATE_CATALOG",
                   "CONFIRMED_PLANET_CATALOG", "CERTIFIED_FALSE_POSITIVE",
                   "ECLIPSING_BINARY_CATALOG", "TCE_CATALOG",
                   "ROBOVETTER_METRICS", "CENTROID_DIAGNOSTICS",
                   "STELLAR_CATALOG", "NEIGHBOR_CONTAMINATION_CATALOG",
                   "INJECTION_RECOVERY", "SCRAMBLED_FALSE_ALARM",
                   "INVERTED_FALSE_ALARM", "PIPELINE_SYSTEMATIC",
                   "SIMULATED_PHYSICS", "TEACHER_PROPOSED_ADVERSARIAL",
                   "LEGACY_HISTORICAL")
ENTRY_FIELDS = ("source_id", "source_family", "source_version_or_release",
                "retrieval_date", "retrieval_method",
                "license_or_usage_status", "raw_hashes",
                "object_identity_mapping", "label_semantics", "known_biases",
                "allowed_tasks", "split_restrictions", "acquisition_status",
                "acquisition_failure_reason")
TERMINAL_STATES = ("INGESTED", "INCOMPATIBLE_WITH_DOCUMENTED_REASON",
                   "UNAVAILABLE_WITH_ARCHIVED_FAILURE",
                   "EXCLUDED_BY_FROZEN_POLICY")
ATTEMPT_SOURCES = {
    "OBSERVATIONAL_LIGHTCURVE": ["Kepler light curves", "TESS light curves"],
    "PLANET_CANDIDATE_CATALOG": ["Kepler KOIs", "TESS TOIs",
                                 "K2 candidate/false-positive populations"],
    "CONFIRMED_PLANET_CATALOG": ["NASA Exoplanet Archive products"],
    "CERTIFIED_FALSE_POSITIVE": ["Kepler Certified False Positives"],
    "ECLIPSING_BINARY_CATALOG": ["Kepler eclipsing-binary catalogs",
                                 "TESS eclipsing-binary sources"],
    "TCE_CATALOG": ["Kepler DR25", "Kepler TCEs",
                    "TESS TCE/DV products where eligible/available"],
    "ROBOVETTER_METRICS": ["Kepler Robovetter metrics"],
    "CENTROID_DIAGNOSTICS": ["TESS TCE/DV products where eligible/available"],
    "STELLAR_CATALOG": ["Gaia stellar/neighbour/context products",
                        "NASA Exoplanet Archive products"],
    "NEIGHBOR_CONTAMINATION_CATALOG": ["Gaia stellar/neighbour/context products"],
    "INJECTION_RECOVERY": ["Kepler injection/recovery products"],
    "SCRAMBLED_FALSE_ALARM": ["Kepler inverted/scrambled false-alarm products"],
    "INVERTED_FALSE_ALARM": ["Kepler inverted/scrambled false-alarm products"],
    "PIPELINE_SYSTEMATIC": ["MAST mission products",
                            "mission-quality/systematics metadata"],
    "SIMULATED_PHYSICS": ["physically generated adversarial cases"],
    "TEACHER_PROPOSED_ADVERSARIAL": [
        "Muse-proposed scenario specifications materialized deterministically"],
    "LEGACY_HISTORICAL": ["legacy snapshot (local)"],
}
REGISTRY_VERSION = "1.0.0"


def probe_local_corpus(repo: Path) -> list:
    """Real filesystem probe for matching corpora (no network).

    Scans data/ (excluding manifests) for corpus bytes. Returns found paths
    (possibly empty: an honest negative is a valid probe outcome).
    """
    # WP-1 STEP 11: Probe the local tree for matching corpora.
    print("[WP-1][STEP 11] Probing local tree for matching corpora",
          file=sys.stderr)
    found = []
    data = repo / "data"
    if data.is_dir():
        for f in sorted(data.rglob("*")):
            if not f.is_file() or "manifests" in f.parts:
                continue
            if f.suffix.lower() in (".csv", ".fits", ".h5", ".pkl", ".parquet"):
                found.append(str(f.relative_to(repo)).replace("\\", "/"))
    print(f"[WP-1][STEP 11] Probe found {len(found)} corpus files",
          file=sys.stderr)
    return found


def build_registry(policy_path: Path = POLICY,
                   repo: Path = REPO) -> tuple:
    """Build frozen registry + status ledger from the frozen policy (pure)."""
    policy = json.loads(policy_path.read_text(encoding="utf-8"))
    probed = probe_local_corpus(repo)
    assignments = policy["status_assignments"]
    if set(assignments) != set(FROZEN_FAMILIES):
        raise ValueError("policy must assign exactly the 17 frozen families")
    foundation = json.loads((repo / "FOUNDATION_MANIFEST.json").read_text())
    index = json.loads((repo / "audits" / "legacy" / "FIXTURE_SAMPLE_INDEX.json")
                       .read_text())
    entries = []
    for fam in FROZEN_FAMILIES:
        a = assignments[fam]
        if a["status"] not in TERMINAL_STATES:
            raise ValueError(f"non-terminal status for {fam}")
        if fam == "LEGACY_HISTORICAL" and a["status"] == "INGESTED":
            entry = {
                "source_id": "COL-SRC-LEGACY-001",
                "source_family": fam,
                "source_version_or_release":
                    "Council-Of-Lords-main.zip@"
                    + foundation["legacy"]["zip_sha256"][:8],
                "retrieval_date": policy["frozen_policy_date"],
                "retrieval_method": "local snapshot hash + namelist index "
                                    "(no extraction)",
                "license_or_usage_status": "UNVERIFIED (verify at use)",
                "raw_hashes": [foundation["legacy"]["zip_sha256"]],
                "object_identity_mapping": "zip-relative paths; protected "
                    "split identities assigned at dataset build",
                "label_semantics": "LEGACY_HISTORICAL for all indexed "
                    f"fixtures (n={index['count']})",
                "known_biases": "historical synthetic draws; "
                    "parallel-classifier era; see ANTI_PATTERN_LEDGER.md",
                "allowed_tasks": [],
                "split_restrictions": "object-level grouping required at use",
                "acquisition_status": "INGESTED",
                "acquisition_failure_reason": "n/a (ingested)",
                "attempted_sources": ATTEMPT_SOURCES[fam]}
        else:
            entry = {
                "source_id": f"COL-SRC-{fam}-001",
                "source_family": fam,
                "source_version_or_release": "UNESTABLISHED "
                    "(WP-1 scope: no retrieval)",
                "retrieval_date": policy["frozen_policy_date"],
                "retrieval_method": "local-corpus-probe v1 "
                                    "(filesystem scan; no network)",
                "license_or_usage_status": "UNVERIFIED "
                    "(no retrieval; verify at acquisition)",
                "raw_hashes": [],
                "object_identity_mapping": "unassigned "
                    "(assigned at dataset build under split policy)",
                "label_semantics": "undefined (source not acquired)",
                "known_biases": "uncharacterized (source not acquired)",
                "allowed_tasks": [],
                "split_restrictions": "n/a (unavailable)",
                "acquisition_status": a["status"],
                "acquisition_failure_reason": a["reason"],
                "attempted_sources": ATTEMPT_SOURCES[fam]}
        if set(entry) - {"attempted_sources"} != set(ENTRY_FIELDS):
            raise ValueError(f"entry schema drift for {fam}")
        entries.append(entry)
    registry = {"registry_version": REGISTRY_VERSION,
                "policy": "configs/datasets/wp1_acquisition_policy_v1.json",
                "policy_sha256": hashlib.sha256(
                    policy_path.read_bytes()).hexdigest(),
                "entries": entries}
    ledger = {"ledger_version": REGISTRY_VERSION,
              "probe": {"method": policy["probe"]["method"],
                        "found_corpus_files": probed},
              "identity_reconciliation": {
                  "method": "protected identities assigned at dataset "
                            "build (splits.py); registry stores raw "
                            "identity namespaces",
                  "namespaces": {"LEGACY_HISTORICAL": "zip-relative paths",
                                 "default": "unassigned"}},
              "statuses": {e["source_family"]: e["acquisition_status"]
                           for e in entries}}
    return registry, ledger


def closure_audit(entries) -> dict:
    """Verdict over entries: every family terminal exactly once (pure)."""
    counts = {s: 0 for s in TERMINAL_STATES}
    seen = set()
    problems = []
    if not isinstance(entries, list):
        return {"gate": "COL-GATE-22", "all_terminal": False,
                "counts": counts,
                "problems": [f"registry entries not a list: {type(entries).__name__}"],
                "verdict": "OPEN"}
    for pos, e in enumerate(entries):
        if not isinstance(e, dict):
            problems.append(f"entry {pos} not an object")
            continue
        fam = e.get("source_family")
        fam = e.get("source_family")
        st = e.get("acquisition_status")
        if fam in seen:
            problems.append(f"duplicate family {fam}")
        seen.add(fam)
        if st not in TERMINAL_STATES:
            problems.append(f"non-terminal {fam}: {st!r}")
        else:
            counts[st] += 1
        if st != "INGESTED" and not e.get("acquisition_failure_reason"):
            problems.append(f"missing reason {fam}")
        if st == "INGESTED" and not e.get("raw_hashes"):
            problems.append(f"missing hashes {fam}")
    missing = set(FROZEN_FAMILIES) - seen
    if missing:
        problems.append(f"silent omission {sorted(missing)}")
    verdict = {"gate": "COL-GATE-22", "all_terminal": not problems,
               "counts": counts, "problems": problems,
               "verdict": "CLOSED" if not problems else "OPEN"}
    print(f"[WP-1][STEP 11] Closure audit: {verdict['verdict']} "
          f"problems={len(problems)}", file=sys.stderr)
    return verdict


def main() -> int:
    print("[WP-1][STEP 11] Building frozen registry and closure evidence",
          file=sys.stderr)
    registry, ledger = build_registry()
    verdict = closure_audit(registry["entries"])
    reg_sha = write_manifest(registry, REPO / "data" / "manifests"
                             / "SOURCE_REGISTRY_v1.json")
    led_sha = write_manifest(ledger, REPO / "data" / "manifests"
                             / "SOURCE_STATUS_LEDGER.json")
    verdict = {**verdict, "registry_sha256": reg_sha,
               "ledger_sha256": led_sha,
               "policy_sha256": registry["policy_sha256"]}
    write_manifest(verdict, REPO / "audits" / "WP1_SOURCE_CLOSURE.json")
    print(f"[WP-1][STEP 11] GATE-22 verdict={verdict['verdict']}",
          file=sys.stderr)
    if verdict["verdict"] != "CLOSED":
        print("GATE-22 = FAIL", file=sys.stderr)
        return 3
    print("GATE-22 = CLOSED", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
