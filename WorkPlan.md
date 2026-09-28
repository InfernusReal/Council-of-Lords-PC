# WorkPlan — COUNCIL-PC-v1.0 (COL-PC-v1.0)

**Experiment:** `COUNCIL-PC-v1.0` / `COL-PC-v1.0`
**Implementation repo:** `InfernusReal/Council-of-Lords-PC`
**Operative spec:** `IMPLEMENTATION_SPEC.md` (revised, OpenCode provider + Sec-15.6 exhaustive source-acquisition doctrine), SHA256 `9d4761e3cb656b0b4295a5ae4efcf08bc13058f00082577d5b92d406de1482e6`, 2983 lines, Sec-0..68 (69 numbered sections)
**Original spec SHA256:** `a9453d20079ace95d8227d0fed095398b4aa6de1d1265f61ba6fe1b4c5dbf0fb` (preserved at `audits/COUNCIL-PC-v1.0_IMPLEMENTATION_SPEC_ORIGINAL.md`)
**Provider migration audit:** `audits/PROVIDER_MIGRATION_AUDIT.md` — PASS, 3 literal lines OpenRouter->OpenCode
**Conceptual parent (read-only):** `PERCEPTIVE CLOSURE: IDENTIFYING AUTHORIZATION-RESOURCE COUNTERFACTUALS` (local `Perception Closure` folder + Downloads drafts; exact paper version pinned in WP-0)
**Legacy parent (archaeological reference only):** `InfernusReal/Council-Of-Lords` + `Downloads/Council-Of-Lords-main.zip` (5771 entries) — NOT a benchmark authority, NOT a qualification source
**Teacher:** Muse Spark 1.3 Contributor through OpenCode, USD 25 default ceiling, schema-bound, provenance-recorded, never ground truth
**Normative inventory:** `planning/NORMATIVE_INVENTORY.yaml` — 561 items canonical (see counts below)
**Coverage map:** `planning/WORKPLAN_COVERAGE.yaml` + `scripts/check_workplan_coverage.py` must print `RESULT = WORKPLAN_COVERAGE_PASS`
**Terminal goal:** `PC_NATIVE_COUNCIL_QUALIFIED` (satisfies own frozen contract; NOT exoplanet confirmation)
**Doctrine (corrected):** Training optimizes specialists; qualification earns registry eligibility; authority licenses their use.
Qualification (WP-6) establishes registry eligibility only. Runtime Lambda (WP-7) controls whether a qualified
specialist may be used. No WorkPlan text treats qualification as runtime authorization.

## SPEC_CONFLICT-01 (process header vs operative spec)

The generic process header supplied with this task names `SPLAY-AM-MST-LIQ-v0.4` / `MST-LIQ-v0.4`
(`audits/SPLAY-AM-MST-LIQ-v0.4_SPEC.txt`, 1740 lines, SHA256 `0E2C166E1B721DFC8A7E5327ED33AF29A1B4AC539CB71849F3C7231B32A8055B`)
with `LIQ0-*`, `MST0-*`, `MSTC-0002=(P,k,C,rho)`, liquidity gates and candidate-freeze semantics.
That experiment is **not** the operative science for this repo. The operative repo (`Council-of-Lords-PC`),
operative spec (COUNCIL-PC-v1.0, 69 sections), and remote HEAD all identify Council.
Per Rule 14 the conflict is preserved, not guessed away:

- `MST-LIQ0-NA`, `MST-MST0-NA`, `MST-CAND-NA`, `MST-FRESHBANK-NA`, `MST-AXIS-NA` are recorded in the
  inventory with `status: not_applicable` and source `SPEC_CONFLICT-01`.
- Council analogues govern instead: `HOLD-*` (holdout/firewall), `Q-*` + `LPC-*`/`CPC-*` (lifecycle),
  `PC-*` (closure/touch/freeze theorems), Sec-64 (successor rule).
- SPLAY Rules 4–10 (rho embedding, legacy T5/T6/T7, stock/liquidity split, theorem transport ladder to
  Dynamic Optimality) do **not** execute in this repo. Council Rules are Sec-0..68.
- Planning discipline Rules 0–3, 11–17 (inventory, coverage, WorkPlan compilation, hygiene, Path ledger,
  self-audit, order, commit/push) **do** apply and are implemented below.

## Normative counts (derived from IMPLEMENTATION_SPEC.md, not memory)

```text
SEC 69 | PHASE 31 (00-30) | WP 9 (WP-0..WP-8) | GATE 23 (COL-GATE-00..22)
THREAT 30 (COL-T01..30) | STOP 25 (COL-STOP-01..25) | TEST 14 | SCHEMA 17
TERM 10 | ART 19 | LABEL 9 | DCLASS 9 | LCONF 7 | MUT 21 | ADV 20 | PCQ 8
DIAG 15 | ACT 25 | LORD 6 | CLI 18 | AUDQ 15 | LPC 16 | CPC 10
PC_OBLIG 20 | WIT 12 | Q 7 | HOLD 8 | TEACH 8 | CLAIM 14 | HYG 5 | REPRO 3
SECRET 2 | SUCC 2 | ANTI 7 | SRC_DOCTRINE 2 | SRC_FAM 17 | SRC_FIELD 14
SRC_STATUS 4 | SRC_REGISTRY 1 | SRC_ATTEMPT 1 | MST_NA 5 + SPEC_CONFLICT 1
INVENTORY_ITEMS_TOTAL = 561
NORMATIVE_ITEMS_TOTAL = 556
NOT_APPLICABLE_ITEMS_TOTAL = 5
```

## WP structure

Nine WPs, exactly as Sec-46 requires. No 5–6 WP compression (would mix accountability across
atomic gates HOLD-02 one-reveal, GATE-05 independent touch, GATE-13 holdout reveal, GATE-15 registry seal).
No extra WPs (API/frontend are phases inside WP-8 per Sec-47, omissible without blocking the terminal gate).
Phase ownership is exactly-one-WP (see each WP §A and the coverage checker assertion 3).

Global commit/push rule (every WP §K): `VERIFY -> UPDATE Path.md -> COMPLIANCE AUDIT -> COMMIT -> PUSH -> VERIFY REMOTE HEAD`.
Record full SHA + push result in `Path.md`. Do not ask the user. Commit messages identify experiment+WP+phase/gate+artifact.

---

## WP-0 — Foundation freeze and archaeology (Sec-46 WP-0)

### A. Normative coverage
- Sec: SEC-00, SEC-01, SEC-02 (non-goals as constraints), SEC-03 (parents/roles), SEC-49, SEC-50, SEC-65 (layout pin), plus process COMMIT-01, HYG-01..05, ANTI-01..07, AUDIT-LEGACY-01, SPEC-CONFLICT-01.
- PHASEs owned: PHASE-00 (pin legacy+PC parent+spec), PHASE-01 (archaeology + anti-pattern ledger). No other WP owns these.
- PC obligations owned: none as producer (pins PC paper version only); consumes PC concepts as frozen references.
- Gates owned: COL-GATE-00 FOUNDATION_FROZEN (producer), COL-GATE-01 LEGACY_ARCHAEOLOGY_COMPLETE (producer).
- Threats exercised: COL-T18 (legacy promotion without requalification — control: LEGACY_UNQUALIFIED wrap), COL-T30 (atomicity moved after freeze — control: freeze atomicity schema v1 here).
- Stops handled: COL-STOP-01 (PC contract cannot be pinned -> BLOCKED), COL-STOP-02 (legacy snapshot cannot be pinned -> BLOCKED).
- Tests owned: legacy regression tests (scaffolding + fixture import policy; full suite runs in WP-8).
- Invariants: legacy never qualified; history never deleted, only quarantined/labeled.

### B. Entry conditions
- Prerequisite: none (first WP). Requires operative spec bytes present (`IMPLEMENTATION_SPEC.md` SHA above),
  original + migration audit in `audits/`, SPLAY template preserved in `audits/` with SPEC-CONFLICT-01 recorded,
  remote `origin/main` reachable (initial commit `3880b80` observed). No firewall/HOLD state yet. No model training.

### C. Scientific scope
- Resolves: what exactly is inherited (paper version, legacy commit/tree, spec version, threat matrix, target ontology D, environment) and what is archaeological only.
- MUST NOT claim: any legacy weight/threshold/fixture is qualified; any benchmark authority; any PC semantics beyond pinning.

### D. Exact files to create or modify
- Inherited read-only (never edit): upstream legacy zip/tree listing, PC paper PDF(s) reference.
- New (this WP): `FOUNDATION_MANIFEST.json`, `audits/legacy/LEGACY_ARCHAEOLOGY.md`, `audits/legacy/LEGACY_FILE_MANIFEST.json`,
  `audits/legacy/ANTI_PATTERN_LEDGER.md`, `PC_PARENT_MANIFEST.json`, `configs/pc/target_ontology_v1.json`,
  `ENVIRONMENT_BASELINE.json`, `.gitignore` (large-artifact hygiene), `.env.example` (names only), `pyproject.toml` skeleton (name/version/deps per Sec-53),
  `planning/` inventory+coverage (this plan), `Path.md` skeleton, `WorkPlan.md` (this file).
- Vendored/hash-bound: legacy fixture sample index (hashes only, no large binaries committed).
- Schemas: none frozen here except target ontology + manifest schemas (draft, frozen in WP-2/WP-3).

### E. Code to be implemented
- `scripts/pin_foundation.py`: responsibility — hash operative spec/audits, list legacy zip (5771 entries via zipfile namelist, no full expand), record PC paper filename+hash, emit manifests. Inputs: local spec/audit paths + legacy zip path. Outputs: JSON manifests with sha256, line counts, entry counts. Ordering: deterministic sorted keys, UTF-8. Failure: any missing source -> `SPEC_CONFLICT`/BLOCKED record, nonzero exit. Independent impl: manifest re-computed by `scripts/final_audit.py` in WP-8 must match. Complexity: O(zip entries).
- `scripts/migrate_legacy_fixtures.py` (skeleton here, full in WP-1/WP-8): lists candidate fixtures, assigns `LEGACY_HISTORICAL`, rejects binaries > threshold from git.
- No ML, no teacher calls in this WP.

### F. Mathematical obligations
- No theorems proved. Obligations: fix identities — target classes D={PLANETARY_CANDIDATE,ASTROPHYSICAL_FP,INSTRUMENTAL_SYSTEMATIC,UNRESOLVED} (PC-TARGET ref), legacy pipeline formula (Sec-0) as historical description, central law (never manually tag E/R/A) as design constraint. Finite testing never a premise.

### G. Benchmarks and anti-overfitting
- No statistical model trained (state explicitly: NO MODEL TRAINED in WP-0). Legacy fixtures labeled LEGACY_HISTORICAL/CONTAMINATED_DEVELOPMENT from birth. No holdout exists yet. Leakage control: legacy data never enters `data/` as observational.

### H. Verification
- `python scripts/gen_normative_inventory.py` reproduces inventory (561 items, 556 normative + 5 not_applicable).
- `python scripts/check_workplan_coverage.py` prints PASS (run after all planning files exist).
- `python scripts/pin_foundation.py --check` re-hashes manifests.
- `git status --short` shows only intended files; no `.env`, no binaries, no `__pycache__`.
- Schema: manifests validate against inline JSON schema (keys present, hashes 64-hex).

### I. Exit gate
- Success: COL-GATE-00 + COL-GATE-01 emit `FOUNDATION_FROZEN`, `LEGACY_ARCHAEOLOGY_COMPLETE` with manifest hashes recorded in Path.md.
- Failure: any pin missing -> GATE FAIL, downstream WPs BLOCKED (NOT_REACHED), no silent continuation.

### J. Failure behavior
- STOP-01/02 -> project `PC_SEMANTICS_UNDERIDENTIFIED` or `DATASET_INTEGRITY_FAILED` terminal candidate; WPs 1–8 NOT_REACHED; history preserved.

### K. Commit/push rule
- VERIFY (H) -> UPDATE Path.md (WP-0 actuals) -> COMPLIANCE AUDIT (coverage checker PASS) -> COMMIT `COL-PC-v1.0 WP-0 foundation+archaeology (GATE-00/01)` -> PUSH -> VERIFY `git ls-remote origin main` == local HEAD. Record SHA in Path.md.

---

## WP-1 — Trusted data core (Sec-46 WP-1)

### A. Normative coverage
- Sec: SEC-06 (partial: quality/preprocessing provenance), SEC-15 incl. Sec-15.6 exhaustive source-acquisition doctrine (Dataset Factory classes/splits/mission/labels/identity + frozen source registry + acquisition closure), SEC-16 (raw preservation/transform ledger), SEC-53 (deps), SEC-65 (data layout).
- PHASEs owned: PHASE-02 (LightCurve type + provenance core), PHASE-03 (preprocessing primitives), PHASE-04 (Dataset Factory foundation + frozen public-source registry + exhaustive source acquisition + source-status ledger + identity reconciliation + acquisition closure audit). Exactly one owner each; PHASE-04 stays with WP-1 (no dependency contradiction: later phases consume the registry, they do not produce it).
- Gates owned: COL-GATE-02 DATA_CORE_CERTIFIED (producer) + COL-GATE-22 DATASET_SOURCE_COVERAGE_CLOSED (producer of the closure artifact; WP-8 re-verifies it at release). GATE-03 produced by WP-4 (full factory cert); WP-1 is prerequisite skeleton.
- Source IDs owned: COL-SRC-DOCTRINE, COL-SRC-ATTEMPT, COL-SRC-FAM-01..17, COL-SRC-FIELD-01..14, COL-SRC-STATUS-01..04, COL-SRC-REGISTRY, COL-SRC-NOSILENT (all producer WP-1).
- Doctrine intent: `Acquire broadly, provenance everything, train selectively, test brutally.` WP-1 builds the acquisition framework + source registry + status-closure mechanism; later actual large data materialization may proceed under the frozen registry without re-scoping (bulky bytes outside ordinary git; manifests + hashes committed).
- Threats controlled: COL-T01 (identity leakage — control: object-level grouping test), COL-T02 (sector/window leakage — control: group-constrained split), COL-T03 (catalog target leakage — control: source-manifest + forbidden-evidence declaration), COL-T10 (scratch vs H — control: admission-only API), COL-T17 (synthetic/observational merge — control: registry source_family + entry schema tags), COL-T19 (fallback as observation — control: DECLARED_DEFAULT schema), COL-T20 (artifact not bound to manifest — control: hash-bound manifests + registry raw_hashes).
- Stops: COL-STOP-04 (H change after freeze -> blocked via schema versioning; this WP freezes H-adjacent data types, H itself frozen in WP-2).
- Tests: unit, property, schema, provenance, leakage (skeleton suites) + source-registry schema tests + acquisition-closure audit test (every registry entry terminal, none silent).
- Schemas produced: LightCurveSchema v1 (producer), DatasetManifestSchema/Split/Transform/Checksum/Leakage drafts (finalized WP-4), SourceRegistryEntrySchema v1 (producer: 14 fields per Sec-15.6).

### B. Entry conditions
- COL-GATE-00 + COL-GATE-01 PASSED with manifest hashes in Path.md. `FOUNDATION_MANIFEST.json` hash matches. No teacher holdout yet. Branch `main` clean.

### C. Scientific scope
- Resolves: can raw light curves be ingested with byte/unit/provenance preservation, deterministic preprocessing, and leakage-free object grouping?
- MUST NOT claim: catalogue semantics (WP-3), PC closure (WP-2), model qualification (WP-6).

### D. Exact files
- New source: `src/council/data/lightcurve.py`, `src/council/data/provenance.py`, `src/council/data/quality.py`, `src/council/data/catalogs.py` (stubs with provenance only, no target-leaking joins), `src/council/preprocessing/normalization.py`, `src/council/preprocessing/detrending.py`, `src/council/preprocessing/windows.py`, `forge/datasets/factory.py`, `forge/datasets/splits.py`, `forge/datasets/manifests.py`, `forge/datasets/source_registry.py` (frozen registry builder + status ledger + identity reconciliation + closure audit), `src/council/cli/` verbs `col data ingest/build/audit` (skeleton).
- Schemas: `configs/schemas/LightCurveSchema_v1.json`, `configs/schemas/DatasetManifestSchema_v1.json` (draft), `configs/schemas/SourceRegistryEntrySchema_v1.json` (14 fields).
- Registry + closure artifacts: `data/manifests/SOURCE_REGISTRY_v1.json` (frozen; 17 families minimum attempted), `data/manifests/SOURCE_STATUS_LEDGER.json` (exactly one terminal state per entry: INGESTED / INCOMPATIBLE_WITH_DOCUMENTED_REASON / UNAVAILABLE_WITH_ARCHIVED_FAILURE / EXCLUDED_BY_FROZEN_POLICY), `audits/WP1_SOURCE_CLOSURE.json` (COL-GATE-22 evidence).
- Tests: `tests/unit/test_lightcurve.py`, `tests/property/test_transform_determinism.py`, `tests/forge/test_object_grouping.py`, `tests/unit/test_no_silent_defaults.py`, `tests/forge/test_source_registry.py` (schema + terminal-state + no-silent-omission).
- Reports: `audits/leakage/WP1_LEAKAGE_REPORT.md` (empty-population template + grouping proof on fixtures).
- Inherited read-only: legacy raw samples index only.

### E. Code details
- `LightCurve`: fields time/flux/flux_err/quality/mission/target/sector/cadence/time_system/flux_definition/units + `raw_hash` (sha256 of ingested bytes) + `source_manifest_ref`. Representation: float64 time (BJD), float32 flux normalized lazily, int32 quality bitmask; NaN only via finite_mask, never silent interpolation. Deterministic ordering: sort by time, stable. Failure: unknown units -> error, not default. Complexity O(n log n) sort.
- `quality.py`: finite_mask/outlier_mask/gap_summary/contamination_flags as pure functions with seeded RNG only where declared; masks versioned.
- `normalization.py`/`detrending.py`: variants as named pure ops (`MEDIAN_DIVIDE`, `SPLINE_v1` with explicit knots/penalty) recording producer/version/params/input_hash/output_hash/seed/mask/units. No fitting to hidden labels.
- `splits.py`: GroupBy protected identity (target_id / TIC/KIC) — all windows/sectors/augmentations of one group in same split; mission strata recorded; `leakage_report.json` asserts zero cross-split identity overlap (independent recheck in WP-4/WP-6).
- `source_registry.py`: builds the frozen registry from the 17 required families + eligible public sources attempted (Kepler DR25/KOIs/TCEs/Certified FPs/Robovetter/injection-recovery/inverted/scrambled/EB catalogs/light curves; K2 populations; TESS TOIs/TCE-DV/light curves/EB sources; MAST; NASA Exoplanet Archive; Gaia; quality/systematics metadata; physical adversarial; Muse-proposed deterministic materializations) with NO fabricated URLs/counts/versions/availability; each entry carries the 14-field schema; identity reconciliation maps raw object identities to protected split identities; closure audit asserts every entry terminal exactly once; any non-terminal entry fails the gate. Framework + registry + closure mechanism ship in WP-1; bulky materialization may follow under the frozen registry.
- CLI `col data ingest/build/audit`: deterministic, JSON to stdout + manifest to `data/manifests/`.

### F. Mathematical obligations
- No theorems. Obligation: prove-by-construction that grouping is exact (test asserts `groups(train) ∩ groups(test) = ∅`) and transforms are hash-chained. Finite fixture survival is not a correctness proof for unseen missions.

### G. Benchmarks/anti-overfitting
- No ML model trained (state explicitly). Development fixtures only (synthetic/legacy-labeled). No validation/test split consumed as training. Seeds recorded where RNG used. No holdout exists; nothing labeled fresh.

### H. Verification
- `pytest tests/unit tests/forge -q`, `python -m council.cli data audit --manifest data/manifests/<id>.json`, `python scripts/check_workplan_coverage.py`, hash check `sha256sum data/manifests/*`.
- Mutation spot-check: scratch-field-admission mutant must fail (admission API rejects non-admitted fields).
- Source-closure check: every `SOURCE_REGISTRY_v1.json` entry has exactly one terminal state; `audits/WP1_SOURCE_CLOSURE.json` verifies; non-terminal or missing entry fails COL-GATE-22.

### I. Exit gate
- Success: COL-GATE-02 `DATA_CORE_CERTIFIED` (raw preserved, units preserved, no silent defaults, grouping exact, deterministic transforms, hashed) + COL-GATE-22 `DATASET_SOURCE_COVERAGE_CLOSED` (frozen registry attempted exhaustively; every entry terminal with ledger + reconciliation + audit frozen and hash-bound; coverage closure, not "all downloaded").
- Failure: GATE FAIL -> WP-2..WP-8 BLOCKED for data-dependent paths; WP-0 stands.

### J. Failure behavior
- Leakage detected -> COL-STOP-10 handler: freeze splits, quarantine dataset version, mark downstream NOT_REACHED until new dataset major version.

### K. Commit/push rule — as global; message `COL-PC-v1.0 WP-1 data-core (PHASE-02/03/04, GATE-02/22)`.

---

## WP-2 — PC semantic core (Sec-46 WP-2)

### A. Normative coverage
- Sec: SEC-04, SEC-05, SEC-08, SEC-09, SEC-33 (controller legality ref), SEC-34, SEC-35, SEC-37, SEC-38.
- PHASEs owned: PHASE-05 (H/P_R/Lambda/omega/A types), PHASE-06 (action/atomicity/touch/closure), PHASE-07 (exact freeze planner + finite sanity fixtures). Exactly one owner each.
- PC obligations produced: PC-H, PC-PR, PC-LAMBDA, PC-OMEGA, PC-TARGET, PC-COMPAT, PC-CLOSURE, PC-ADMIT, PC-TOUCH, PC-ATOM, PC-SUCC, PC-COST, PC-KAPPA, PC-IDENT, PC-INDTOUCH (all producer WP-2; consumers WP-3..WP-8).
- Gates owned: COL-GATE-04 PC_CORE_CERTIFIED, COL-GATE-05 TOUCH_DERIVATION_INDEPENDENT_AGREEMENT (both producer).
- Witnesses owned: WIT-01..12 (all producer).
- Threats: COL-T08 (manual touch — control: derived-only + recompute-reject), COL-T09 (underidentified as identified — control: BOUNDARY_UNDERIDENTIFIED path), COL-T11 (score vs P_R — control: type separation), COL-T12 (availability outside Lambda — control: Lambda-gated action set), COL-T13 (split mixed action — control: atomic freeze masks), COL-T15 (confidence as closure — control: closure predicate test), COL-T29 (hidden authority side channel — control: Lambda reflection test), COL-T30 (atomicity moved — control: ATOMICITY_SCHEMA hash).
- Stops: COL-STOP-04/05/06/07/08/17 (H/P_R/Lambda/atomicity/touch/manual-label freezes).
- Tests: PC semantic, touch derivation, freeze tests (producer).

### B. Entry conditions
- COL-GATE-02 PASSED. `LightCurveSchema_v1` hash pinned. `ACTION_SCHEMA` draft + `ATOMICITY_SCHEMA` draft hashes recorded. No candidate freeze yet. Controller code from WP-7 not yet present (planner here is controlled exact planner for finite PC experiments only).

### C. Scientific scope
- Resolves: are H/P_R/Lambda/Atom/Succ+/touch/closure/freeze mathematically pinned enough to make resource counterfactuals identified and touch independently recomputable?
- MUST NOT claim: catalogue correctness, model quality, astronomical prevalence, cost optimality beyond controlled instances.

### D. Exact files
- New: `src/council/pc/contract.py` (PC_CONTRACT.json emitter), `state.py` (H,P_R,Lambda,omega,C,M + checkpoint IDs/hashes), `closure.py` (C_R + closed predicate), `touch.py` (primary derivation), `touch_independent.py` (separately implemented equality over canonical serialization), `freeze.py` (8-mask planner + kappa/K computation), `authority.py`, `representation.py` (relation handles; engine in WP-3), `atomicity.py`, `configs/pc/target_v1.json` (D + UNRESOLVED policy), `configs/pc/cost_convention_v1.json` (unit costs + real-cost tracking fields), `ACTION_SCHEMA.json`, `ATOMICITY_SCHEMA.json`, `PC_CONTRACT.json`.
- Tests: `tests/pc/test_closure.py`, `test_touch_derivation.py`, `test_independent_touch_agreement.py`, `test_freeze_masks.py`, `test_identification_gate.py`, fixtures for WIT-01..12 (pure E/R/A, ER/EA/RA/ERA, open/closed, R-fallback, R-structural-failure, underidentified).
- CLI: `col pc touch/close/freeze` (exact, deterministic).

### E. Code details
- `state.py`: immutable dataclasses (frozen), `state_hash = sha256(canonical_json)`; H as typed append-only log with parent_state_id chain; P_R as partition handle (equivalence relation over history hashes, not raw floats); Lambda as capability bitset reflected in `omega.action_set`; C as explicit finite set or exact surrogate with `surrogate_kind` tag (no silent approximation).
- `touch.py` (primary): compares pre/post semantic objects (H,P_R,Lambda hashes); emits subset of {E,R,A}. `touch_independent.py`: re-derives from canonical serialization with separately written equality (different code path, no shared helper). Disagreement -> error, blocks GATE-05.
- `freeze.py`: for F in [EMPTY,E,R,A,ER,EA,RA,ERA] removes actions with touch∩F≠∅ (whole action, never partial), computes kappa as infmax path cost on finite instance via exhaustive search with deterministic tie-break (sorted action IDs); K tuple in fixed coordinate order. Real costs tracked separately, never mixed into unit-cost claim.
- `closure.py`: `closed(s) := |{A(x): x in C_R(s)}|==1`; open states cannot emit closed verdict (type-level enforcement + test).
- Numerics: hashes hex; costs nonnegative float64, unit costs integers 0/1 for controlled runs; no threshold magic.

### F. Mathematical obligations
- For each PC-*: statement source (Sec-N), domain (finite controlled instances for executable checks; abstract sets for definitions), prerequisites (frozen schemas), strategy (construction + property tests + independent recomputation), Layer A artifact (JSON fixtures + traces), Layer B (deterministic checker code, not full Lean — Lean out of scope for v1.0; state explicitly), Layer C (mutants + underidentified fixture must be refused, not guessed), human-review gate (PC contract review recorded in Path.md; ACCEPT applies only to exact bytes), downstream consumers (WP-3 representation, WP-7 controller, WP-8 freeze geometry). Finite survival never a proof premise.

### G. Benchmarks/anti-overfitting
- No ML trained. Finite fixtures are development/FORMAL_PC_CONSTRUCTED, never FRESH. No holdout. No hyperparameter search. Deterministic, seed-free (or fixed seed recorded).

### H. Verification
- `pytest tests/pc -q`, `col pc touch --pre ... --post ...`, `col pc freeze --instance ...` + independent recompute agreement, `python scripts/check_workplan_coverage.py`, `python scripts/check_lifecycle.py` (stub; full in WP-6), hash-verify schemas.

### I. Exit gate
- Success: GATE-04 (all WIT fixtures pass, open/closed correct, R-fallback vs structural-failure distinguished, underidentified refused) + GATE-05 (primary==independent on all fixtures).
- Failure: STOP-08 (touch disagreement) or STOP-04/05/06/07 -> PC_SEMANTICS_UNDERIDENTIFIED; downstream WP-3..WP-8 BLOCKED.

### J. Failure behavior
- Touch disagreement / identification failure -> REFUTED planner output, BLOCKED consumers, no retroactive justification from later WPs.

### K. Commit/push rule — message `COL-PC-v1.0 WP-2 pc-core (PHASE-05/06/07, GATE-04/05)`.

---

## WP-3 — Catalogue and diagnostic reconstruction (Sec-46 WP-3)

### A. Normative coverage
- Sec: SEC-06 (EvidenceState full schema + admission + no-fallback), SEC-07 (P_R refinement examples), SEC-10 (action vocab wiring for catalogue/diagnostic actions), SEC-39 (diagnostic library).
- PHASEs owned: PHASE-08 (catalogue schema + state builder), PHASE-09 (period/transit/noise primitives), PHASE-10 (representation refinement engine). Exactly one owner each.
- Gates owned: COL-GATE-06 CATALOGUE_ENGINE_CERTIFIED, COL-GATE-07 REPRESENTATION_ENGINE_CERTIFIED.
- PC obligations consumed: PC-H/ADMIT/NOFALLBACK (producer of EvidenceState impl), PC-PR (producer of refinement engine), PC-TOUCH (emits R-touching actions), PC-VIEWS (view constructors for PRE/POST refinement).
- Diagnostics owned: DIAG-01..15 (producer v1 where data permits; each with input requirements/algorithm/output/uncertainty/rep-effect/boundary/provenance).
- Actions wired: ACT-01..15 catalogue/diagnostic subset + ACT-22 REFINE_REPRESENTATION (producer wiring; controller execution in WP-7).
- Threats: COL-T10 (scratch vs H), COL-T11 (score vs P_R), COL-T19 (fallback), COL-T24 (LLM numerals without validation — control: deterministic validators).
- Tests: schema, provenance, PC semantic (representation), touch (R) — producer.

### B. Entry conditions
- GATE-04 + GATE-05 PASSED; PC contract/ATOMICITY hashes pinned. DATA_CORE (GATE-02) available. No candidate freeze. Diagnostics may not consume hidden labels.

### C. Scientific scope
- Resolves: can the monolithic `SupremeTelescopeConverter` be decomposed into independently testable operators that emit versioned EvidenceState + diagnostics with representation effects, without scalar-penalty semantics?
- MUST NOT claim: model performance, closure, qualification.

### D. Exact files
- New: `src/council/evidence/schema.py` (EvidenceStateSchema v1), `state_builder.py` (H_0..H_t builder, hash chain), `admission.py` (only legal admission actions mutate H), `views.py` (PRE/POST views), `src/council/detection/period_search.py` (BLS + alternate), `transit_search.py`, `morphology.py`, `odd_even.py`, `secondary.py`, `systematics.py`, `src/council/preprocessing/*` extensions, `src/council/pc/representation.py` (refinement rules mapping diagnostic outputs -> P_R partitions), configs `configs/schemas/EvidenceStateSchema_v1.json`, `RepresentationSchema_v1.json`.
- Decompose legacy converter: each legacy function mapped in `audits/legacy/CONVERTER_DECOMPOSITION.md` (no monolithic port).
- Tests: `tests/unit/test_evidence_schema.py`, `test_admission_only.py`, `test_no_silent_fallback.py`, `test_diagnostics_deterministic.py`, `tests/pc/test_representation_touch.py`.
- First outputs (required): period candidates, transit summary, noise summary, odd/even, secondary, stellar context, contamination where available, provenance for all fields.

### E. Code details
- `EvidenceState`: typed nested object per Sec-6 schema (identity/observation/quality/preprocessing/periodicity/transit/stellar/spatial/noise/specialist_observations/provenance); `state_hash` over canonical JSON; parent chain; per-field source/transform/producer_version/time/hash. `admission.py` exposes `admit(state, action, payload) -> new_state` only for declared actions; direct field assignment outside admission raises. Fallback: `value+fallback=true+reason+uncertainty+source=DECLARED_DEFAULT`, distinguishable; stellar fallbacks never equal measured values in equality logic.
- Detectors: BLS (deterministic grid, sorted periods, explicit alias graph + harmonics + uncertainty), odd/even (depth difference + p-value with fixed seed), secondary (phase-fold significance + noise floor), morphology stats (depth/duration/ingress/egress/shape), noise (robust scatter/red-noise/local SNR/variability). All pure, versioned, units explicit.
- `representation.py`: diagnostic -> partition refinement rules (e.g., odd/even inequality splits certificate class; P vs 2P alias splits; secondary present splits). Rule outputs new P_R handle + touch R; no scalar `advanced_score` mutation.
- Ordering: builder applies actions in ledger order; CLI replays ledger deterministically.

### F. Mathematical obligations
- PC-H/PC-PR instantiations: show admission-only mutation (test: scratch field without admission absent from H hash) and R-touch correctness (test: flag change without P_R change emits no R). Finite diagnostics are evidence, not proofs of astrophysical correctness.

### G. Benchmarks/anti-overfitting
- No ML trained. Diagnostics tuned only on DEVELOPMENT/LEGACY_HISTORICAL; thresholds recorded; no holdout access. Mutation: score-as-P_R mutant must be killed.

### H. Verification
- `pytest tests/unit tests/pc -q`, `col data audit`, evidence hash-chain verify, `check_workplan_coverage.py`, independent touch recheck on REFINE actions.

### I. Exit gate
- Success: GATE-06 (all required first outputs present with provenance, no silent defaults, decomposed operators) + GATE-07 (each diagnostic has declared rep-effect + boundary; R-touch correct).
- Failure: fallback/score confusion -> GATE FAIL, WP-4 views BLOCKED until fixed in new schema version.

### J. Failure behavior
- Schema change required -> new schema major version + re-run WP-1/WP-2 affected checks; downstream NOT_REACHED until re-certified.

### K. Commit/push rule — message `COL-PC-v1.0 WP-3 catalogue-diagnostics (PHASE-08/09/10, GATE-06/07)`.

---

## WP-4 — COL Forge (Sec-46 WP-4; train dev candidates only, no promotion)

### A. Normative coverage
- Sec: SEC-11 (specialist principle), SEC-13 (hardware/size contract), SEC-14 (Forge pipeline), SEC-15 (remainder: manifests/label policy), SEC-17 (Task Factory + required fields), SEC-18 (SpecialistSpec), SEC-19 (training engine + run manifests), SEC-20 (search ordering), SEC-21 (calibration), SEC-22 (abstention), SEC-23 (qualification components as harness, not verdict), SEC-24 (capability map builder), SEC-28 (resource views), SEC-60 (baselines).
- PHASEs owned: PHASE-11 (Task Factory + SpecialistSpec), PHASE-12 (classical adapters), PHASE-13 (PyTorch compact trainer), PHASE-14 (calibration+abstention+OOD interfaces), PHASE-15 (qualification harness). Exactly one owner each.
- Gates owned: COL-GATE-03 DATASET_FACTORY_CERTIFIED (full factory; prerequisite WP-1 skeleton), COL-GATE-08 FORGE_OPERATIONAL, COL-GATE-09 CALIBRATION_PIPELINE_CERTIFIED, COL-GATE-10 QUALIFICATION_HARNESS_CERTIFIED.
- PC obligations: PC-VIEWS (producer of View_v constructors), PC-RELIAB interface (metadata only).
- Threats: COL-T01/02/03/05/06/07 (search/holdout discipline — control: hidden-holdout absence attested + search excludes holdout), COL-T16 (calibration omitted — control: calibration required artifact), COL-T17 (synthetic/observational merge — control: source-class tags), COL-T20 (artifact-manifest binding — control: run manifest hashes), COL-T28 (OOD confident — control: abstention/OOD interface).
- Tests: model-interface, calibration, leakage, schema — producer harness.
- Schemas produced: TaskSpecSchema, SpecialistSpecSchema, RunManifestSchema, QualificationReportSchema (draft→v1 here), CapabilityMapSchema (builder).

### B. Entry conditions
- GATE-06 + GATE-07 PASSED (authorized views definable). GATE-04/05 still pinned (touch/views consistent). No candidate freeze yet (dev candidates only). No holdout reveal (HOLD-01 enforced: holdout bank if created is sealed and inaccessible).

### C. Scientific scope
- Resolves: can Forge manufacture reproducible, leakage-free, calibrated, abstaining dev candidates with capability maps under resource caps, without promoting any Lord?
- MUST NOT claim: any Lord qualified; any holdout result; any closure.

### D. Exact files
- New: `forge/datasets/*` (completion), `forge/tasks/factory.py` + `configs/tasks/*.yaml` (TaskSpec per lord role, with allowed/forbidden evidence mandatory), `forge/training/trainers/{sklearn,xgboost,lightgbm,catboost,torch}.py`, `objectives/`, `sampling/`, `search/`, `callbacks/`, `reproducibility/`, `forge/calibration/*` (Platt/isotonic/temperature + ECE/Brier/reliability/coverage-risk), `forge/qualification/harness.py` (Q_* gates as code, dev mode), `forge/stress/*` (role suites), `forge/manifests/*`, `src/council/evidence/views.py` (PRE/POST/NO_STELLAR/NO_NEIGHBOR/NO_SPECIALIST/LIMITED_AUTHORITY views), `scripts/{build_dataset,train_specialist}.py`, runs under `runs/<run_id>/` (git-ignored binaries, committed manifests only).
- TaskSpecs frozen as drafts here (frozen for qualification in WP-6).
- Tests: `tests/forge/*` (task validate, split validity, trainer smoke on tiny synthetic, calibration bins, abstention flags, view enforcement).

### E. Code details
- `TaskSpec`: required fields per Sec-17.1 enforced by validator (`col task validate`); `allowed_evidence`/`forbidden_evidence` mandatory; view constructor filters H fields accordingly (forbidden field present in input -> error, never silent drop).
- Trainers: config-driven, `run_id` immutable (uuid4 + hash of config+dataset+code_hash), `environment.json` (pip freeze + cuda), `seed.json`; classical via sklearn/xgb/lgbm/catboost; torch compact (MLP/1D-CNN within 5e4–2e6 params default, ≤5e6 only with reason + VRAM proof). Search: small grids/Optuna with ordering Sec-20 (legality→leakage→validation→calibration→abstention→stress→smaller→cheaper→simpler→lower variance); larger model never outranks smaller on negligible gain (tie-break rule coded).
- Calibration: separate split from fitting; outputs Brier/ECE/bins/class-conditional/mission-conditional/SNR-conditional/coverage-risk/threshold/abstention-coverage. Abstention output: prediction/prob/uncertainty/applicability/abstained/reason with six disjoint reasons (MODEL_ABSTAIN/MODEL_OOD/EVIDENCE_MISSING/REPRESENTATION_OPEN/AUTHORITY_BLOCKED/CONTROLLER_BUDGET_STOP).
- Capability builder: strata metrics (mission/SNR/period/depth/coverage/transit-count/stellar/contamination/label-confidence) + known weaknesses disclosure (no hiding).
- Resource: VRAM check fails closed if >4GB under frozen config (COL-STOP-21 handler).

### F. Mathematical obligations
- No theorems. Obligation: SpecialistSpec training-time evidence == runtime view evidence (checked by view-enforcement test; mismatch disqualifies that view). Finite validation success never a qualification verdict (qualification executes in WP-6 under holdout).

### G. Benchmarks/anti-overfitting (explicit)
- Statistical models ARE trained here (dev only). Training corpus: DEVELOPMENT + LEGACY_HISTORICAL + SYNTHETIC_STRESS (explicit source classes); validation: INTERNAL_VALIDATION object-disjoint; hidden holdout NEVER touched (attest in run manifest `holdout_accessed=false`); teacher scenarios only TEACHER_GENERATED_DEVELOPMENT, never relabeled observational. Seeds frozen per TaskSpec seed_policy; hyperparameters frozen per run; leakage controls: object-level grouping + `leakage_report.json` per dataset version; mutation: forbidden-evidence mutant must be rejected; OOD tests per lord; no benchmark adaptation (dev metrics never tune holdout).

### H. Verification
- `col task validate --spec configs/tasks/<id>.yaml`, `col train run --spec ... --dataset ...`, `col calibrate ...`, `pytest tests/forge -q`, registry-absent check (no promotion), `check_workplan_coverage.py`, VRAM feasibility log for torch candidates.

### I. Exit gate
- Success: GATE-03 (full factory manifests+leakage zero) + GATE-08 (end-to-end dev run per lord role with run manifests) + GATE-09 (calibration pipeline emits required outputs on dev data) + GATE-10 (harness executes Q_* on dev data, correctly FAILs unqualified dev models).
- Failure: leakage/forbidden-evidence/VRAM breach -> GATE FAIL; WP-5/WP-6 BLOCKED until new dataset/task version.

### J. Failure behavior
- Harness failure -> FORGE_QUALIFIED_RUNTIME_BLOCKED candidate; no promotion attempted; dev artifacts remain non-registry.

### K. Commit/push rule — message `COL-PC-v1.0 WP-4 forge (PHASE-11..15, GATE-03/08/09/10)`.

---

## WP-5 — Muse teacher and adversarial development (Sec-46 WP-5; development-only)

### A. Normative coverage
- Sec: SEC-29 (teacher subsystem, jobs, schemas, provenance, budget), SEC-30 (adversarial scenario pattern + families), SEC-31 (failure discovery + acceptance criteria).
- PHASEs owned: PHASE-16 (teacher infra), PHASE-17 (adversarial/dev generation). Exactly one owner each.
- Gates owned: COL-GATE-11 TEACHER_PIPELINE_CERTIFIED.
- Threats: COL-T04 (teacher as ground truth — control: synthetic-only + validation gate), COL-T05/06/07 (holdout-conditioned generation — control: prompt-hash audit + holdout-blind attestation), COL-T22/23/24 (budget/route/numerals — controls: budget fail-closed, route logging, deterministic materializer).
- Stops: COL-STOP-11/18/19/20.
- Tests: teacher schema tests, budget tests, provenance tests (producer).

### B. Entry conditions
- GATE-08 + GATE-10 PASSED (Forge can consume teacher scenarios as dev data). No candidate freeze. Holdout sealed (if exists) — prompts must not contain holdout outcomes (audited). `OPENCODE_API_KEY` via env only (never committed).

### C. Scientific scope
- Resolves: can Muse propose adversarial scenarios/failure hypotheses/representation refinements through a schema-bound, budget-capped, provenance-recorded pipeline whose outputs are always synthetic/dev and deterministically materialized?
- MUST NOT claim: teacher output is ground truth, labels, holdout evidence, or runtime authority.

### D. Exact files
- New: `forge/teacher/muse/{client.py,prompts/*,schemas/*,budget.py,replay.py}`, `forge/teacher/adversarial_generation/*`, `failure_analysis/*`, `curriculum/*`, `representation_proposals/*`, `validation/*`, `configs/teacher/budget_v1.json` (USD 25 ceiling), `benchmarks/development/teacher_scenarios_v1/` (materialized cases with SYNTHETIC_STRESS/LLM_PROPOSED_SCENARIO tags), `TEACHER_BUDGET_LEDGER.json`, `TEACHER_PROVENANCE_MANIFEST.json` (hashes, no secrets).
- Secrets: `.env.example` (OPENCODE_API_KEY name only); `budget.py` fail-closed; `replay.py` caches scrubbed responses + hashes.
- CLI: `col teacher generate/audit` (JSON + ledger update).
- Tests: `tests/forge/test_teacher_schema.py`, `test_budget_fail_closed.py`, `test_provenance_scrub.py`, `test_materializer_deterministic.py`.

### E. Code details
- `client.py`: OpenCode route (model `muse-spark-1.3-contributor` pinned in config; route/version recorded per transaction); retries bounded; timeouts explicit; no hidden prompt injection (prompt templates hashed, `prompt_hash` stored).
- `budget.py`: pre-call estimate + post-call actual; `remaining <= 0` or `estimate > remaining` -> abort nonzero before network call; ledger append-only.
- Materializer: JSON-schema-validated scenario constraints -> deterministic/physics-aware generator (seeded RNG, recorded seed) -> light-curve/feature case with `source_class=SYNTHETIC_STRESS`, `generator_version`, `teacher_proposal_hash`; freeform text never ingested as label.
- Failure analyst: clusters numeric failures first (deterministic), then bounded summaries to teacher; acceptance only via deterministic criterion/statistical separation/new test family/physical check/human rationale (coded checklist + human sign-off file).
- Representation proposals: schema-only output (`representation_proposals/*.json`), applied only via WP-3 engine in new version, never direct P_R mutation.

### F. Mathematical obligations
- None. Obligation: prove-by-audit that no teacher bytes entered H, labels, holdout, or registry without validation + provenance (audit query must return empty set).

### G. Benchmarks/anti-overfitting
- No ML trained here. Teacher outputs are TEACHER_GENERATED_DEVELOPMENT/CONTAMINATED_CANARY by construction, usable for dev/stress, never FRESH. Prompt audit ensures no holdout conditioning. One-way gate: dev -> stress suite version bump only.

### H. Verification
- `col teacher audit --ledger ...` (budget sum, secret scan, schema pass rate), `pytest tests/forge -k teacher -q`, `rg -i openrouter` must be empty (provider is OpenCode), `rg -i 'sk-...|api[_-]?key'` on committed files must be empty.

### I. Exit gate
- Success: GATE-11 (client+budget+schemas+replay+materializer+failure-analyst all certified on dev data; ledger balanced).
- Failure: budget exceeded/secret leak/ground-truth bypass -> STOP-19/20/11, WP-6 BLOCKED until rotated + sealed.

### J. Failure behavior
- Budget exhausted -> terminal candidate TEACHER_BUDGET_EXHAUSTED; teacher pipeline frozen; Forge may continue only on non-teacher dev data.

### K. Commit/push rule — message `COL-PC-v1.0 WP-5 teacher (PHASE-16/17, GATE-11)`; verify no secrets in diff before push (`git diff --cached --check` + secret scan).

---

## WP-6 — Specialist qualification and registry (Sec-46 WP-6)

### A. Normative coverage
- Sec: SEC-15 (frozen datasets), SEC-17/18 (frozen TaskSpec/SpecialistSpec), SEC-21/22/23/24 (calibration/abstention/qualification/capability), SEC-26 (registry layout/immutability), SEC-41/42 (holdout/labels), SEC-61 (Lord promotion list).
- PHASEs owned: PHASE-18 (initial search), PHASE-19 (candidate freeze), PHASE-20 (holdout reveal), PHASE-21 (registry promotion). Exactly one owner each.
- Gates owned: COL-GATE-12 SPECIALIST_CANDIDATE_SET_FROZEN, COL-GATE-13 FRESH_HOLDOUT_REVEALED_ONCE, COL-GATE-14 INITIAL_LORDS_QUALIFIED, COL-GATE-15 REGISTRY_SEALED.
- Qualification gates executed: Q-01..07 + LPC-01..16 (each candidate must pass all; aggregate accuracy insufficient).
- Holdout rules enforced: HOLD-01..08 (exactly-once reveal, no regeneration, no second unlock).
- Threats: COL-T05/06/07 (holdout discipline), COL-T14 (fixed weights as reliability — control: r_i(s) metadata only), COL-T16/18/20/21 (calibration/legacy/binding/mutation), COL-T28 (OOD).
- Stops: COL-STOP-09/10/12/13/14/15.
- Tests: qualification, calibration, registry integrity, leakage (execution, not just harness).

### B. Entry conditions (strict, firewall)
- GATE-08 + GATE-09 + GATE-10 + GATE-11 PASSED. TaskSpecs + training/validation populations + thresholds + hidden holdout bank + candidate set + calibration protocol + stress suites all FROZEN with hashes recorded BEFORE any training in this WP (preregistration commit). Holdout bank generated+committed (hashes) BEFORE target-guided synthesis, revealed only AFTER GATE-12. No fresh-bank read before candidate freeze (checker assertion 17). Controller/runtime (WP-7) must not consume candidates yet.

### C. Scientific scope
- Resolves: which dev candidates, if any, earn registry eligibility (the title Lord) under the frozen qualification contract and sealed holdout? Qualification earns registry eligibility only; it does not authorize runtime use — authority (Lambda, WP-7) licenses use.
- MUST NOT claim: closure, optimality, exoplanet confirmation, or that failed candidates prove impossibility.

### D. Exact files
- Prereg (before training): `forge/manifests/QUALIFICATION_PREREG_v1.json` (task/dataset/split/threshold/holdout-hash/candidate-list/protocol/stress versions + seeds).
- New: `runs/*` manifests (frozen), `audits/qualification/<lord>_QUALIFICATION_REPORT.json` (per LPC checklist), `<lord>_CAPABILITY_MAP.json`, `benchmarks/manifests/HOLDOUT_MANIFEST.json` (sealed then revealed once), `registry/<lord>/vX.Y.Z/*` (model bytes + spec/task/calibration/capability/dataset/qualification/environment/signature/checksums), `REGISTRY_MANIFEST.json`, `scripts/qualify_specialist.py`, `col qualify` + `col registry verify/list` implementations.
- Tests: `tests/forge/test_candidate_freeze.py`, `test_holdout_once.py`, `tests/registry/test_immutability.py`, `test_bytes_match_qualification.py`.
- Baselines required first per Sec-60 (majority/logreg/RF/GBM/XGB/LGBM/CatBoost) before custom CNN justification.

### E. Code details
- `qualify_specialist.py`: loads prereg, verifies dataset/split/task hashes, trains/freezes candidates (or loads frozen candidates), runs Q_* on validation then ONCE on holdout after GATE-12, emits capability maps with disclosed weaknesses, promotes only all-pass candidates with new semantic versions (any byte/calibration/preproc/contract change -> new version). Registry verifier checks hashes, version immutability, calibration-model binding, capability-artifact binding.
- Search ordering per Sec-20 coded; classical baselines precede torch CNN; CNN only if beats/complements on declared role within 4GB VRAM.
- Holdout reveal: `scripts/reveal_holdout_once.py` appends single reveal record (timestamp+hash+accessor) to ledger; second invocation aborts (no second unlock, no regeneration after reveal).

### F. Mathematical obligations
- Qualification is a conjunction Q(M)=Q_general∧…∧Q_semantic; each conjunct has explicit gate code + report section. Finite holdout survival is evidence for promotion under the contract, never a universal guarantee (CLAIM-09 enforced in report disclaimer).

### G. Benchmarks/anti-overfitting (strictest)
- Models trained: classical + compact torch as preregistered. Training: prereg corpora; validation: INTERNAL_VALIDATION; test: FRESH_QUALIFICATION_HOLDOUT (one reveal); contaminated/legacy never fresh; seeds frozen; hyperparameters frozen at GATE-12; leakage: object-level + `leakage_report.json` zero-overlap proof; mutation: holdout-in-train mutant killed; OOD + stress required; no benchmark adaptation (any post-reveal repair -> new campaign + new bank per HOLD-03).

### H. Verification
- `col qualify --prereg ...`, `col registry verify --manifest REGISTRY_MANIFEST.json`, `pytest tests/registry tests/forge -q`, deterministic rerun reproduces qualifying bytes or metrics within frozen tolerance, `check_workplan_coverage.py` + `check_lifecycle.py` (no runtime consumption yet) + `check_firewall.py` (reveal-once proof).

### I. Exit gate
- Success: GATE-12 (candidate set hash frozen) -> GATE-13 (single reveal recorded) -> GATE-14 (only all-pass candidates promoted, reports complete) -> GATE-15 (registry seal verifies cleanly).
- Failure: STOP-09/10/12/13/14/15 -> HOLDOUT_CONTAMINATED / SPECIALIST_QUALIFICATION_FAILED / DATASET_INTEGRITY_FAILED; failed attempts preserved (REPRO-02); no relabeling.

### J. Failure behavior
- Qualification failure -> FORGE_QUALIFIED_RUNTIME_BLOCKED or SPECIALIST_QUALIFICATION_FAILED terminal candidate; WP-7 NOT_REACHED for unqualified lords; honest seal required (no success narrative rewrite).

### K. Commit/push rule — message `COL-PC-v1.0 WP-6 qualification-registry (PHASE-18..21, GATE-12/13/14/15)`; record holdout reveal hash + registry seal hash in Path.md.

---

## WP-7 — Council runtime integration (Sec-46 WP-7)

### A. Normative coverage
- Sec: SEC-04/05 (checkpoint/closure wiring), SEC-08 (Lambda enforcement), SEC-09/10 (action execution), SEC-25 (reliability r_i(s) metadata), SEC-27 (SpecialistResult interface), SEC-28 (authorized views enforcement), SEC-32 (engine layout), SEC-33 (controller), SEC-56 (runtime report).
- PHASEs owned: PHASE-22 (controller integration), PHASE-23 (authorized resource views audit), PHASE-24 (trace/replay). Exactly one owner each.
- Gates owned: COL-GATE-16 COUNCIL_RUNTIME_CERTIFIED, COL-GATE-17 RESOURCE_VIEW_AUDIT_PASSED.
- Council promotion criteria executed: CPC-01..10 (all must hold before PC evaluation).
- Threats: COL-T12/15/25/27/29 (authority/closure/API/unresolved/side-channel), COL-T08/11/13 (touch/score/split via runtime actions).
- Stops: COL-STOP-16 (vote bypass), COL-STOP-22 (frontend/API required for core).
- Tests: PC semantic (runtime), model-interface (view-filtered), registry (qualified-only loading).

### B. Entry conditions
- GATE-14 + GATE-15 PASSED (registry sealed; only qualified bytes loadable). GATE-04/05 still pinned (closure/touch agree). GATE-12/13 ledger shows legal reveal-once. Controller config frozen. No freeze-geometry claims yet (WP-8).

### C. Scientific scope
- Resolves: can registry Lords be integrated as recommend-only advisors inside a PC-native sequential engine where only the controller executes source-atomic actions and closure is PC-defined?
- Authority doctrine: a qualified Lord is only eligible; Lambda licenses actual use. The controller loads a qualified version AND checks current Lambda + authorized views before any call. MUST NOT claim: freeze geometry, clean-room reproduction, terminal qualification (WP-8).

### D. Exact files
- New: `src/council/lords/{base,loader,morphology,periodicity,false_positive,stellar,instrument,general}.py`, `src/council/controller/{policy,planner,action_ranker,budget}.py`, `src/council/registry/{reader,verifier,schemas}.py`, `src/council/reporting/{trace,candidate_report,audit_report}.py`, `src/council/cli/` verbs `col council analyze/replay`, configs `configs/controller/policy_v1.yaml` (deterministic heuristic; learned controller out of scope), `audits/pc/WP7_VIEW_AUDIT.json`.
- Specialist interface: `lord.evaluate(view)` returning SpecialistResult per Sec-27 (claims/probs/uncertainty/applicability/ood/abstained/reason/diagnostics/recommended_actions/evidence_refs/provenance/hash); lords cannot mutate H/P_R/Lambda (enforced by capability: view is deep-frozen copy + loader drops write handles).
- Reports: per Sec-56 fields (identity/provenance/hash-chain/actions/pre-post/touch/refinements/transitions/versions/views/abstentions/worlds/open-closed/terminal-or-escalation/cost/replay).

### E. Code details
- `loader.py`: verifies registry signature+checksums, rejects LEGACY_UNQUALIFIED/unqualified bytes for closure paths (regression-only wrapper allowed for side-by-side, never as qualified producer); version pinning exact.
- `policy.py`: deterministic heuristic over (omega, open/closed, recommendations, capability metadata, cost, world distinctions, authorized views); seeded RNG only if declared; forbidden: hidden-label peek, holdout-truth peek, forbidden evidence, unqualified calls, confidence-override of closure, P_R rewrite after truth observation (each forbidden path has a test asserting refusal).
- `views.py` enforcement: each lord receives `View_v` filtered copy; runtime asserts `input_view_hash` matches authorized view + SpecialistSpec allowed set; mismatch -> AUTHORITY_BLOCKED abstention, never silent coercion.
- `budget.py`: unit costs + real-cost ledger (CPU/GPU/API/catalog/human); budget warnings via Lambda `may_continue_after_budget_warning`; UNRESOLVED termination under explicit rule remains legal.
- Trace: every transition logs pre/post IDs, derived touch (primary+independent), cost; replay re-executes ledger to identical terminal checkpoint under declared conditions.

### F. Mathematical obligations
- Closure consumed from WP-2: closed states emit only common target class; open states never emit closed verdicts (type + test). r_i(s) is reliability metadata, never a hidden vote weight (historical 1.4x pattern forbidden by test asserting no such constant). Qualification bytes prove eligibility, never authorization — every runtime call site re-checks Lambda (test: qualified lord under revoked Lambda abstains with AUTHORITY_BLOCKED). Finite runtime demos are not closure proofs.

### G. Benchmarks/anti-overfitting
- No new ML trained (state explicitly; learned controller is later extension, out of scope). Candidate discovery already frozen; runtime consumes only registry versions. Views enforce train/runtime evidence match (mismatch disqualifies that view). Diagnostics/benchmarks: DEVELOPMENT + ADV families + FORMAL_PC_CONSTRUCTED; holdout not re-accessed; clean-room pending WP-8.

### H. Verification
- `col council analyze --target ... --ledger ...`, `col council replay --trace ...`, `pytest tests/pc tests/registry -q`, view-audit (`every specialist input hash ∈ authorized views`), mutation spot-checks (vote-bypass, hidden-weight, unqualified-load mutants killed), `check_workplan_coverage.py` + lifecycle (no pre-qualified consumption) + firewall (no post-reveal training).

### I. Exit gate
- Success: GATE-16 (authorized-only inputs, no state mutation by lords, controller-executed actions, PC closure, legal UNRESOLVED, logged+replayable) + GATE-17 (view audit passed).
- Failure: CPC failure / vote bypass / view violation -> GATE FAIL; WP-8 NOT_REACHED.

### J. Failure behavior
- Runtime violation -> COUNCIL_RUNTIME BLOCKED; registry remains sealed; no freeze-geometry claims; fix requires new controller/loader version + re-certification.

### K. Commit/push rule — message `COL-PC-v1.0 WP-7 runtime (PHASE-22/23/24, GATE-16/17)`.

---

## WP-8 — Freeze geometry, clean-room, final seal (Sec-46 WP-8)

### A. Normative coverage
- Sec: SEC-35 (kappa/K recomputation), SEC-36 (8 PC questions), SEC-37/38 (identification + independent recomputation at release), SEC-40/42 (adversarial + labels at release), SEC-43 (full mutation campaign), SEC-45 STOP-19..25 release stops, SEC-51 (release package), SEC-57/58 (optional API/frontend, omissible), SEC-59 (priority order attested), SEC-62/63/64/67/68 (promotion/terminals/successor/audit/doctrine).
- PHASEs owned: PHASE-25 (freeze geometry), PHASE-26 (mutation campaign), PHASE-27 (clean-room reproduction), PHASE-28 (optional API), PHASE-29 (optional frontend), PHASE-30 (final seal). Exactly one owner each; PHASE-28/29 may be omitted (record NOT_APPLICABLE with reason, never blocking GATE-21).
- Gates owned: COL-GATE-18 PC_FREEZE_GEOMETRY_RECOMPUTED, COL-GATE-19 MUTATION_SUITE_PASSED, COL-GATE-20 CLEANROOM_REPRODUCTION_PASSED, COL-GATE-21 PC_NATIVE_COUNCIL_QUALIFIED (terminal).
- Artifacts produced: ART-01..19 (all producer WP-8 Release package).
- Audit questions answered: AUDQ-01..15 (each yes with evidence or explicit limitation -> weaker terminal per Sec-67).
- Threats: all COL-T01..30 re-audited at release (freeze controls); Stops: COL-STOP-16..25 release enforcement.
- Terminal: selects exactly one of TERM-01..10 honestly (weaker terminal if any AUDQ is NO).

### B. Entry conditions
- GATE-16 + GATE-17 PASSED. Registry sealed (GATE-15 hash). Holdout ledger legal (GATE-13 once). Source closure artifact (GATE-22) re-verified: registry STATUS ledger still all-terminal. PC contract + schemas + target + atomicity hashes all pinned and unchanged since WP-2/WP-3 (any change -> successor version, not in-place edit). No uncommitted science files.

### C. Scientific scope
- Resolves: under the frozen contract, what is the resource dependence (freeze signature), does the system survive mutation/falsification, reproduce from clean checkout, and close the terminal claim honestly?
- MUST NOT claim: exoplanet confirmation, production validity, prevalence from unit costs, or impossibility from RESOURCE_LIMIT_REACHED.

### D. Exact files
- New: `FREEZE_RESULTS.json` (kappa/K in EMPTY,E,R,A,ER,EA,RA,ERA order + per-PCQ answers), `TOUCH_RECOMPUTATION.json` (primary vs independent agreement at release), `MUTATION_RESULTS.json` (21 mutants killed/blocked per suite), `RELEASE_MANIFEST.json`, `SOURCE_COMMIT.txt`, `ENVIRONMENT_LOCK.*`, `FINAL_AUDIT.md` (AUDQ yes/no + evidence), `FINAL_RESULT.json` (terminal state + hashes), `audits/{pc,mutation,release,leakage,qualification}/*`, optional `src/council/api/*` (adapter only, after GATE-16) + frontend stub (observational only; both must pass STOP-22 check: core runs without them).
- CLI: `col pc freeze`, `col audit full`, `scripts/final_audit.py`, `scripts/run_council.py`.
- Tests: freeze, mutation, clean-room reproduction, legacy regression (import under LEGACY_HISTORICAL).

### E. Code details
- Freeze runner: exact planner on controlled evaluation instances (feasible sizes only; infeasible -> declared limitation, not guessed signature); 8-mask computation with whole-action removal; K tuple ordered as specified; per-PCQ controlled cases (Sec-36) executed as separate instances (E-only/R-only/A-only closures, stellar-removal fallback vs structural failure, morphology substitution, specialist cost reduction without necessity, pipeline-dependence divergence, underidentified refusal).
- Mutation runner: each MUT-01..21 mapped to assigned suite(s); suite must kill (fail-closed) its mutants; survivors block GATE-19.
- Clean-room: fresh checkout (or `git worktree`) + `ENVIRONMENT_LOCK` + manifests -> rerun qualification sample + council replay -> byte/metric match within frozen tolerance; frontend/API absent during core rerun.
- API/frontend (if built): thin adapters; static check asserts no scientific logic (no preprocessing/model-selection/scoring/closure/authority/representation code outside `src/council/` + `forge/`).

### F. Mathematical obligations
- Kappa/K are implementation resource diagnostics on controlled instances, not astronomical prevalence claims (disclaimer in FREEZE_RESULTS). Closure-cost claims state unit-cost convention explicitly. No finite benchmark upgraded to confirmation (CLAIM-09 test).

### G. Benchmarks/anti-overfitting (release)
- Final evaluation uses: dev (tuning history disclosed), INTERNAL_VALIDATION, CONTAMINATED_CANARY (regression), FRESH holdout (already revealed once in WP-6, now historical for future versions — never re-revealed), CLEANROOM_POST_FREEZE (new clean-room runs), FORMAL_PC_CONSTRUCTED (finite PC instances), OBSERVATIONAL_EXTERNAL_TEST where available. No new holdout access in WP-8. Post-freeze large-n/adversarial testing allowed only without changing frozen candidates. Formal proof remains as in WP-2 (deterministic checkers; no Lean claim).

### H. Verification
- `col pc freeze --manifest ...`, `col audit full --release ...`, `pytest tests/mutation tests/pc -q`, `python scripts/final_audit.py --release RELEASE_MANIFEST.json`, fresh-checkout reproduction (`git clone <remote> <tmp> && <repro steps>`), `col registry verify`, source-closure re-verification (`audits/WP1_SOURCE_CLOSURE.json` still all-terminal), secret scan, VRAM re-attestation, `python scripts/check_workplan_coverage.py` (still PASS), lifecycle + firewall re-checks.

### I. Exit gate
- Success: GATE-18 (K recomputed + PCQs answered) + GATE-19 (all assigned mutants killed) + GATE-20 (clean-room replay matches) -> GATE-21 `PC_NATIVE_COUNCIL_QUALIFIED` (or weaker TERM honestly selected, e.g., QUALIFIED_WITH_DECLARED_LIMITATIONS if an AUDQ is NO with disclosed limitation).
- Failure: any release STOP (16..25) or AUDQ NO without limitation -> terminal is failure state (e.g., HOLDOUT_CONTAMINATED, RESOURCE_LIMIT_REACHED as limit-not-impossibility, ARCHITECTURE_SUCCESSOR_REQUIRED sealed honestly then v1.1 proposed).

### J. Failure behavior
- Release failure freezes the architecture honestly (SUCC-01/02): preserve witness, diagnose missing resource, seal v1.0 with failed terminal, propose successor only with newly justified coordinate. No in-place semantic rewrite. Stale v0.4-namespace outputs quarantined per hygiene (only new outputs in `artifacts/v04/`-equivalent `release/` namespace; history preserved).

### K. Commit/push rule — message `COL-PC-v1.0 WP-8 seal (PHASE-25..30, GATE-18/19/20/21)`; record release SHA + remote HEAD + FINAL_RESULT in Path.md; tag `col-pc-v1.0-qualified` only if GATE-21 passed.

---

## Appendix — Cross-WP traceability (summary; authoritative map is WORKPLAN_COVERAGE.yaml)

- PHASE ownership: WP-0:00,01 | WP-1:02,03,04 (04 incl. frozen source registry + acquisition + closure audit) | WP-2:05,06,07 | WP-3:08,09,10 | WP-4:11,12,13,14,15 | WP-5:16,17 | WP-6:18,19,20,21 | WP-7:22,23,24 | WP-8:25,26,27,28,29,30. Exactly one owner per phase.
- GATE producers: WP-0:00,01 | WP-1:02,22 | WP-4:03,08,09,10 | WP-2:04,05 | WP-3:06,07 | WP-5:11 | WP-6:12,13,14,15 | WP-7:16,17 | WP-8:18,19,20,21. (GATE-22 produced WP-1, re-verified WP-8; numbering append-only, GATE-21 remains terminal.)
- Every THREAT/STOP/TEST/ARTIFACT/SCHEMA/HOLDOUT/MUTANT/DIAG/ADV/CLI/AUDQ/LPC/CPC/PC-obligation/SRC-family/SRC-field/SRC-status maps to ≥1 WP in coverage; every HOLD freeze transition has permitted owner/order; every candidate-freeze rule represented; lifecycle (candidate→eligible→registry→Lambda-licensed-runtime) enforced; no fresh read before freeze; no legacy-as-fresh; no silent source omission; no surgical-boundary breach.
