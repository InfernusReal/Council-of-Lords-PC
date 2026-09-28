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
- Repair commit SHA: (recorded below after push). Push result: (recorded below). Remote HEAD: (verified below).
- Path verdict for this operation: FOLLOWS WorkPlan.md — PLANNING REPAIR CLOSED (pending commit/push verification).

---

## WP-0 — Foundation freeze and archaeology — PLANNED (not yet executed)

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
