# Anti-pattern ledger — required design input (IMPLEMENTATION_SPEC.md Sec-50)

Each finding quotes the normative source, then records the WP-0 evidence and the v1.0 design rule.

## ANTI-01 — parallel classifiers over the same features

> The named specialists are largely parallel neural classifiers over the same eight catalogue-style features.

Evidence: 5 `*_train.py` specialists under `COUNCIL_OF_LORDS_NASA_NATIVE/` consuming
catalogue-style vectors. Rule: a Lord is trained for a scientific role, not a seed
(Sec-11); distinct competence axis required (WP-4 TaskSpecs).

## ANTI-02 — specialties encoded via losses/widths/thresholds

> Different "specialties" are often encoded through altered losses, layer widths, thresholds, or class weights rather than independent scientific views.

Rule: seed/width/threshold/loss-name/weight changes alone never establish a distinct
epistemic role (Sec-11). Qualification checks the competence axis (WP-6 LPC).

## ANTI-03 — hard-coded ensemble weights and boosts/penalties

> The ensemble applies hard-coded specialist weights and context-specific boosts/penalties.

Evidence: `smart_ensemble_fix.py`, `supreme_ensemble_nasa_train.py`. Rule: fixed multipliers
(e.g. 1.4x-style weights) are forbidden as a decision rule (Sec-25); reliability, if used,
is state-dependent `r_i(s)` metadata, never a vote weight; closure is PC-defined (WP-7).

## ANTI-04 — monolithic converter

> The converter bundles catalog lookup, defaults, detrending, period detection, transit characterization, and false-positive scoring.

Evidence: `supreme_telescope_converter.py` (2 copies). Rule: decompose into independently
testable operators; never port monolithically (WP-3).

## ANTI-05 — synthetic draws presented via NASA ranges

> Generated training distributions are presented using NASA parameter ranges but are still synthetic draws.

Evidence: `nasa_catalog_data_generator` (2 hits). Rule: teacher/synthetic provenance is never
relabeled observational (Sec-15.1, Sec-30); source classes enforced by Dataset Factory (WP-1/WP-4).

## ANTI-06 — historical adversarial ideas worth preserving

> Several stress suites and false-positive fixture families are valuable as historical adversarial ideas.

Evidence: `brutal_reality_test/` (20 entries, 16 adversarial CSVs), `clean_ultimate_test/`
(13 entries). Rule: import under `LEGACY_HISTORICAL` only; never fresh holdout evidence
(Sec-40); indexed in `FIXTURE_SAMPLE_INDEX.json`.

## ANTI-07 — caches, checkpoints, deps, datasets tracked together

> The repository tracks generated caches, binary checkpoints, frontend dependencies, and datasets together.

Evidence: `.vite/`, `__pycache__/`, `.h5`/`.pkl` binaries, frontend + datasets in one tree.
Rule: clean-room layout per Sec-65; `.gitignore` excludes binaries/caches/runs; manifests +
hashes committed, bulky bytes outside ordinary git (WP-0 hygiene; WP0-T04 enforces).
