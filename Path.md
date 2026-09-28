# Path — COUNCIL-PC-v1.0 live execution ledger

**Experiment:** `COUNCIL-PC-v1.0` (`COL-PC-v1.0`) | **Repo:** `InfernusReal/Council-of-Lords-PC`
**Operative spec:** `IMPLEMENTATION_SPEC.md` SHA256 `766ecfaac5540be2f932bedc08a99981949aede7e32649ab33f7fa5a98908da6` (2864 lines)
**Original spec:** `audits/COUNCIL-PC-v1.0_IMPLEMENTATION_SPEC_ORIGINAL.md` SHA256 `a9453d20079ace95d8227d0fed095398b4aa6de1d1265f61ba6fe1b4c5dbf0fb`
**Migration audit:** `audits/PROVIDER_MIGRATION_AUDIT.md` PASS (OpenRouter->OpenCode, 3 lines)
**SPLAY template (non-operative, preserved):** `audits/SPLAY-AM-MST-LIQ-v0.4_SPEC.txt` SHA256 `0E2C166E1B721DFC8A7E5327ED33AF29A1B4AC539CB71849F3C7231B32A8055B` — see SPEC-CONFLICT-01 in WorkPlan.md
**Conceptual parent:** Perceptive Closure (local `Perception Closure/` + Downloads drafts; exact version pinned WP-0)
**Legacy parent:** `InfernusReal/Council-Of-Lords` + `Downloads/Council-Of-Lords-main.zip` (5771 entries, archaeological only)
**Teacher:** Muse Spark 1.3 Contributor through OpenCode, USD 25 ceiling
**Plan:** `WorkPlan.md` (9 WPs) | **Inventory:** `planning/NORMATIVE_INVENTORY.yaml` (519 items) | **Coverage:** `planning/WORKPLAN_COVERAGE.yaml` | **Checker:** `scripts/check_workplan_coverage.py`

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
- Commit SHA: (to record on planning commit below).
- Push result: (to record).
- Remote-head verification: (to record via `git ls-remote origin main`).
- WorkPlan-adherence verdict: (pending execution; planning files FOLLOWS WorkPlan.md by construction).

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
