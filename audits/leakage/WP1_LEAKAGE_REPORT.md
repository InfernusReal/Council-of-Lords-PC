# WP-1 leakage report — empty population + mechanism proof

**Status:** WP-1 trains no models and defines no training population. There is no
WP-1 training corpus that could leak. This report records the grouping mechanism,
its proof obligations, and a worked example on legacy fixture identities.

## Mechanism (COL-T01/T02 control)

`splits.py object_group_split`: deterministic hash-bucket assignment
(`sha256(object_id) mod 1000`), all records of one protected identity in one
split by construction; `leakage_report` audits overlap (must be exactly empty)
and mission strata. Independent recheck: the test suite recomputes disjointness
with set logic independent of the producer (`tests/forge/test_object_grouping.py`).

## Worked example (legacy fixture identities, NOT a training population)

- Population: 127 `FIXTURE_SAMPLE_INDEX.json` paths as pseudo-identities,
  mission heuristic from filename (`Kepler`/`TESS`/`legacy-mixed`).
- Split: train=106, test=21. Overlap=0 (disjoint=True).
- Strata: legacy-mixed train=102/test=21; Kepler train=2/test=0; TESS train=2/test=0.
- Meaning: mechanism demonstration only. Legacy fixtures remain
  `LEGACY_HISTORICAL`; none are observational, fresh, or training data.

## Anti-overfitting posture (WP-1)

NO ML MODEL TRAINED. Development fixtures only (synthetic/legacy-labeled).
No validation/test split consumed as training. Seeds recorded where RNG is
used (WP-1 producers use hash-based determinism; no RNG). No holdout exists;
nothing is labeled fresh. Protected-identity leakage blocks downstream use
(COL-STOP-10 handler: freeze splits, quarantine dataset version).
