"""Dataset Factory skeleton: versioned release manifests (WP-1).

Full factory (TaskSpec binding, transform graphs, stress populations) is
WP-4. This skeleton freezes the release identity, entry validation against
the Sec-15.1/15.4 vocabularies, and hash binding. Contract: WP-1-REQ-006.
"""
from __future__ import annotations

from .manifests import manifest_hash
import sys

# WP-1 STEP 08: Fix dataset release skeleton.
print("[WP-1][STEP 08] Fixing dataset release skeleton", file=sys.stderr)

SOURCE_CLASSES = ("OBSERVATIONAL_RAW", "OBSERVATIONAL_DERIVED",
                  "CATALOG_LABELLED", "SIMULATED_PHYSICS", "SYNTHETIC_STRESS",
                  "LLM_PROPOSED_SCENARIO", "LEGACY_HISTORICAL",
                  "CONTAMINATED_DEVELOPMENT", "HIDDEN_HOLDOUT")
LABEL_CONFIDENCE = ("CONFIRMED", "HIGH_CONFIDENCE", "CATALOG_CANDIDATE",
                    "KNOWN_FALSE_POSITIVE", "SIMULATED_KNOWN", "AMBIGUOUS",
                    "UNRESOLVED")
FACTORY_VERSION = "1.0.0-skeleton"


def create_dataset_release(task: str, version: str, entries: list,
                           split_policy: str = "object-level-v1") -> dict:
    """Validate entries and emit a versioned release manifest (pure).

    Entry: {object_id, source_class, label_confidence, mission}.
    Release id: COL-DATASET-<task>-v<version>. Raises on any violation.
    """
    if not task or not version:
        raise ValueError("task and version are required")
    seen = set()
    clean = []
    allowed_keys = {"object_id", "source_class", "label_confidence", "mission"}
    for e in entries:
        extra = set(e) - allowed_keys
        if extra:
            raise ValueError(f"unadmitted scratch fields rejected: {sorted(extra)}")
        oid = e.get("object_id", "")
        if not oid or oid in seen:
            raise ValueError(f"duplicate/blank object_id: {oid!r}")
        seen.add(oid)
        if e.get("source_class") not in SOURCE_CLASSES:
            raise ValueError(f"illegal source_class: {e.get('source_class')!r}")
        if e.get("label_confidence") not in LABEL_CONFIDENCE:
            raise ValueError(f"illegal label_confidence: {e.get('label_confidence')!r}")
        if not e.get("mission"):
            raise ValueError(f"missing mission for {oid!r}")
        clean.append({"object_id": oid, "source_class": e["source_class"],
                      "label_confidence": e["label_confidence"],
                      "mission": e["mission"]})
    release = {"release_id": f"COL-DATASET-{task}-v{version}",
               "task": task, "version": version,
               "factory_version": FACTORY_VERSION,
               "split_policy": split_policy,
               "n_entries": len(clean), "entries": clean}
    release["manifest_hash"] = manifest_hash(release)
    print(f"[WP-1][STEP 08] Release {release['release_id']} "
          f"n={len(clean)}", file=sys.stderr)
    return release
