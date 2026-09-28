# Legacy archaeology — Council of Lords (historical implementation)

**Role:** archaeological reference only. Not a validated scientific parent, not a benchmark
authority, not a source of grandfathered model qualification (IMPLEMENTATION_SPEC.md Sec-0, Sec-3.2).

## Source pin

- Remote: `https://github.com/InfernusReal/Council-Of-Lords`, HEAD `72222ad289616046e87e79ac4876c7f47fe40c0b`.
- Local snapshot: `Council-Of-Lords-main.zip`, SHA256 `cf524060012b72aa84a6543038372133eb00ecb3817d91c34e43601138c49695`, 57710 bytes (77 MB), 5771 zip entries.
- Full entry listing with CRCs: `LEGACY_FILE_MANIFEST.json` (same directory).
- Fixture sample index (hashes only, no binaries): `FIXTURE_SAMPLE_INDEX.json` (127 entries, all `LEGACY_HISTORICAL`).

## Layout (top level)

`COUNCIL_OF_LORDS_NASA_NATIVE/`, `backend/`, `frontend/`, `brutal_reality_test/`,
`clean_ultimate_test/`, `README.md` (88 README hits across tree), `instructions-for-use.md`,
`node_modules`-style frontend deps (`.vite/`), `__pycache__/`. Generated caches, binary
checkpoints, frontend dependencies, and datasets are tracked together (see anti-pattern ledger).

## Training scripts (6 `*_train.py`, all under `COUNCIL_OF_LORDS_NASA_NATIVE/`)

`atmospheric_warrior_nasa_train.py`, `backyard_genius_nasa_train.py`,
`celestial_oracle_nasa_train.py`, `chaos_master_nasa_train.py`,
`cosmic_conductor_nasa_train.py`, `supreme_ensemble_nasa_train.py`.
Named specialists are parallel neural classifiers over the same catalogue-style inputs;
specialties are encoded via altered losses, widths, thresholds, or class weights.

## Ensemble logic

`supreme_ensemble_nasa_train.py`, `smart_ensemble_fix.py`, `test_nasa_native_ensemble.py`.
Applies hard-coded specialist weights and context-specific boosts/penalties
(e.g. fixed per-specialist multipliers). Forbidden as a scientific decision rule in v1.0
(Sec-25); preserved here as evidence of the historical pattern.

## Converter

`supreme_telescope_converter.py` (two copies: `COUNCIL_OF_LORDS_NASA_NATIVE/` and `backend/`).
Bundles catalog lookup, defaults, detrending, period detection, transit characterization,
and false-positive scoring in one monolith. Must NOT be ported monolithically (WP-3
decomposes it into independently testable operators; mapping recorded there).

## Fixture inventory

- `brutal_reality_test/`: 20 entries incl. 16 adversarial CSVs (`ground_hell`, `heartbreak_binary`,
  `instrumental_demon`, `kepler_disaster`, `stellar_demon`, `tess_nightmare`,
  `tiny_earth_analog`, `ultra_contact_binary`, each in two tree locations).
- `clean_ultimate_test/`: 13 entries.
- `nasa_catalog_data_generator` (2 hits): synthetic draws presented via NASA parameter ranges.
- Model binaries (`.h5` checkpoints, `.pkl` scalers under `COUNCIL_OF_LORDS_NASA_NATIVE/`):
  listed in `LEGACY_FILE_MANIFEST.json`, REJECTED from `FIXTURE_SAMPLE_INDEX.json` by the
  binary gate. Old checkpoints/scalers are never qualified preprocessing or models.

## Import policy (COL-T18 control)

Historical models may be wrapped as `LEGACY_UNQUALIFIED` for side-by-side regression only.
They may never enter a PC closure policy as qualified evidence producers unless
retrained/requalified through Forge. Enforcement: `scripts/migrate_legacy_fixtures.py --check`
fails on any unlabeled, fresh-labeled, or binary fixture entry (WP0-T01).

## Atomicity note (COL-T30 control)

No atomicity boundary is frozen here. The freeze commitment in
`configs/pc/atomicity_freeze_commitment_v1.json` records that the normative
`ACTION_SCHEMA.json`/`ATOMICITY_SCHEMA.json` are frozen in WP-2; any later movement
requires a successor version per Sec-64.
