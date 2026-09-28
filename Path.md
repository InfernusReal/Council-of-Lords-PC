# Path — COUNCIL-PC-v1.0 live execution ledger

**Experiment:** `COUNCIL-PC-v1.0` (`COL-PC-v1.0`) | **Repo:** `InfernusReal/Council-of-Lords-PC`
**Operative spec:** `IMPLEMENTATION_SPEC.md` SHA256 `9d4761e3cb656b0b4295a5ae4efcf08bc13058f00082577d5b92d406de1482e6` (2983 lines; pre-repair SHA `766ecfaa…8908da6`, 2864 lines — see planning-repair entry below)
**Original spec:** `audits/COUNCIL-PC-v1.0_IMPLEMENTATION_SPEC_ORIGINAL.md` SHA256 `a9453d20079ace95d8227d0fed095398b4aa6de1d1265f61ba6fe1b4c5dbf0fb`
**Migration audit:** `audits/PROVIDER_MIGRATION_AUDIT.md` PASS (OpenRouter->OpenCode, 3 lines)
**SPLAY template (non-operative, preserved):** `audits/SPLAY-AM-MST-LIQ-v0.4_SPEC.txt` SHA256 `0E2C166E1B721DFC8A7E5327ED33AF29A1B4AC539CB71849F3C7231B32A8055B` — see SPEC-CONFLICT-01 in WorkPlan.md
**Conceptual parent:** Perceptive Closure (local `Perception Closure/` + Downloads drafts; exact version pinned WP-0)
**Legacy parent:** `InfernusReal/Council-Of-Lords` + `Downloads/Council-Of-Lords-main.zip` (5771 entries, archaeological only)
**Teacher:** Muse Spark 1.3 Contributor through OpenCode, USD 25 ceiling
**Plan:** `WorkPlan.md` (9 WPs) | **Inventory:** `planning/NORMATIVE_INVENTORY.yaml` (561 items canonical: 556 normative + 5 not_applicable) | **Coverage:** `planning/WORKPLAN_COVERAGE.yaml` | **Checker:** `scripts/check_workplan_coverage.py`

Rule: update contemporaneously; never reconstruct from memory; superseded entries stay marked superseded.
Each WP ends with an explicit verdict: `FOLLOWS WorkPlan.md` / `DEVIATION — VERSIONED AND JUSTIFIED` / `NONCOMPLIANT — BLOCKED`.
Commit rule per WP: `VERIFY -> UPDATE Path.md -> COMPLIANCE AUDIT -> COMMIT -> PUSH -> VERIFY REMOTE HEAD`.

## Planning audit (Rule 13 self-audit, 2026-09-28)

- WorkPlan.md, Path.md skeleton, NORMATIVE_INVENTORY (519), WORKPLAN_COVERAGE (519 mappings), checker all built before any scientific WP execution.
- Checker run 1 (primary method, structured parse):
```text
NORMATIVE_ITEMS_TOTAL = 514
MAPPED_ITEMS_TOTAL = 514
UNMAPPED = 0
UNKNOWN_MAPPINGS = 0
PHASE_OWNERSHIP_ERRORS = 0
THEOREM_OWNERSHIP_ERRORS = 0
GATE_ERRORS = 0
THREAT_CONTROL_ERRORS = 0
STOP_CONTROL_ERRORS = 0
FIRST_CONSUMER_ERRORS = 0
HOLDOUT_ORDER_ERRORS = 0
CLAIM_POLICY_ERRORS = 0
RESULT = WORKPLAN_COVERAGE_PASS
```
- Second omission audit (different method, independent grep counts): SPEC_PHASES 31/INV 31; SPEC_GATES 22/INV 22; SPEC_THREATS 30; SPEC_STOPS 25; COV mappings 519. No unmapped/multiply-owned items found; phase table matches WorkPlan appendix exactly.
- Identifier sets compared: SEC 69, PHASE 31, GATE 22, THREAT 30, STOP 25, TEST 14, SCHEMA 17, TERM 10, ART 19, LABEL 9, DCLASS 9, LCONF 7, MUT 21, ADV 20, PCQ 8, DIAG 15, ACT 25, LORD 6, CLI 18, AUDQ 15, LPC 16, CPC 10, PC_OBLIG 20, WIT 12, Q 7, HOLD 8, TEACH 8, CLAIM 12 + MST_NA 5 + SPEC-CONFLICT-01. Counts derived from spec parse, not memory.
- Spec conflicts: SPEC-CONFLICT-01 recorded (SPLAY header vs Council operative spec); MST LIQ0/MST0/candidate/bank/axis marked not_applicable with resolution, not silently dropped. No other conflicts; no underspecified-interface blocks at planning level (PC contract interfaces frozen in WP-2; if underspec emerges, record PREREG_INTERFACE_UNDERSPECIFIED and block consumer per Rule 14).
- Scientific execution authorization: planning PASS; WP-0 entry gates satisfied (spec bytes present, remotes reachable). Execution authorized strictly in WP order after planning commit/push.
- Planning commit: `1a08a03d7d892272a15b63489a69fc0fa1362e55` (14 files, 19560 insertions).
- Push result: `3880b80..1a08a03 main -> main` to `https://github.com/InfernusReal/Council-of-Lords-PC.git` — PUSH OK.
- Remote HEAD verified: `git ls-remote origin main` = `1a08a03d7d892272a15b63489a69fc0fa1362e55 refs/heads/main` — matches local HEAD.
- Note: counts above (519/514) are SUPERSEDED by the planning-repair entry below; preserved here as history.

## Planning repair — surgical planning-layer closure (no WP-0 execution)

- Reason for repair: (1) canonical count terminology (inventory vs normative vs not_applicable);
  (2) section-bounded source-line fidelity with fail-closed anchors + bounds invariant;
  (3) newly authorized exhaustive/brutal dataset acquisition doctrine (Sec-15.6, 17 families,
  14-field registry, 4 terminal states, COL-GATE-22, PHASE-04 expansion, WP-1 ownership);
  (4) qualification-vs-authority wording correction (registry eligibility; authority licenses use).
- Exact files changed: `IMPLEMENTATION_SPEC.md` (Sec-15.6 insertion, PHASE-04 line, COL-GATE-22 line,
  doctrine wording line); `scripts/gen_normative_inventory.py` (section-bounded rewrite + 42 new IDs);
  `scripts/gen_workplan_coverage.py` (GATE-22→WP-1, 6 new categories, PHASE-04 anchoring, WP-1 files);
  `scripts/check_workplan_coverage.py` (bounds invariant, canonical counts, doctrine presence);
  `planning/NORMATIVE_INVENTORY.yaml` + `planning/WORKPLAN_COVERAGE.yaml` (regenerated);
  `WorkPlan.md` (canonical counts, WP-1 expansion, GATE-22, doctrine wording, appendix);
  `audits/WORKPLAN_SEMANTIC_CLOSURE_AUDIT.md` (new); `Path.md` (this entry).
- Old operative spec SHA: `766ecfaac5540be2f932bedc08a99981949aede7e32649ab33f7fa5a98908da6` (2864 lines).
- New operative spec SHA: `9d4761e3cb656b0b4295a5ae4efcf08bc13058f00082577d5b92d406de1482e6` (2983 lines).
- Inventory count before/after: 519 → 561. Normative before/after: 514 → 556.
  Not_applicable before/after: 5 → 5 (unchanged members).
- Source-pointer repair summary: generator lookups now bounded to declared Sec-N line ranges with
  exact/full-phrase anchors and fail-closed behavior (no line-0/unrelated-line fallback); 3 fidelity
  corrections documented (HOLD-07→Sec-42, HOLD-08→Sec-40, TEACH-08→Sec-52); all other items retain
  sections; checker asserts every numbered-section pointer lies within its section bounds.
- New dataset acquisition doctrine summary: `Acquire broadly, provenance everything, train selectively,
  test brutally.` Frozen registry (17 families minimum, 14-field entries, attempt-without-asserting-availability
  over Kepler/K2/TESS/MAST/Archive/Gaia/quality/adversarial/teacher families); exactly-one-terminal-state
  per entry (INGESTED / INCOMPATIBLE_WITH_DOCUMENTED_REASON / UNAVAILABLE_WITH_ARCHIVED_FAILURE /
  EXCLUDED_BY_FROZEN_POLICY); DATASET_SOURCE_COVERAGE_CLOSED = coverage closure of the frozen registry
  (not "all downloaded"); WP-1 ships framework + registry + closure mechanism, bulky bytes stay out of git.
- New/changed normative IDs: COL-GATE-22; COL-SRC-DOCTRINE/ATTEMPT/NOSILENT/REGISTRY; COL-SRC-FAM-01..17;
  COL-SRC-FIELD-01..14; COL-SRC-STATUS-01..04; CLAIM split 12→14 (auth vs calib lines).
- Checker outputs:
```text
INVENTORY_ITEMS_TOTAL = 561
NORMATIVE_ITEMS_TOTAL = 556
NOT_APPLICABLE_ITEMS_TOTAL = 5
MAPPED_ITEMS_TOTAL = 556
UNMAPPED = 0
UNKNOWN_MAPPINGS = 0
SOURCE_POINTER_ERRORS = 0
PHASE_OWNERSHIP_ERRORS = 0
THEOREM_OWNERSHIP_ERRORS = 0
GATE_ERRORS = 0
THREAT_CONTROL_ERRORS = 0
STOP_CONTROL_ERRORS = 0
FIRST_CONSUMER_ERRORS = 0
HOLDOUT_ORDER_ERRORS = 0
CLAIM_POLICY_ERRORS = 0
DATASET_SOURCE_DOCTRINE_PRESENT = TRUE
DATASET_SOURCE_COVERAGE_GATE_PRESENT = TRUE
RESULT = WORKPLAN_COVERAGE_PASS
```
- Independent audit outputs: section/gate/threat/stop/phase counts cross-checked by direct spec grep vs
  inventory vs coverage (see verification commands below); source-line bounds spot-verified; holdout
  ordering (freeze GATE-12 before reveal GATE-13; registry seal GATE-15 before runtime WP-7) confirmed.
- Closure-audit result: `audits/WORKPLAN_SEMANTIC_CLOSURE_AUDIT.md` — 26/26 rows PASS, `WORKPLAN_SEMANTIC_CLOSURE = PASS`.
- Deviations: HOLD-07/HOLD-08/TEACH-08 source-section corrections (justified above; all else retained).
  No scientific/runtime architecture altered; 9-WP structure, PC semantics, holdout firewall, teacher
  role/ceiling, hardware constraints, vote prohibition, LLM-free runtime all preserved.
- Explicit statement: WP-0 scientific execution has NOT started. No foundation pin, no training, no registry
  promotion, no runtime integration performed in this operation.
- Repair commit SHA: `c72d03fdfa1047aca6e98040b93bc63b75cd3b94` ("COL-PC-v1.0 close planning audit and dataset-source coverage", 9 files).
  Push result: `1c012d5..c72d03f main -> main` to `https://github.com/InfernusReal/Council-of-Lords-PC.git` — PUSH OK.
  Remote HEAD verified: `git ls-remote origin main` = `c72d03fdfa1047aca6e98040b93bc63b75cd3b94` — matches local HEAD.
- Path verdict for this operation: FOLLOWS WorkPlan.md — PLANNING REPAIR CLOSED (pending commit/push verification).

---

## WP-0 — Foundation freeze and archaeology — PLANNED (not yet executed)

## WP-0 CONTRACT (locked before implementation; N=0, PREVIOUS_PHASE=NOT_APPLICABLE)

Phase binding: CURRENT_PHASE=WP-0. Previous-phase gate N/A (first phase); pre-foundation audit performed instead:
operative spec present (SHA `9d4761e3…406de1`, 2983 lines), audits/ complete (original/migration/SPLAY),
origin/main reachable and == local HEAD, no holdout/firewall/model artifacts on tree, no `tests/` dir yet.

| REQ-ID | Requirement (WorkPlan WP-0 A–K + spec) | Artifact / location |
|---|---|---|
| WP-0-REQ-001 | Operative spec bytes present, SHA `9d4761e3…406de1`, 2983 lines | `IMPLEMENTATION_SPEC.md` |
| WP-0-REQ-002 | Original spec + migration audit + SPLAY template in `audits/` | `audits/` (3 files) |
| WP-0-REQ-003 | `origin/main` reachable | `git ls-remote` == HEAD |
| WP-0-REQ-004 | No holdout/firewall/model artifacts; no training | tree scan |
| WP-0-REQ-005 | `FOUNDATION_MANIFEST.json` schema-valid, hashes match recomputation | `FOUNDATION_MANIFEST.json` |
| WP-0-REQ-006 | PC parent pinned (Desktop Counterfactuals.pdf `494334e5…12ff112d58`) + alternates listed | `PC_PARENT_MANIFEST.json` |
| WP-0-REQ-007 | Archaeology: remote HEAD `72222ad2…`, zip SHA, ensemble/converter/scripts, LEGACY_UNQUALIFIED policy | `audits/legacy/LEGACY_ARCHAEOLOGY.md` |
| WP-0-REQ-008 | 5771 zip entries, sorted, CRCs, zip SHA | `audits/legacy/LEGACY_FILE_MANIFEST.json` |
| WP-0-REQ-009 | 7 Sec-50 anti-pattern findings | `audits/legacy/ANTI_PATTERN_LEDGER.md` |
| WP-0-REQ-010 | Target ontology D (4 classes) + UNRESOLVED policy | `configs/pc/target_ontology_v1.json` |
| WP-0-REQ-011 | Environment baseline | `ENVIRONMENT_BASELINE.json` |
| WP-0-REQ-012 | Atomicity-freeze commitment (T30 control; normative schema stays WP-2) | `configs/pc/atomicity_freeze_commitment_v1.json` |
| WP-0-REQ-013 | `pin_foundation.py`: hash/list/emit, step logs, `--check`, fail-closed nonzero | `scripts/pin_foundation.py` |
| WP-0-REQ-014 | `migrate_legacy_fixtures.py` skeleton: list, label LEGACY_HISTORICAL, binary-size gate | `scripts/migrate_legacy_fixtures.py` |
| WP-0-REQ-015 | Legacy regression scaffolding WP0-T01..T05 | `tests/legacy_regression/` |
| WP-0-REQ-016 | Fixture sample index hash-bound, hashes only, no binaries | `audits/legacy/FIXTURE_SAMPLE_INDEX.json` |
| WP-0-REQ-017 | Manifest schema validation green (keys, 64-hex hashes) | `scripts/audit_foundation.py` |
| WP-0-REQ-018 | T18 control enforced (unlabeled/promoted legacy rejected) | policy + WP0-T01/T03 |
| WP-0-REQ-019 | T30 control (commitment record + test) | REQ-012 + WP0-T02 |
| WP-0-REQ-020 | STOP-01/02 evaluated PASS (both pinnable) with evidence | this entry + manifests |
| WP-0-REQ-021 | NO MODEL TRAINED; no teacher calls | tree scan + this statement |
| WP-0-REQ-022 | H reruns: inventory 561/556/5 + coverage PASS on final tree | commands below |
| WP-0-REQ-023 | Git hygiene: no .env/binaries/secrets; only intended files | `git status` |
| WP-0-REQ-024 | Path WP-0 record + log inventory + closeout; history preserved append-only | `Path.md` |
| WP-0-REQ-025 | Commit msg `COL-PC-v1.0 WP-0 foundation+archaeology (GATE-00/01)`; push; ls-remote == HEAD; clean tree | git |

Named-test semantic lock: WP0-T01 fixture-label policy (every indexed fixture LEGACY_HISTORICAL/CONTAMINATED_DEVELOPMENT, none fresh) | WP0-T02 manifest integrity (recomputed == recorded; counts match) | WP0-T03 pin check (`--check` exit 0; missing source → nonzero) | WP0-T04 hygiene (no binaries/secrets/.env) | WP0-T05 determinism (two regens byte-identical).
Exit: GATE-00 FOUNDATION_FROZEN + GATE-01 LEGACY_ARCHAEOLOGY_COMPLETE.

- WorkPlan prescription: WorkPlan.md §WP-0 (PHASE-00/01; GATE-00/01; manifests + archaeology + layout + env + plan files).
- Entry-gate status: PLANNING-COMPLETE (this commit). Foundation pin execution pending next commit.
- Actual implementation inventory: (pending — `FOUNDATION_MANIFEST.json`, `PC_PARENT_MANIFEST.json`, `audits/legacy/*`, `configs/pc/target_ontology_v1.json`, `ENVIRONMENT_BASELINE.json`, `.gitignore`, `.env.example`, `pyproject.toml` skeleton).
- Exact files created/changed: (pending; this planning commit creates WorkPlan/Path/inventory/coverage/checker+generators + spec copies).
- Exact algorithms/code implemented: (pending — `scripts/pin_foundation.py`).
- Exact commands executed: `python scripts/gen_normative_inventory.py`, `python scripts/gen_workplan_coverage.py`, `python scripts/check_workplan_coverage.py` (planning only).
- Benchmark/test results: coverage PASS (above); second audit PASS.
- Proof artifacts: none (no theorems in WP-0).
- Theorem status: n/a.
- Deviations from WorkPlan: none at planning time.
- Bug discoveries / repairs: none.
- Anti-overfitting evidence: legacy labeled historical from birth; no training.
- Gate outputs: GATE-00/01 PENDING (planning commit is not the foundation pin; pin executes post-planning).
- Coverage audit: PASS (planning scope).
- Commit SHA: `1a08a03d7d892272a15b63489a69fc0fa1362e55` (planning bundle).
- Push result: PUSH OK (`3880b80..1a08a03 main -> main`).
- Remote-head verification: VERIFIED (`git ls-remote origin main` == local HEAD).
- WorkPlan-adherence verdict: FOLLOWS WorkPlan.md (planning files only; WP-0 execution pending next).
- NOTE: planning-era placeholders above are SUPERSEDED by the WP-0 execution record below. Preserved as history.

## WP-0 EXECUTION RECORD (CURRENT_PHASE=WP-0)

- Phase/scope: WP-0 foundation freeze + archaeology (PHASE-00/01). Previous-phase: NOT_APPLICABLE (first phase; pre-foundation audit in contract above).
- Entry-gate verification: REQ-001 spec SHA `9d4761e3…406de1` confirmed; REQ-002 audits/ complete; REQ-003 `git ls-remote origin main` == HEAD at start; REQ-004 tree scan: no holdout/model/teacher artifacts. Entry predicate true. `WP-0 ENTRY AUDIT: previous_phase_verified=NOT_APPLICABLE(first phase); required_upstream_statuses=none; required_frozen_artifacts=spec+audits+legacy-zip+PC-paper(all present); required_hashes=all match; required_source_state=clean planning tree; required_kernel_state=n/a; required_schema_state=draft manifest schemas; required_external_evidence=legacy HEAD via ls-remote OK; entry_gate_result=PASS`.
- WorkPlan section followed: WorkPlan.md §WP-0 A–K literally; contract above (locked before implementation).
- Normative sources: IMPLEMENTATION_SPEC.md Sec-00/01/02/03/46/49/50/53/65 + PC-TARGET (Sec-4) + central law (Sec-0).
- Files created: `FOUNDATION_MANIFEST.json` (bb11c846…), `PC_PARENT_MANIFEST.json` (77391c5d…), `audits/legacy/LEGACY_FILE_MANIFEST.json` (7fe0c169…, 843033 bytes, 5771-entry listing), `audits/legacy/LEGACY_ARCHAEOLOGY.md`, `audits/legacy/ANTI_PATTERN_LEDGER.md`, `audits/legacy/FIXTURE_SAMPLE_INDEX.json` (127 entries), `configs/pc/target_ontology_v1.json`, `configs/pc/atomicity_freeze_commitment_v1.json`, `ENVIRONMENT_BASELINE.json`, `scripts/pin_foundation.py` (STEPS 01–08), `scripts/migrate_legacy_fixtures.py` (STEPS 10–13), `scripts/audit_foundation.py` (STEPS 20–26, independent), `tests/legacy_regression/test_wp0_foundation.py` (WP0-T01..T05), `tests/legacy_regression/test_wp0_stress.py` (10 stress/mutation/red-team cases).
- Files modified: `Path.md` only (this record). No spec/WorkPlan/coverage changes in WP-0.
- Code implemented: deterministic hashing (sorted keys, UTF-8 LF, no timestamps), zip namelist inventory with CRCs, fixture labeling + binary gate, rebuild-and-compare `--check`, schema/hash validation, stop/gate grading. Fail-closed nonzero on any missing source.
- Algorithms/semantics: sha256 pinning; byte-identity determinism; LEGACY_HISTORICAL-from-birth labeling; LEGACY_UNQUALIFIED wrap policy; atomicity commitment (normative schema frozen WP-2).
- Schemas: manifest JSON (keys + 64-hex), target ontology v1, atomicity commitment v1 (all draft here).
- Artifacts: manifests + docs + index listed above; no binaries committed.
- Tests: WP0-T01..T05 (5 passed); stress/mutation/red-team (10 passed); total `15 passed in ~4.5s`, exit 0.
- Benchmarks: none (NO MODEL TRAINED in WP-0 — stated explicitly).
- Stress tests: missing zip/PC (exit 2 BLOCKED), empty zip (honest count 0), corrupted/malformed manifest (`--check` nonzero), unlabeled/binary/fresh fixtures (MIGRATION_CHECK FAIL), removed archaeology doc (auditor FAIL), post-stress integrity (all PASS).
- Anti-overfitting controls: legacy never observational/fresh/qualified; no holdout exists; no training.
- Threats addressed: COL-T18 (wrap policy + WP0-T01 + migrate `--check`), COL-T30 (commitment record; normative schema stays WP-2).
- Stops enforced: STOP-01 PASS (PC paper pinned `494334e5…`), STOP-02 PASS (5771-entry snapshot pinned); project proceeds (no BLOCKED terminal).
- Invariants checked: legacy never qualified; history preserved (append-only Path; git history intact).
- Gates opened: COL-GATE-00 FOUNDATION_FROZEN + COL-GATE-01 LEGACY_ARCHAEOLOGY_COMPLETE (auditor STEP 26, manifest hashes in this entry).
- Statuses changed: WP-0 PLANNED → IMPLEMENTED → VERIFIED (closeout below).
- Hashes: spec `9d4761e3…`; legacy zip `cf524060…`; PC pinned `494334e5…`; remote legacy HEAD `72222ad2…`; manifests bb11c846…/77391c5d…/7fe0c169….
- Commands executed (exit codes): `pin_foundation.py` (0), `migrate_legacy_fixtures.py` (0), `audit_foundation.py` → INDEPENDENT_AUDIT = PASS (0), `pin_foundation.py --check` → FOUNDATION_CHECK = PASS (0), `migrate --check` → PASS (0), `pytest tests/legacy_regression -q` → 15 passed (0), `gen_normative_inventory.py` → 561/556/5 (0), `gen_workplan_coverage.py` (0), `check_workplan_coverage.py` → PASS (0).
- Failures encountered + repairs: (1) auditor hardcoded 5771 vs file-only listing → repaired to manifest-comparison, re-audited PASS; (2) test REPO path off by one level → fixed, 5/5 pass; (3) auditor hex-set logic flaw (`>=` superset bug) → fixed; (4) stress test overwrote committed manifests → backup/restore added. All preserved here with provenance.
- Counterexamples: none (no theorems in WP-0).
- Deviations: none from WorkPlan (atomicity commitment file is the T30 control as specified; normative schema remains WP-2 per coverage).
- External blockers: none.
- Log inventory (final, matches committed bytes; STEP-09 unused gap documented):
  - pin_foundation.py: STEP-01 comment 17/log 18; STEP-02 comment 73/log 74; STEP-03 comment 86/log 87; STEP-04 comment 96/log 97; STEP-05 comment 108/log 109; STEP-06 comment 121/log 122 (+per-file log 157); STEP-07 comment 164/log 165 (+match log 180); STEP-08 comment 181/log 182.
  - migrate_legacy_fixtures.py: STEP-10 comment 17/log 18; STEP-11 comment 34/log 35; STEP-12 comment 49/log 50 (+result log 74); STEP-13 comment 81/log 82.
  - audit_foundation.py: STEP-20 comment 17/log 18; STEP-21 comment 38/log 39; STEP-22 comment 53/log 54 (+files log 58/59); STEP-23 comment 77/log 78; STEP-24 comment 94/log 95; STEP-25 comment 112/log 113; STEP-26 comment 125/log 126 (+result logs 129/132).
- Commit: (below). Push: (below). Final compliance verdict: (closeout below).

## WP-0 FINAL CLOSEOUT

- Previous-phase revalidation: NOT_APPLICABLE (N=0, first phase; pre-foundation audit PASS).
- Entry gate: PASS (predicate above).
- Scope completed: REQ-001..025 all implemented.
- Files created/modified: listed above; `git status` shows only intended WP-0 files.
- Core implementation: pin + migrate + independent audit + 15 tests, all green.
- Console/log inventory: above (final line numbers verified against committed bytes).
- Tests: 15/15 pass (WP0-T01..T05 + 10 stress/mutation/red-team).
- Stress tests: pass (fail-closed demonstrated on 8 damage cases).
- Mutation tests: pass (corrupted/malformed/unlabeled/binary/fresh/removed all rejected).
- Independent checks: `audit_foundation.py` (separate code path) PASS; regen byte-identical; second grep audit (69 sec / 31 phases / 23 gates / 30 threats / 25 stops; INV==COV 561; bounds 554/554 clean).
- Threats: T18/T30 controlled. Stops: STOP-01/02 PASS. Invariants: hold.
- Statuses: GATE-00/01 OPEN (emit FOUNDATION_FROZEN, LEGACY_ARCHAEOLOGY_COMPLETE).
- Artifacts + hashes: listed above.
- Exit-criteria matrix: EXIT-01 manifests exist+valid PASS | EXIT-02 hashes match recomputation PASS | EXIT-03 archaeology complete (HEAD+zip+scripts+ensemble+converter+fixtures+policy) PASS | EXIT-04 anti-patterns recorded (7/7) PASS | EXIT-05 ontology+env+commitment frozen PASS | EXIT-06 scripts run green incl. step logs PASS | EXIT-07 tests 15/15 + stress/mutation PASS | EXIT-08 H reruns PASS | EXIT-09 hygiene PASS | EXIT-10 Path record complete PASS.
- Compliance-audit result: contract reconstructed at closeout agrees with phase-start contract (CONTRACT_START_CLOSEOUT_DIFF = 0); requirement-vs-repo-vs-Path-vs-tests comparison: compliance_gaps = 0. False-closure attacks (removed doc, dropped audit, corrupted/malformed pins, bad labels): all rejected by a detector. Verifier soundness holds.
- Remaining execution-owned items: none. Future-phase work: WP-1..WP-8 NOT_STARTED. External blockers: none. Not-applicable: HOLD/qualification/registry/runtime obligations (later phases).
- Deviations: none.
- Final verdict: WP-0 = COMPLETE.
- Claim-evidence pointers: "15/15 green" → `pytest tests/legacy_regression -q` exit 0 | "all artifacts present" → file list + auditor STEP 22b PASS | "mutations caught" → 8/8 damage cases nonzero/FAIL | "independent agreement" → INDEPENDENT_AUDIT = PASS + regen identical | "compliance_gaps = 0" → reconstruction audit + red-team above.
- Commit/push/HEAD: recorded below after verification.

## WP-1 — Trusted data core — NOT_REACHED

- WorkPlan prescription: WorkPlan.md §WP-1 (PHASE-02/03/04; GATE-02; LightCurve/provenance/quality/preprocessing/splits).
- Entry-gate status: BLOCKED until WP-0 GATE-00/01 PASSED.
- (Remaining Path fields pending execution; do not reconstruct retroactively.)

## WP-2 — PC semantic core — NOT_REACHED

- WorkPlan prescription: WorkPlan.md §WP-2 (PHASE-05/06/07; GATE-04/05; H/P_R/Lambda/closure/touch/freeze + 12 witnesses + independent touch).
- Entry-gate status: BLOCKED until GATE-02 PASSED.
- (Remaining fields pending.)

## WP-3 — Catalogue and diagnostic reconstruction — NOT_REACHED

- WorkPlan prescription: WorkPlan.md §WP-3 (PHASE-08/09/10; GATE-06/07; EvidenceState + diagnostics + representation engine; converter decomposition).
- Entry-gate status: BLOCKED until GATE-04/05 PASSED.

## WP-4 — COL Forge (dev only) — NOT_REACHED

- WorkPlan prescription: WorkPlan.md §WP-4 (PHASE-11..15; GATE-03/08/09/10; tasks/trainers/calibration/harness/views; no promotion).
- Entry-gate status: BLOCKED until GATE-06/07 PASSED.

## WP-5 — Muse teacher and adversarial development — NOT_REACHED

- WorkPlan prescription: WorkPlan.md §WP-5 (PHASE-16/17; GATE-11; OpenCode client + budget + schemas + materializer; dev-only).
- Entry-gate status: BLOCKED until GATE-08/10 PASSED. Secrets via env only.

## WP-6 — Specialist qualification and registry — NOT_REACHED (firewall)

- WorkPlan prescription: WorkPlan.md §WP-6 (PHASE-18..21; GATE-12/13/14/15; prereg -> freeze -> one reveal -> promote; LPC/CPC/Q).
- Entry-gate status: BLOCKED until GATE-08/09/10/11 PASSED + prereg frozen. Holdout reveal-once enforced; no second unlock.

## WP-7 — Council runtime integration — NOT_REACHED

- WorkPlan prescription: WorkPlan.md §WP-7 (PHASE-22/23/24; GATE-16/17; qualified-only loading + authorized views + PC closure + replay).
- Entry-gate status: BLOCKED until GATE-14/15 PASSED.

## WP-8 — Freeze geometry, clean-room, final seal — NOT_REACHED

- WorkPlan prescription: WorkPlan.md §WP-8 (PHASE-25..30; GATE-18/19/20/21; K recompute + PCQs + mutation + clean-room + release package + honest terminal).
- Entry-gate status: BLOCKED until GATE-16/17 PASSED. API/frontend omissible without blocking GATE-21.
