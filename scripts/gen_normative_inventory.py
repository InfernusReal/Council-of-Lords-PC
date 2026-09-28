"""Deterministic generator for planning/NORMATIVE_INVENTORY.yaml.

Reads IMPLEMENTATION_SPEC.md (operative spec) and derives every normative
item with section-bounded source pointers.

Fidelity contract (planning repair):
- Every item from a numbered spec section declares source_section Sec-N.
- The source-line lookup is bounded to that section's line range
  (heading line .. next heading line - 1). Global fallback is forbidden.
- Anchors are exact/full phrases from the declared section.
- The generator FAILS (nonzero exit) if a required anchor cannot be found
  inside its declared section. It never silently emits line 0 or an
  unrelated line for a numbered-section item.
- Output ordering is deterministic (fixed insertion order).

Source-section corrections applied during repair (documented, not silent):
- HOLD-07 -> Sec-42 (the no-relabel sentence lives in Sec-42, not Sec-41).
- HOLD-08 -> Sec-40 (the legacy-fixture freshness bar lives in Sec-40).
- TEACH-08 -> Sec-52 (secret hygiene lives in Sec-52, not Sec-29).
All other items retain their previously declared sections.
"""
import pathlib, re, hashlib, sys

SPEC = pathlib.Path("IMPLEMENTATION_SPEC.md")
OUT = pathlib.Path("planning/NORMATIVE_INVENTORY.yaml")
text = SPEC.read_text(encoding="utf-8")
lines = text.splitlines()
sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

# --- numbered-section line bounds: {N: (start, end)} inclusive ---
bounds = {}
_heads = []
for i, l in enumerate(lines, 1):
    m = re.match(r"# (\d+)\.\s", l)
    if m:
        _heads.append((int(m.group(1)), i))
_heads.sort()
for idx, (num, ln) in enumerate(_heads):
    end = _heads[idx + 1][1] - 1 if idx + 1 < len(_heads) else len(lines)
    bounds[num] = (ln, end)

def sec_num(source_section):
    m = re.fullmatch(r"Sec-(\d+)", source_section)
    return int(m.group(1)) if m else None

def find_in_section(phrase, source_section, item_id):
    """Bounded lookup. Fails loudly if absent from the declared section."""
    n = sec_num(source_section)
    if n is None:
        raise SystemExit(
            f"FIDELITY-FAIL {item_id}: source_section '{source_section}' is not "
            f"a numbered section; numbered-section items require Sec-N")
    if n not in bounds:
        raise SystemExit(f"FIDELITY-FAIL {item_id}: section {n} not found in spec")
    s, e = bounds[n]
    for ln in range(s, e + 1):
        if phrase in lines[ln - 1]:
            return ln
    raise SystemExit(
        f"FIDELITY-FAIL {item_id}: anchor {phrase!r} not found in "
        f"Sec-{n} lines {s}-{e}")

items = []

def add(item_id, category, source_section, anchor, description, status="normative"):
    n = sec_num(source_section)
    if status == "normative" and n is not None:
        ln = find_in_section(anchor, source_section, item_id)
    elif status == "normative":
        # normative item outside numbered sections (process rule): pin to line 1 explicitly
        ln = 1
    else:
        ln = 0
    items.append({
        "id": item_id, "category": category, "source_section": source_section,
        "source_file": "IMPLEMENTATION_SPEC.md", "source_line": ln,
        "source_anchor": anchor, "description": description, "status": status,
    })

def add_sec(n, title, ln):
    items.append({"id": f"SEC-{n:02d}", "category": "spec_section",
        "source_section": f"Sec-{n}", "source_file": "IMPLEMENTATION_SPEC.md",
        "source_line": ln, "source_anchor": f"# {n}.",
        "description": f"Spec section {n}: {title}", "status": "normative"})

# --- 0. Spec sections SEC-00..SEC-68 (69 items; source_line = heading line) ---
titles = {}
for i, l in enumerate(lines, 1):
    m = re.match(r"# (\d+)\.\s+(.*)", l)
    if m:
        titles[int(m.group(1))] = (m.group(2).strip(), i)
for n in range(0, 69):
    title, ln = titles.get(n, (f"section-{n}", 0))
    if ln == 0:
        raise SystemExit(f"FIDELITY-FAIL SEC-{n:02d}: heading '# {n}.' missing")
    add_sec(n, title, ln)

# --- PHASES 00..30 (31), Sec-47 ---
for n in range(0, 31):
    add(f"PHASE-{n:02d}", "phase", "Sec-47", f"PHASE {n:02d}",
        f"Normative phase {n:02d} per phase map")

# --- Work packages WP-0..WP-8 (9), Sec-46 ---
for n in range(0, 9):
    add(f"WP-{n}", "work_package", "Sec-46", f"## WP-{n}",
        f"Work package WP-{n} per Sec-46")

# --- Gates COL-GATE-00..22 (23), Sec-48 ---
gate_names = {
 0: "FOUNDATION_FROZEN", 1: "LEGACY_ARCHAEOLOGY_COMPLETE", 2: "DATA_CORE_CERTIFIED",
 3: "DATASET_FACTORY_CERTIFIED", 4: "PC_CORE_CERTIFIED", 5: "TOUCH_DERIVATION_INDEPENDENT_AGREEMENT",
 6: "CATALOGUE_ENGINE_CERTIFIED", 7: "REPRESENTATION_ENGINE_CERTIFIED", 8: "FORGE_OPERATIONAL",
 9: "CALIBRATION_PIPELINE_CERTIFIED", 10: "QUALIFICATION_HARNESS_CERTIFIED", 11: "TEACHER_PIPELINE_CERTIFIED",
 12: "SPECIALIST_CANDIDATE_SET_FROZEN", 13: "FRESH_HOLDOUT_REVEALED_ONCE", 14: "INITIAL_LORDS_QUALIFIED",
 15: "REGISTRY_SEALED", 16: "COUNCIL_RUNTIME_CERTIFIED", 17: "RESOURCE_VIEW_AUDIT_PASSED",
 18: "PC_FREEZE_GEOMETRY_RECOMPUTED", 19: "MUTATION_SUITE_PASSED", 20: "CLEANROOM_REPRODUCTION_PASSED",
 21: "PC_NATIVE_COUNCIL_QUALIFIED", 22: "DATASET_SOURCE_COVERAGE_CLOSED"}
for n, nm in gate_names.items():
    add(f"COL-GATE-{n:02d}", "gate", "Sec-48", f"COL-GATE-{n:02d}",
        f"Gate {nm}")

# --- Threats COL-T01..30, Sec-44 ---
for n in range(1, 31):
    add(f"COL-T{n:02d}", "threat", "Sec-44", f"COL-T{n:02d}",
        f"Threat COL-T{n:02d} per threat matrix")

# --- Stops COL-STOP-01..25, Sec-45 ---
for n in range(1, 26):
    add(f"COL-STOP-{n:02d}", "stop", "Sec-45", f"COL-STOP-{n:02d}",
        f"Stop COL-STOP-{n:02d}")

# --- Test classes (14, Sec-54): full lines with punctuation ---
tests = ["unit tests;", "property tests;", "schema tests;", "provenance tests;",
 "leakage tests;", "model-interface tests;", "calibration tests;",
 "registry integrity tests;", "PC semantic tests;", "touch derivation tests;",
 "freeze tests;", "mutation tests;", "legacy regression tests;",
 "clean-room reproduction tests."]
for i, anchor in enumerate(tests, 1):
    add(f"TEST-{i:02d}", "test_class", "Sec-54", anchor,
        f"Test class: {anchor}")

# --- Schemas (17, Sec-66) ---
schemas = ["LightCurveSchema", "EvidenceStateSchema", "RepresentationSchema",
 "AuthoritySchema", "ActionSchema", "CheckpointSchema", "SpecialistResultSchema",
 "TaskSpecSchema", "SpecialistSpecSchema", "DatasetManifestSchema",
 "RunManifestSchema", "QualificationReportSchema", "CapabilityMapSchema",
 "RegistryEntrySchema", "TeacherTransactionSchema", "CouncilTraceSchema",
 "FreezeResultSchema"]
for i, nm in enumerate(schemas, 1):
    add(f"SCHEMA-{i:02d}", "schema", "Sec-66", nm,
        f"Schema v1 to freeze: {nm}")

# --- Terminal outcomes (10, Sec-63) ---
terms = ["PC_NATIVE_COUNCIL_QUALIFIED", "QUALIFIED_WITH_DECLARED_LIMITATIONS",
 "FORGE_QUALIFIED_RUNTIME_BLOCKED", "PC_SEMANTICS_UNDERIDENTIFIED",
 "SPECIALIST_QUALIFICATION_FAILED", "DATASET_INTEGRITY_FAILED",
 "HOLDOUT_CONTAMINATED", "TEACHER_BUDGET_EXHAUSTED", "RESOURCE_LIMIT_REACHED",
 "ARCHITECTURE_SUCCESSOR_REQUIRED"]
for i, nm in enumerate(terms, 1):
    add(f"TERM-{i:02d}", "terminal_outcome", "Sec-63", nm,
        f"Terminal state: {nm}")

# --- Release artifacts (19, Sec-51): full names ---
arts = ["RELEASE_MANIFEST.json", "SOURCE_COMMIT.txt", "ENVIRONMENT_LOCK",
 "DATASET_MANIFESTS", "TASK_SPECS", "SPECIALIST_SPECS", "REGISTRY_MANIFEST.json",
 "QUALIFICATION_REPORTS", "PC_CONTRACT.json", "ACTION_SCHEMA.json",
 "ATOMICITY_SCHEMA.json", "TOUCH_RECOMPUTATION.json", "FREEZE_RESULTS.json",
 "MUTATION_RESULTS.json", "TEACHER_BUDGET_LEDGER.json",
 "TEACHER_PROVENANCE_MANIFEST.json", "LEGACY_ARCHAEOLOGY.md", "FINAL_AUDIT.md",
 "FINAL_RESULT.json"]
for i, nm in enumerate(arts, 1):
    add(f"ART-{i:02d}", "release_artifact", "Sec-51", nm,
        f"Release package artifact: {nm}")

# --- Evaluation labels (9, Sec-42) ---
labels = ["LEGACY_HISTORICAL", "DEVELOPMENT", "INTERNAL_VALIDATION",
 "TEACHER_GENERATED_DEVELOPMENT", "CONTAMINATED_CANARY",
 "FRESH_QUALIFICATION_HOLDOUT", "CLEANROOM_POST_FREEZE",
 "FORMAL_PC_CONSTRUCTED", "OBSERVATIONAL_EXTERNAL_TEST"]
for i, nm in enumerate(labels, 1):
    add(f"LABEL-{i:02d}", "eval_label", "Sec-42", nm,
        f"Evaluation row label: {nm}")

# --- Dataset source classes (9, Sec-15.1 fence) ---
dcls = ["OBSERVATIONAL_RAW", "OBSERVATIONAL_DERIVED", "CATALOG_LABELLED",
 "SIMULATED_PHYSICS", "SYNTHETIC_STRESS", "LLM_PROPOSED_SCENARIO",
 "LEGACY_HISTORICAL", "CONTAMINATED_DEVELOPMENT", "HIDDEN_HOLDOUT"]
for i, nm in enumerate(dcls, 1):
    add(f"DCLASS-{i:02d}", "dataset_class", "Sec-15", nm,
        f"Dataset source class: {nm}")

# --- Label confidence (7, Sec-15.4 fence) ---
lconf = ["CONFIRMED", "HIGH_CONFIDENCE", "CATALOG_CANDIDATE",
 "KNOWN_FALSE_POSITIVE", "SIMULATED_KNOWN", "AMBIGUOUS", "UNRESOLVED"]
for i, nm in enumerate(lconf, 1):
    add(f"LCONF-{i:02d}", "label_confidence", "Sec-15", nm,
        f"Label confidence: {nm}")

# --- Mutation controls (21, Sec-43): full mutant lines ---
mutants = [
 "raw scratch field silently admitted into H;",
 "representation flag changes without P_R change;",
 "P_R changes but touch omits R;",
 "authority changes action availability without Lambda change;",
 "manual touch label overrides derived touch;",
 "freeze removes only part of a mixed source-atomic action;",
 "hidden label leaked into controller observation;",
 "holdout row appears in training identity group;",
 "model trained with forbidden evidence;",
 "registry model bytes changed under same version;",
 "calibration file from another model version;",
 "capability map attached to wrong artifact;",
 "unqualified model loaded as qualified;",
 "teacher output accepted as observational ground truth;",
 "teacher prompt contains hidden holdout outcome;",
 "synthetic provenance dropped;",
 "solar-default fallback presented as measured stellar data;",
 "legacy fixed specialist weights reintroduced;",
 "majority vote bypasses closure;",
 "red flag directly subtracts arbitrary verdict score;",
 "API/frontend mutates scientific state outside engine;"]
for i, anchor in enumerate(mutants, 1):
    add(f"MUT-{i:02d}", "mutation_control", "Sec-43", anchor,
        f"Semantic mutant: {anchor}")

# --- Adversarial corpus families (20, Sec-40): full lines ---
adv = ["clean planetary transits;", "grazing eclipsing binaries;",
 "detached eclipsing binaries;", "contact binaries;",
 "diluted/blended binaries;", "stellar activity;", "rotational variability;",
 "instrument artifacts;", "period aliases;", "secondary eclipses;",
 "very low SNR candidates;", "two-transit sparse events;",
 "long-period candidates;", "strong data gaps;", "centroid contamination;",
 "contradictory stellar metadata;", "OOD catalogue values;",
 "OOD light-curve morphology;", "calibration-edge cases;",
 "specialist disagreement cases."]
for i, anchor in enumerate(adv, 1):
    add(f"ADV-{i:02d}", "adversarial_family", "Sec-40", anchor,
        f"Adversarial corpus family: {anchor}")

# --- PC evaluation questions (8, Sec-36): full lines ---
pcq = ["Can closure occur without new evidence admission?",
 "Can closure occur without representation refinement?",
 "Can closure occur without authority-changing actions?",
 "Does removing external stellar evidence create finite fallback or structural failure?",
 "Can morphology diagnostics substitute for additional evidence?",
 "Does a learned specialist reduce closure cost without becoming structurally necessary?",
 "Can two behaviorally similar pipelines have different resource dependence under different anchors?",
 "Does the runtime refuse unique resource attribution when H/P_R/Lambda/Atom are underidentified?"]
for i, anchor in enumerate(pcq, 1):
    add(f"PCQ-{i:02d}", "pc_eval_question", "Sec-36", anchor,
        f"PC evaluation question: {anchor}")

# --- Red-flag diagnostics (15, Sec-39): full lines ---
diags = ["V/U morphology;", "odd/even depth asymmetry;", "secondary eclipse;",
 "period harmonics and aliases;", "transit-duration consistency;",
 "stellar-radius/depth consistency;", "centroid shift;",
 "neighbor contamination;", "mission systematic-period coincidence;",
 "strong stellar variability;", "low effective SNR;",
 "insufficient transit count;", "severe cadence gaps;", "model OOD;",
 "cross-specialist semantic disagreement."]
for i, anchor in enumerate(diags, 1):
    add(f"DIAG-{i:02d}", "diagnostic", "Sec-39", anchor,
        f"Red-flag diagnostic: {anchor}")

# --- Action vocabulary (25, Sec-10) ---
acts = ["LOAD_LIGHTCURVE", "APPLY_QUALITY_MASK", "NORMALIZE_FLUX",
 "DETREND_VARIANT", "SEARCH_PERIOD_BLS", "SEARCH_PERIOD_ALTERNATE",
 "FOLD_PERIOD", "FIT_TRANSIT_SHAPE", "COMPUTE_ODD_EVEN",
 "SEARCH_SECONDARY_ECLIPSE", "COMPUTE_VARIABILITY",
 "COMPUTE_CENTROID_DIAGNOSTICS", "QUERY_STELLAR_CATALOG",
 "QUERY_NEIGHBOR_CATALOG", "ESTIMATE_DILUTION", "RUN_MORPHOLOGY_LORD",
 "RUN_PERIODICITY_LORD", "RUN_FALSE_POSITIVE_LORD", "RUN_STELLAR_LORD",
 "RUN_INSTRUMENT_LORD", "RUN_GENERAL_VETTER", "REFINE_REPRESENTATION",
 "REQUEST_ADDITIONAL_SECTOR", "ESCALATE_HUMAN", "STOP_UNRESOLVED"]
for i, nm in enumerate(acts, 1):
    add(f"ACT-{i:02d}", "action_vocab", "Sec-10", nm,
        f"Action vocabulary entry: {nm}")

# --- Lord roster (6, Sec-12): backticked table names ---
lords = ["`MorphologyLord`", "`PeriodicityLord`", "`FalsePositiveLord`",
 "`StellarPlausibilityLord`", "`InstrumentLord`", "`GeneralVetter`"]
for i, anchor in enumerate(lords, 1):
    add(f"LORD-{i:02d}", "lord_roster", "Sec-12", anchor,
        f"Initial roster lord: {anchor.strip(chr(96))}")

# --- CLI commands (18, Sec-55) ---
clis = ["col data ingest", "col data build", "col data audit",
 "col task validate", "col train run", "col train search", "col calibrate",
 "col qualify", "col registry verify", "col registry list",
 "col teacher generate", "col teacher audit", "col council analyze",
 "col council replay", "col pc touch", "col pc close", "col pc freeze",
 "col audit full"]
for i, nm in enumerate(clis, 1):
    add(f"CLI-{i:02d}", "cli_command", "Sec-55", nm, f"CLI command: {nm}")

# --- Final audit questions (15, Sec-67): full lines ---
aq = ["Can every qualified model be traced to exact training data and code?",
 "Can every dataset row be traced to a source class and protected identity?",
 "Can every runtime feature be traced to admitted evidence?",
 "Can every specialist input be proven authorized by its view?",
 "Can every E/R/A touch be independently recomputed?",
 "Can every representation refinement be traced to a declared diagnostic/action?",
 "Can every authority change be traced to Lambda?",
 "Can every closed verdict be recomputed from the frozen target and represented compatible worlds?",
 "Can every open state be shown not to bypass closure?",
 "Can every teacher-derived artifact be distinguished from ground truth?",
 "Can every holdout claim be shown uncontaminated?",
 "Can every registry artifact be byte-verified?",
 "Can the system run without the frontend?",
 "Can the scientific core run without an LLM at inference time?",
 "Can the final release be replayed from its manifests?"]
for i, anchor in enumerate(aq, 1):
    add(f"AUDQ-{i:02d}", "audit_question", "Sec-67", anchor,
        f"Final audit question: {anchor}")
# --- Lord promotion criteria (16, Sec-61): full lines ---
lpc = ["TaskSpec is frozen;", "input schema is frozen;",
 "allowed/forbidden evidence is frozen;",
 "dataset and split manifests are frozen;",
 "protected-identity leakage is zero;", "training is reproducible;",
 "calibration requirement passes;", "abstention requirement passes;",
 "OOD/applicability requirement passes;",
 "role-specific stress suite passes;",
 "fresh qualification holdout requirement passes;",
 "capability map is generated;", "known failure regions are disclosed;",
 "artifact bytes are hashed;", "registry package verifies cleanly;",
 "no hidden teacher dependency exists at runtime unless explicitly declared."]
for i, anchor in enumerate(lpc, 1):
    add(f"LPC-{i:02d}", "promotion_criterion", "Sec-61", anchor,
        f"Lord promotion criterion: {anchor}")

# --- Council promotion criteria (10, Sec-62): full lines ---
cpc = ["all loaded Lords are registry-qualified;", "PC target is frozen;",
 "H/P_R/Lambda semantics are frozen;", "action/atomicity boundary is frozen;",
 "independent touch derivation agrees;",
 "controller is deterministic or fully seed-bound;",
 "all resource views enforce allowed evidence;",
 "open states cannot emit authoritative closed verdicts;",
 "mutation controls pass;",
 "replay is deterministic under declared conditions."]
for i, anchor in enumerate(cpc, 1):
    add(f"CPC-{i:02d}", "promotion_criterion", "Sec-62", anchor,
        f"Council promotion criterion: {anchor}")

# --- PC semantic obligations (20): exact anchors in declared sections ---
pcobl = [
 ("PC-H", "Sec-6",
  "Only an explicit source-atomic evidence-admission action may add or change the admitted history.",
  "Admitted evidence history H with admission-only mutation"),
 (r"PC-PR", "Sec-7", r"P_R\rightarrow P_R'",
  "Certificate/representation relation P_R refinement"),
 ("PC-LAMBDA", "Sec-8", "Authority is extensional.",
  "Epistemic authority Lambda extensional licensing"),
 ("PC-OMEGA", "Sec-4", "omega_t   controller-visible observation;",
  "Controller observation omega without hidden leakage"),
 (r"PC-TARGET", "Sec-4", r"A_\Pi:X\rightarrow D.",
  "Sealed vetting target A_Pi over D"),
 (r"PC-COMPAT", "Sec-5", r"C_R(s)=\{x:",
  "Represented compatible-world set C_R"),
 (r"PC-CLOSURE", "Sec-5", r"|\{A_\Pi(x):x\in C_R(s)\}|=1.",
  "Target-relative closure |{A(x)}|=1, no vote bypass"),
 ("PC-ADMIT", "Sec-6", "Raw availability is not admission.",
  "Source-atomic admission rule; raw availability != admission"),
 ("PC-NOFALLBACK", "Sec-6", "source=DECLARED_DEFAULT",
  "No silent solar-default fallback; DECLARED_DEFAULT with uncertainty"),
 ("PC-TOUCH", "Sec-9", "T_s(q)=",
  "Extensional touch derivation T_s(q), no manual E/R/A"),
 ("PC-ATOM", "Sec-9", "A freeze never invents a partial action",
  "Source atomicity Atom; freezes never split mixed actions"),
 ("PC-SUCC", "Sec-9", "positive-support successor",
  "Positive-support successors Succ+ semantics"),
 (r"PC-COST", "Sec-34", r"c(q)\ge 0.",
  "Nonnegative action cost c(q) with unit-cost convention declared"),
 (r"PC-KAPPA", "Sec-35", r"\kappa_\Pi(s)",
  "Closure cost kappa and freeze signature K over 8 freezes"),
 ("PC-IDENT", "Sec-37", "BOUNDARY_UNDERIDENTIFIED",
  "Identification gate; BOUNDARY_UNDERIDENTIFIED if touch underidentified"),
 ("PC-INDTOUCH", "Sec-38", "two differently structured touch derivations",
  "Independent touch reconstruction agreement gate"),
 (r"PC-VIEWS", "Sec-28", r"x_i^{(v)}=View_v(H,P_R,\Lambda).",
  "Authorized PC resource views View_v(H,P_R,Lambda)"),
 (r"PC-RELIAB", "Sec-25", r"r_i(s)=f_i(",
  "State-dependent reliability r_i(s), no fixed 1.4x weights"),
 ("PC-REPORT", "Sec-56", "EvidenceState hash chain;",
  "Runtime report with hash chain, touch, authority, cost, replay"),
 ("PC-CONTROLLER", "Sec-33",
  "The controller chooses among legal source-atomic actions.",
  "Controller legality: no holdout peek, no forbidden evidence, no closure override")]
for oid, sec, anchor, desc in pcobl:
    add(oid, "pc_obligation", sec, anchor, desc)

# --- PC sanity witnesses (12, Sec-46 WP-2 fence): full lines ---
wit = ["pure E action;", "pure R action;", "pure A action;",
 "mixed ER action;", "mixed EA action;", "mixed RA action;",
 "mixed ERA action;", "open state;", "closed state;",
 "R-freeze finite fallback;", "R-freeze structural failure;",
 "boundary-underidentified fixture."]
for i, anchor in enumerate(wit, 1):
    add(f"WIT-{i:02d}", "pc_witness", "Sec-46", anchor,
        f"PC finite sanity witness: {anchor}")

# --- Qualification Q components (7, Sec-23): exact LaTeX ---
for i, nm in enumerate([r"Q_{general}", r"Q_{calibration}", r"Q_{stress}",
                        r"Q_{OOD}", r"Q_{leakage}", r"Q_{reproducibility}",
                        r"Q_{semantic}"], 1):
    add(f"Q-{i:02d}", "qualification_gate", "Sec-23", nm,
        f"Qualification component: {nm}")

# --- Holdout / firewall rules ---
add("HOLD-01", "holdout_rule", "Sec-41",
    "freeze a new qualification holdout",
    "Freeze hidden holdout before final promotion; inaccessible to fitting/search/thresholds/teacher/repair")
add("HOLD-02", "holdout_rule", "Sec-41",
    "One reveal per qualification campaign",
    "One reveal per qualification campaign; after reveal bank becomes historical")
add("HOLD-03", "holdout_rule", "Sec-41", "requires a new hidden bank",
    "New major campaign requires new hidden bank")
add("HOLD-04", "holdout_rule", "Sec-41", "model fitting;",
    "No holdout row in training identity group (object-level split; holdout barred from model fitting)")
add("HOLD-05", "holdout_rule", "Sec-41", "threshold search;",
    "No post-hoc threshold tuning on holdout")
add("HOLD-06", "holdout_rule", "Sec-41",
    "representation-rule tuning based on holdout residual",
    "No post-hoc representation tuning on holdout")
# Fidelity corrections: the stating sentences live in Sec-42 / Sec-40.
add("HOLD-07", "holdout_rule", "Sec-42",
    "No historical result may be relabeled fresh.",
    "No historical result relabeled fresh")
add("HOLD-08", "holdout_rule", "Sec-40",
    "and cannot serve as fresh holdout evidence.",
    "Legacy fixtures only LEGACY_HISTORICAL, never fresh holdout")

# --- Teacher rules ---
add("TEACH-01", "teacher_rule", "Sec-29",
    "is the default external teacher for v1.0 development",
    "Muse Spark via OpenCode; schema-bound, provenance-recorded, budget-capped, no ground-truth authority")
add("TEACH-02", "teacher_rule", "Sec-29",
    "must pass a versioned JSON schema",
    "Structured output only for machine ingestion (versioned JSON schema)")
add("TEACH-03", "teacher_rule", "Sec-29",
    "Every teacher transaction records:",
    "Every transaction records model/provider/route/prompt_hash/input_hash/schema/params/response_hash/validation/cost")
add("TEACH-04", "teacher_rule", "Sec-29", "USD 25.00",
    "Budget USD 25 default ceiling; fail closed before exceeding")
add("TEACH-05", "teacher_rule", "Sec-29", "adversarial scenario generation;",
    "Scenario-constraints pattern: proposal->schema->materializer->synthetic provenance, never observational")
add("TEACH-06", "teacher_rule", "Sec-29", "failure-cluster interpretation;",
    "Failure discovery requires deterministic criterion/statistical separation/new test family/physical check/human rationale")
add("TEACH-07", "teacher_rule", "Sec-29",
    "but may not be machine-ingested as a label without conversion and validation",
    "No teacher-derived artifact as runtime ground truth unless declared")
# Fidelity correction: secret hygiene lives in Sec-52.
add("TEACH-08", "teacher_rule", "Sec-52", "must never be committed",
    "Secrets: .env ignored, no keys in logs/traces, scrubbed provider responses")

# --- Claim restrictions / non-goals: full Sec-2 lines (12) + Sec-4/Sec-56 guards ---
claims = [
 "five specialists are optimal;",
 "more specialists are always better;",
 "neural networks are required;",
 "large models are required;",
 "LLMs should participate in runtime classification;",
 "Muse Spark output is ground truth;",
 "weighted voting is an acceptable closure rule;",
 "classifier confidence is authorization;",
 "classifier confidence is calibrated probability;",
 "a red flag should subtract a fixed scalar penalty;",
 "finite benchmark success identifies a universal scientific guarantee;",
 "PC E/R/A is a universal ontology for astronomy;"]
for i, anchor in enumerate(claims, 1):
    add(f"CLAIM-{i:02d}", "claim_policy", "Sec-2", anchor,
        f"Non-goal / forbidden claim: {anchor}")
add("CLAIM-13", "claim_policy", "Sec-4",
    "It must not be used to conceal failure to compute closure.",
    "UNRESOLVED must not conceal failure to compute closure")
add("CLAIM-14", "claim_policy", "Sec-56",
    "It must not present a closed target class",
    "Closed verdict must not be presented as confirmed exoplanet")

# --- Hygiene / successor / reproducibility / secrets ---
add("HYG-01", "hygiene", "Sec-49",
    "The old repository is mined, not ported wholesale.",
    "Legacy mined not ported wholesale; preserve list per Sec-49.1")
add("HYG-02", "hygiene", "Sec-49",
    "## 49.2 Do not preserve as normative implementation",
    "Do-not-preserve list per Sec-49.2")
add("HYG-03", "hygiene", "Sec-49", "LEGACY_UNQUALIFIED",
    "Historical models wrapped LEGACY_UNQUALIFIED for regression only")
add("HYG-04", "hygiene", "Sec-65",
    "Use manifests and an external artifact strategy where appropriate.",
    "Clean-room repository layout per Sec-65; large artifacts via manifests not casual git")
add("HYG-05", "hygiene", "Sec-65",
    "should not be committed casually to ordinary Git history.",
    "Large raw/run/model binaries not committed casually")
add("REPRO-01", "reproducibility", "Sec-51",
    "Every release-level artifact must be hash-addressable.",
    "Every release artifact hash-addressable")
add("REPRO-02", "reproducibility", "Sec-51",
    "Failed qualification attempts and negative results are preserved.",
    "Failed/negative results preserved, no rewritten success narrative")
add("REPRO-03", "reproducibility", "Sec-13",
    "requires more than 4 GB VRAM under its frozen training configuration",
    "Default roster trains within 4GB VRAM; exception needs versioned justification")
add("SECRET-01", "secret", "Sec-52", ".env ignored;",
    "Secrets via env/manager; .env ignored; .env.example names only")
add("SECRET-02", "secret", "Sec-52", "no API keys in logs;",
    "No keys/headers in logs/traces; scrubbed storage; hashes separate from credentials")
add("SUCC-01", "successor_rule", "Sec-64",
    "1. preserve the failed architecture;",
    "Successor rule: preserve architecture+witness, diagnose, seal, version, add only justified change")
add("SUCC-02", "successor_rule", "Sec-64",
    "No new coordinate is silently inserted into the existing release.",
    "No new coordinate silently inserted into existing release")
add("COMMIT-01", "commit_rule", "process", "",
    "Every completed WP: VERIFY->UPDATE Path.md->COMPLIANCE AUDIT->COMMIT->PUSH->VERIFY REMOTE HEAD")
add("AUDIT-LEGACY-01", "parent_import", "Sec-46", "legacy repository commit;",
    "WP-0 pins legacy commit/README/scripts/ensemble/converter/fixtures + PC paper + spec + threats + ontology + env")
add("ANTI-01", "anti_pattern", "Sec-50",
    "are largely parallel neural classifiers over the same eight catalogue-style features.",
    "Anti-pattern ledger entry: parallel classifiers over same 8 features")
add("ANTI-02", "anti_pattern", "Sec-50",
    "are often encoded through altered losses, layer widths, thresholds, or class weights",
    "Anti-pattern: specialties via losses/widths/thresholds not views")
add("ANTI-03", "anti_pattern", "Sec-50",
    "The ensemble applies hard-coded specialist weights",
    "Anti-pattern: hard-coded weights and boosts/penalties")
add("ANTI-04", "anti_pattern", "Sec-50", "The converter bundles catalog lookup,",
    "Anti-pattern: monolithic converter bundling")
add("ANTI-05", "anti_pattern", "Sec-50",
    "but are still synthetic draws.",
    "Anti-pattern: synthetic draws presented via NASA ranges")
add("ANTI-06", "anti_pattern", "Sec-50",
    "are valuable as historical adversarial ideas.",
    "Valuable historical adversarial ideas preserved as LEGACY_HISTORICAL")
add("ANTI-07", "anti_pattern", "Sec-50",
    "The repository tracks generated caches,",
    "Anti-pattern: caches/checkpoints/deps/datasets tracked together")

# --- Exhaustive dataset-source doctrine (39 new normative IDs, Sec-15.6) ---
add("COL-SRC-DOCTRINE", "source_doctrine", "Sec-15",
    "Acquire broadly, provenance everything, train selectively, test brutally.",
    "Exhaustive-by-default acquisition doctrine: acquire broadly, provenance everything, train selectively, test brutally")
add("COL-SRC-ATTEMPT", "source_attempt_list", "Sec-15",
    "These are source families to attempt, not assertions",
    "Public source families to attempt without asserting availability; record actual status at execution")
src_fams = ["OBSERVATIONAL_LIGHTCURVE", "PLANET_CANDIDATE_CATALOG",
 "CONFIRMED_PLANET_CATALOG", "CERTIFIED_FALSE_POSITIVE",
 "ECLIPSING_BINARY_CATALOG", "TCE_CATALOG", "ROBOVETTER_METRICS",
 "CENTROID_DIAGNOSTICS", "STELLAR_CATALOG",
 "NEIGHBOR_CONTAMINATION_CATALOG", "INJECTION_RECOVERY",
 "SCRAMBLED_FALSE_ALARM", "INVERTED_FALSE_ALARM", "PIPELINE_SYSTEMATIC",
 "SIMULATED_PHYSICS", "TEACHER_PROPOSED_ADVERSARIAL", "LEGACY_HISTORICAL"]
for i, nm in enumerate(src_fams, 1):
    add(f"COL-SRC-FAM-{i:02d}", "source_family", "Sec-15", nm,
        f"Required frozen-registry source family: {nm}")
src_fields = ["source_id", "source_family", "source_version_or_release",
 "retrieval_date", "retrieval_method", "license_or_usage_status",
 "raw_hashes", "object_identity_mapping", "label_semantics", "known_biases",
 "allowed_tasks", "split_restrictions", "acquisition_status",
 "acquisition_failure_reason"]
for i, nm in enumerate(src_fields, 1):
    add(f"COL-SRC-FIELD-{i:02d}", "source_registry_field", "Sec-15", nm,
        f"Frozen source-registry entry field: {nm}")
src_states = ["INGESTED", "INCOMPATIBLE_WITH_DOCUMENTED_REASON",
 "UNAVAILABLE_WITH_ARCHIVED_FAILURE", "EXCLUDED_BY_FROZEN_POLICY"]
for i, nm in enumerate(src_states, 1):
    add(f"COL-SRC-STATUS-{i:02d}", "source_status", "Sec-15", nm,
        f"Terminal acquisition state: {nm}; no silent omission")
add("COL-SRC-REGISTRY", "source_registry", "Sec-15",
    "frozen source registry",
    "Frozen public-source registry + status ledger + identity reconciliation + acquisition closure audit, hash-bound")
add("COL-SRC-NOSILENT", "source_doctrine", "Sec-15",
    "No silent omission is allowed.",
    "No silent omission: unattempted/unentered/non-terminal source is a coverage failure")

# --- MST template residue: explicitly NOT_APPLICABLE (SPEC_CONFLICT-01) ---
mst_na = [
 ("MST-LIQ0-NA", "liquidity_obligation",
  "SPLAY template LIQ0-* has no Council counterpart; Council tracks activation via PC views/diagnostics, not rho"),
 ("MST-MST0-NA", "theorem_obligation",
  "SPLAY MST0-* transfer theorems have no Council counterpart; Council theorems are PC closure/freeze/diagnostic obligations"),
 ("MST-CAND-NA", "candidate_identity",
  "SPLAY MSTC-0002=(P,k,C,rho) identity has no Council counterpart; Council candidates are SpecialistSpec versions"),
 ("MST-FRESHBANK-NA", "fresh_bank",
  "SPLAY fresh-bank H4L/n=28 witness rules map to Council HOLD-*; no separate MST bank applies"),
 ("MST-AXIS-NA", "axis_successor",
  "SPLAY rho-axis surgical allowance does not apply; Council successor rule is Sec-64")]
for mid, cat, desc in mst_na:
    items.append({"id": mid, "category": cat, "source_section": "SPEC_CONFLICT-01",
        "source_file": "audits/SPLAY-AM-MST-LIQ-v0.4_SPEC.txt", "source_line": 1,
        "source_anchor": "", "description": desc, "status": "not_applicable"})
items.append({"id": "SPEC-CONFLICT-01", "category": "spec_conflict",
    "source_section": "process-Rule-14", "source_file": "IMPLEMENTATION_SPEC.md",
    "source_line": 1, "source_anchor": "",
    "description": "Process header names SPLAY-AM-MST-LIQ-v0.4/MST-LIQ but operative repo+spec are COUNCIL-PC-v1.0; MST rho/LIQ0/MST0 semantics are NOT_APPLICABLE; Council sections govern",
    "status": "normative"})

# --- write YAML deterministically (with canonical count terminology) ---
OUT.parent.mkdir(parents=True, exist_ok=True)
norm_total = sum(1 for it in items if it["status"] == "normative")
na_total = sum(1 for it in items if it["status"] == "not_applicable")
with OUT.open("w", encoding="utf-8") as f:
    f.write("# NORMATIVE_INVENTORY for COUNCIL-PC-v1.0\n")
    f.write("# operative_spec: IMPLEMENTATION_SPEC.md\n")
    f.write(f"# operative_sha256: {sha}\n")
    f.write("# provider_migration: OpenRouter->OpenCode (3 literal lines, audit PASS; see audits/PROVIDER_MIGRATION_AUDIT.md)\n")
    f.write("# planning_mutation: Sec-15.6 exhaustive source-acquisition doctrine + COL-GATE-22 + registry-eligibility wording\n")
    f.write(f"# total_lines: {len(lines)}\n")
    f.write("# generated_by: scripts/gen_normative_inventory.py (deterministic, section-bounded anchors)\n")
    f.write("metadata:\n")
    f.write("  experiment: COUNCIL-PC-v1.0\n")
    f.write("  short_name: COL-PC-v1.0\n")
    f.write("  implementation_repo: InfernusReal/Council-of-Lords-PC\n")
    f.write("  conceptual_parent: PERCEPTIVE CLOSURE: IDENTIFYING AUTHORIZATION-RESOURCE COUNTERFACTUALS\n")
    f.write("  legacy_parent: InfernusReal/Council-Of-Lords (archaeological reference only)\n")
    f.write("  teacher: Muse Spark 1.3 Contributor through OpenCode\n")
    f.write(f"  operative_spec_sha256: {sha}\n")
    f.write(f"  spec_lines: {len(lines)}\n")
    f.write(f"  inventory_items_total: {len(items)}\n")
    f.write(f"  normative_items_total: {norm_total}\n")
    f.write(f"  not_applicable_items_total: {na_total}\n")
    f.write("items:\n")
    for it in items:
        f.write(f"  - id: {it['id']}\n")
        f.write(f"    category: {it['category']}\n")
        f.write(f"    source_section: {it['source_section']}\n")
        f.write(f"    source_file: {it['source_file']}\n")
        f.write(f"    source_line: {it['source_line']}\n")
        f.write(f"    source_anchor: \"{it['source_anchor'].replace(chr(34), chr(39))}\"\n")
        d = it['description'].replace('"', "'")
        f.write(f'    description: "{d}"\n')
        f.write(f"    status: {it['status']}\n")
print(f"WROTE {OUT} inventory={len(items)} normative={norm_total} na={na_total} sha={sha}")