# COUNCIL-PC-v1.0 Provider Migration Audit

**Migration:** OpenRouter -> OpenCode  
**Scope:** provider-name correction only  
**Result:** `PASS`

This audit verifies that the revised implementation specification changes only the three literal provider references requested by the user. No scientific, PC, training, qualification, registry, runtime, work-package, gate, threat, stop-condition, or terminal-claim semantics were modified.

## 1. Composition table — side-by-side

| Line | Before | After | Status |
|---:|---|---|---|
| 19 | `**External teacher target:** Muse Spark 1.3 Contributor through OpenRouter, with all teacher use schema-bound, provenance-recorded, budget-capped, and excluded from unverified ground-truth authority.` | `**External teacher target:** Muse Spark 1.3 Contributor through OpenCode, with all teacher use schema-bound, provenance-recorded, budget-capped, and excluded from unverified ground-truth authority.` | PASS |
| 2071 | `OpenRouter client;` | `OpenCode client;` | PASS |
| 2338 | `OpenRouter API keys must never be committed.` | `OpenCode API keys must never be committed.` | PASS |

## 2. Structural non-regression table

| Invariant | Original | Revised | Result |
|---|---:|---:|---|
| Total lines | 2864 | 2864 | PASS |
| Markdown headings | 108 | 108 | PASS |
| Numbered top-level sections | 69 | 69 | PASS |
| Work-package headings | 9 | 9 | PASS |
| Code-fence markers | 228 | 228 | PASS |
| `\boxed{...}` occurrences | 14 | 14 | PASS |
| Remaining `OpenRouter` mentions | 3 | 0 | PASS |
| `OpenCode` mentions | 0 | 3 | PASS |
| Changed lines | 0 baseline | 3 provider-only | PASS |
| Round-trip equivalence (`OpenCode` -> `OpenRouter`) | n/a | byte-for-byte original text | PASS |

## 3. Closure matrix

| Closure obligation | Required condition | Evidence | Verdict |
|---|---|---|---|
| CLOSURE-P01 Provider target | External teacher names OpenCode rather than OpenRouter | Revised external-teacher line | PASS |
| CLOSURE-P02 Client implementation | WP-5 names OpenCode client | Revised WP-5 implementation list | PASS |
| CLOSURE-P03 Secret policy | Secret rule names OpenCode API keys | Revised secrets section | PASS |
| CLOSURE-P04 No stale provider text | No `OpenRouter` token remains anywhere in revised spec | Full-file token scan: 0 matches | PASS |
| CLOSURE-P05 Scientific semantics preserved | Every non-provider line remains identical | Exact line-by-line comparison | PASS |
| CLOSURE-P06 Section topology preserved | Same headings, section count, and WP count | Structural counts above | PASS |
| CLOSURE-P07 Markdown composition preserved | Same line count, code fences, and boxed-expression count | Structural counts above | PASS |
| CLOSURE-P08 Reversibility | Replacing `OpenCode` with `OpenRouter` reconstructs the original exactly | Round-trip comparison | PASS |
| CLOSURE-P09 PC architecture preserved | No edits to H, P_R, Lambda, touch, closure, freeze, or target semantics | Diff contains only three provider-name lines | PASS |
| CLOSURE-P10 Training/qualification preserved | No edits to Forge, SpecialistSpec, qualification, registry, model limits, or evaluation gates | Diff contains only three provider-name lines | PASS |

### Closure result

```text
PROVIDER_MIGRATION_CLOSED = PASS
REGRESSION_DETECTED = FALSE
UNRESOLVED_PROVIDER_REFERENCES = 0
CHANGED_LINES = 3
CHANGE_CLASS = LITERAL_PROVIDER_SUBSTITUTION_ONLY
```

## 4. Integrity hashes

```text
original_sha256 = a9453d20079ace95d8227d0fed095398b4aa6de1d1265f61ba6fe1b4c5dbf0fb
revised_sha256  = 766ecfaac5540be2f932bedc08a99981949aede7e32649ab33f7fa5a98908da6
```

The hashes are expected to differ because the provider name changed. The round-trip equivalence check is the non-regression certificate: replacing the three revised `OpenCode` literals back with `OpenRouter` yields text identical to the original specification.
