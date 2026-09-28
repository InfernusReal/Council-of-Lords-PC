# WorkPlan Semantic Closure Audit — COUNCIL-PC-v1.0 planning repair

**Scope:** surgical planning-layer repair only. No WP-0 scientific execution.
**Before:** operative spec SHA256 `766ecfaac5540be2f932bedc08a99981949aede7e32649ab33f7fa5a98908da6`, 2864 lines.
**After:** operative spec SHA256 `9d4761e3cb656b0b4295a5ae4efcf08bc13058f00082577d5b92d406de1482e6`, 2983 lines (+119, Sec-15.6 doctrine only + PHASE-04 line + COL-GATE-22 line + doctrine wording line).
**Provider migration audit** (`audits/PROVIDER_MIGRATION_AUDIT.md`) untouched. Old SHA distinguished below as pre-mutation; new SHA is current.

## Composition audit (before → after)

| Structure | Before | After | Delta |
|---|---|---:|---|
| Spec lines | 2864 | 2983 | +119 |
| Numbered sections | 69 (0–68) | 69 (0–68) | 0 (15.6 is a subsection) |
| Phases | 31 (00–30) | 31 (00–30) | 0 (PHASE-04 text expanded, ID/owner unchanged) |
| Gates | 22 (00–21) | 23 (00–22) | +1 COL-GATE-22 |
| Threats / stops | 30 / 25 | 30 / 25 | 0 |
| Test classes / schemas | 14 / 17 | 14 / 17 | 0 |
| Claim items | 12 | 14 | +2 fidelity split (confidence-auth vs confidence-calib lines) |
| Dataset-source IDs | 0 | 40 (doctrine+attempt+17 fam+14 field+4 status+registry+nosilent+gate*) | +40 (*gate counted in gates row) |
| INVENTORY_ITEMS_TOTAL | 519 | 561 | +42 |
| NORMATIVE_ITEMS_TOTAL | 514 | 556 | +42 |
| NOT_APPLICABLE_ITEMS_TOTAL | 5 | 5 | 0 |
| WPs | 9 | 9 | 0 |

Changed normative structures: Sec-15.6 added; PHASE-04 text expanded; COL-GATE-22 added (owner WP-1,
spec_phase PHASE-04, re-verified WP-8); CLAIM-07 split into auth/calib lines (CLAIM-08/09) with
UNRESOLVED-guard → CLAIM-13 and no-confirmed-exoplanet → CLAIM-14; source-section corrections
HOLD-07→Sec-42, HOLD-08→Sec-40, TEACH-08→Sec-52 (all other items retain sections); doctrine wording
replaced (registry eligibility; authority licenses use); generator now section-bounded with fail-closed
anchors; checker extended (bounds invariant, counts, doctrine presence).

## Closure matrix

| # | Obligation | Evidence | Verdict |
|---|---|---|---|
| 1 | operative spec identity | `IMPLEMENTATION_SPEC.md` SHA `9d4761e3…406de1` (2983 lines) pinned in WorkPlan/Path/inventory metadata | PASS |
| 2 | provider migration preserved | migration audit untouched; operative spec has 0 `OpenRouter` lines; remaining mentions only document the historical migration | PASS |
| 3 | inventory total accounting | INVENTORY_ITEMS_TOTAL = 561 (generator-computed, deterministic) | PASS |
| 4 | normative/not-applicable accounting | NORMATIVE 556 + NOT_APPLICABLE 5 = 561; canonical terminology in WorkPlan/checker/Path | PASS |
| 5 | all numbered sections mapped | 69 SEC items, each owned (checker assertion 4) | PASS |
| 6 | all phases uniquely owned | 31 phases, exact WP table incl. PHASE-04→WP-1 (checker assertion 3) | PASS |
| 7 | all WPs preserved | 9 WPs, no restructure | PASS |
| 8 | all gates owned | 23 gates incl. COL-GATE-22→WP-1 (checker assertion 7) | PASS |
| 9 | all threats controlled | 30/30 with controls (checker assertion 9) | PASS |
| 10 | all stops handled | 25/25 with handlers (checker assertion 10) | PASS |
| 11 | PC semantic core preserved | H/P_R/Lambda/omega/A_Pi/Atom/Succ+ anchors verified in spec; Sec-4/5/9 owned WP-2 | PASS |
| 12 | touch derivation preserved | `T_s(q)=` extensional derivation + no-manual-tag law present | PASS |
| 13 | independent touch reconstruction preserved | two-derivations requirement + GATE-05 present | PASS |
| 14 | holdout firewall preserved | one-reveal rule + HOLD-01..08 mapped; reveal-after-freeze ordering enforced | PASS |
| 15 | Forge/Registry/Runtime separation preserved | WP-4 dev-only, WP-6 promotion, WP-7 licensed runtime; lifecycle checks pass | PASS |
| 16 | source-line fidelity repaired | generator uses section-bounded exact anchors, fail-closed | PASS |
| 17 | section-bounded source pointers verified | SOURCE_POINTER_ERRORS = 0 over all numbered-section items | PASS |
| 18 | exhaustive dataset doctrine present | Sec-15.6 + COL-SRC-DOCTRINE + boxed intent in spec; DATASET_SOURCE_DOCTRINE_PRESENT = TRUE | PASS |
| 19 | source registry planned | COL-SRC-REGISTRY + 17 families + 14 fields + WP-1 `source_registry.py` + registry/ledger/closure files | PASS |
| 20 | source terminal states planned | 4 states + COL-SRC-NOSILENT; exactly-one-terminal enforced by closure audit design | PASS |
| 21 | DATASET_SOURCE_COVERAGE_CLOSED present | COL-GATE-22 in spec gate ladder, inventory, coverage (WP-1, PHASE-04), WorkPlan WP-1/WP-8 | PASS |
| 22 | Phase 04 updated | registry + acquisition + ledger + reconciliation + closure audit in spec line, inventory description, WorkPlan WP-1, coverage spec_phase | PASS |
| 23 | WP-1 ownership updated | WP-1 owns PHASE-04, GATE-02/22, all 40 dataset-source IDs | PASS |
| 24 | qualification-vs-authority wording corrected | registry-eligibility wording in spec Sec-68 + WorkPlan header/WP-6/WP-7; old wording absent from operative spec | PASS |
| 25 | no stale OpenRouter outside historical context | operative spec 0 hits; planning files only reference the migration audit event | PASS |
| 26 | no regression in gates/lifecycle ordering | GATE-21 still terminal; GATE-22 append-only; reveal→promote→seal→runtime order intact; all PC/teacher/hardware/vote/LLM/successor anchors present | PASS |

## Machine-readable closure block

```text
INVENTORY_ITEMS_TOTAL = 561
NORMATIVE_ITEMS_TOTAL = 556
NOT_APPLICABLE_ITEMS_TOTAL = 5
UNMAPPED_NORMATIVE_ITEMS = 0
SOURCE_POINTER_ERRORS = 0
PHASE_OWNERSHIP_ERRORS = 0
GATE_ERRORS = 0
THREAT_CONTROL_ERRORS = 0
STOP_CONTROL_ERRORS = 0
HOLDOUT_ORDER_ERRORS = 0
DATASET_SOURCE_DOCTRINE_PRESENT = TRUE
DATASET_SOURCE_COVERAGE_GATE_PRESENT = TRUE
REGRESSION_DETECTED = FALSE
WORKPLAN_SEMANTIC_CLOSURE = PASS
```
