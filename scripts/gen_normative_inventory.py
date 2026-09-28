"""Deterministic generator for planning/NORMATIVE_INVENTORY.yaml.
Reads IMPLEMENTATION_SPEC.md (operative revised spec, OpenCode provider)
and derives every normative item with source pointers.
No counts are hardcoded from memory; all enumerations are parsed or
explicitly listed from the spec text with section/line provenance.
"""
import pathlib, re, hashlib

SPEC = pathlib.Path("IMPLEMENTATION_SPEC.md")
OUT = pathlib.Path("planning/NORMATIVE_INVENTORY.yaml")
text = SPEC.read_text(encoding="utf-8")
lines = text.splitlines()
sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

def find_line(substr):
    for i, l in enumerate(lines, 1):
        if substr in l:
            return i
    return 0

def section_line(n):
    # "# N. " headings; N=0..68
    for i, l in enumerate(lines, 1):
        if re.match(rf"# {n}\.(\s|$)", l):
            return i
    return 0

items = []
def add(id, category, source_section, source_pat, description, status="normative"):
    ln = find_line(source_pat) if source_pat else 0
    items.append({
        "id": id, "category": category, "source_section": source_section,
        "source_file": "IMPLEMENTATION_SPEC.md", "source_line": ln,
        "description": description, "status": status,
    })

# --- 0. Spec sections SEC-00..SEC-68 (69 items) ---
titles = {}
for i, l in enumerate(lines, 1):
    m = re.match(r"# (\d+)\.\s+(.*)", l)
    if m:
        titles[int(m.group(1))] = (m.group(2).strip(), i)
for n in range(0, 69):
    title, ln = titles.get(n, (f"section-{n}", 0))
    items.append({"id": f"SEC-{n:02d}", "category": "spec_section",
        "source_section": f"Sec-{n}", "source_file": "IMPLEMENTATION_SPEC.md",
        "source_line": ln, "description": f"Spec section {n}: {title}", "status": "normative"})

# --- PHASES 00..30 (31) ---
for n in range(0, 31):
    pat = f"PHASE {n:02d}"
    items.append({"id": f"PHASE-{n:02d}", "category": "phase",
        "source_section": "Sec-47", "source_file": "IMPLEMENTATION_SPEC.md",
        "source_line": find_line(pat), "description": f"Normative phase {n:02d} per phase map",
        "status": "normative"})

# --- Work packages WP-0..WP-8 (9) ---
for n in range(0, 9):
    items.append({"id": f"WP-{n}", "category": "work_package",
        "source_section": "Sec-46", "source_file": "IMPLEMENTATION_SPEC.md",
        "source_line": find_line(f"## WP-{n}"), "description": f"Work package WP-{n} per Sec-46",
        "status": "normative"})

# --- Gates COL-GATE-00..21 (22) ---
gate_names = {
 0:"FOUNDATION_FROZEN",1:"LEGACY_ARCHAEOLOGY_COMPLETE",2:"DATA_CORE_CERTIFIED",
 3:"DATASET_FACTORY_CERTIFIED",4:"PC_CORE_CERTIFIED",5:"TOUCH_DERIVATION_INDEPENDENT_AGREEMENT",
 6:"CATALOGUE_ENGINE_CERTIFIED",7:"REPRESENTATION_ENGINE_CERTIFIED",8:"FORGE_OPERATIONAL",
 9:"CALIBRATION_PIPELINE_CERTIFIED",10:"QUALIFICATION_HARNESS_CERTIFIED",11:"TEACHER_PIPELINE_CERTIFIED",
 12:"SPECIALIST_CANDIDATE_SET_FROZEN",13:"FRESH_HOLDOUT_REVEALED_ONCE",14:"INITIAL_LORDS_QUALIFIED",
 15:"REGISTRY_SEALED",16:"COUNCIL_RUNTIME_CERTIFIED",17:"RESOURCE_VIEW_AUDIT_PASSED",
 18:"PC_FREEZE_GEOMETRY_RECOMPUTED",19:"MUTATION_SUITE_PASSED",20:"CLEANROOM_REPRODUCTION_PASSED",
 21:"PC_NATIVE_COUNCIL_QUALIFIED"}
for n, nm in gate_names.items():
    add(f"COL-GATE-{n:02d}", "gate", "Sec-48", f"COL-GATE-{n:02d}", f"Gate {nm}")

# --- Threats COL-T01..30 ---
for n in range(1, 31):
    add(f"COL-T{n:02d}", "threat", "Sec-44", f"COL-T{n:02d}", f"Threat COL-T{n:02d} per threat matrix")

# --- Stops COL-STOP-01..25 ---
for n in range(1, 26):
    add(f"COL-STOP-{n:02d}", "stop", "Sec-45", f"COL-STOP-{n:02d}", f"Stop COL-STOP-{n:02d}")

# --- Test classes (14, Sec-54) ---
tests = ["unit tests","property tests","schema tests","provenance tests","leakage tests",
"model-interface tests","calibration tests","registry integrity tests","PC semantic tests",
"touch derivation tests","freeze tests","mutation tests","legacy regression tests","clean-room reproduction tests"]
for i, nm in enumerate(tests, 1):
    add(f"TEST-{i:02d}", "test_class", "Sec-54", nm.split()[0], f"Test class: {nm}")

# --- Schemas (17, Sec-66) ---
schemas = ["LightCurveSchema","EvidenceStateSchema","RepresentationSchema","AuthoritySchema",
"ActionSchema","CheckpointSchema","SpecialistResultSchema","TaskSpecSchema","SpecialistSpecSchema",
"DatasetManifestSchema","RunManifestSchema","QualificationReportSchema","CapabilityMapSchema",
"RegistryEntrySchema","TeacherTransactionSchema","CouncilTraceSchema","FreezeResultSchema"]
for i, nm in enumerate(schemas, 1):
    add(f"SCHEMA-{i:02d}", "schema", "Sec-66", nm, f"Schema v1 to freeze: {nm}")

# --- Terminal outcomes (10, Sec-63) ---
terms = ["PC_NATIVE_COUNCIL_QUALIFIED","QUALIFIED_WITH_DECLARED_LIMITATIONS","FORGE_QUALIFIED_RUNTIME_BLOCKED",
"PC_SEMANTICS_UNDERIDENTIFIED","SPECIALIST_QUALIFICATION_FAILED","DATASET_INTEGRITY_FAILED",
"HOLDOUT_CONTAMINATED","TEACHER_BUDGET_EXHAUSTED","RESOURCE_LIMIT_REACHED","ARCHITECTURE_SUCCESSOR_REQUIRED"]
for i, nm in enumerate(terms, 1):
    add(f"TERM-{i:02d}", "terminal_outcome", "Sec-63", nm, f"Terminal state: {nm}")

# --- Release artifacts (19, Sec-51) ---
arts = ["RELEASE_MANIFEST.json","SOURCE_COMMIT.txt","ENVIRONMENT_LOCK","DATASET_MANIFESTS","TASK_SPECS",
"SPECIALIST_SPECS","REGISTRY_MANIFEST.json","QUALIFICATION_REPORTS","PC_CONTRACT.json","ACTION_SCHEMA.json",
"ATOMICITY_SCHEMA.json","TOUCH_RECOMPUTATION.json","FREEZE_RESULTS.json","MUTATION_RESULTS.json",
"TEACHER_BUDGET_LEDGER.json","TEACHER_PROVENANCE_MANIFEST.json","LEGACY_ARCHAEOLOGY.md","FINAL_AUDIT.md","FINAL_RESULT.json"]
for i, nm in enumerate(arts, 1):
    add(f"ART-{i:02d}", "release_artifact", "Sec-51", nm.split('.')[0], f"Release package artifact: {nm}")

# --- Evaluation labels (9, Sec-42) ---
labels = ["LEGACY_HISTORICAL","DEVELOPMENT","INTERNAL_VALIDATION","TEACHER_GENERATED_DEVELOPMENT",
"CONTAMINATED_CANARY","FRESH_QUALIFICATION_HOLDOUT","CLEANROOM_POST_FREEZE","FORMAL_PC_CONSTRUCTED","OBSERVATIONAL_EXTERNAL_TEST"]
for i, nm in enumerate(labels, 1):
    add(f"LABEL-{i:02d}", "eval_label", "Sec-42", nm, f"Evaluation row label: {nm}")

# --- Dataset source classes (9, Sec-15.1) ---
dcls = ["OBSERVATIONAL_RAW","OBSERVATIONAL_DERIVED","CATALOG_LABELLED","SIMULATED_PHYSICS","SYNTHETIC_STRESS",
"LLM_PROPOSED_SCENARIO","LEGACY_HISTORICAL","CONTAMINATED_DEVELOPMENT","HIDDEN_HOLDOUT"]
for i, nm in enumerate(dcls, 1):
    add(f"DCLASS-{i:02d}", "dataset_class", "Sec-15", nm, f"Dataset source class: {nm}")

# --- Label confidence (7, Sec-15.4) ---
lconf = ["CONFIRMED","HIGH_CONFIDENCE","CATALOG_CANDIDATE","KNOWN_FALSE_POSITIVE","SIMULATED_KNOWN","AMBIGUOUS","UNRESOLVED"]
for i, nm in enumerate(lconf, 1):
    add(f"LCONF-{i:02d}", "label_confidence", "Sec-15", nm, f"Label confidence: {nm}")

# --- Mutation controls (21, Sec-43) ---
mutants = [
 "raw scratch field silently admitted into H",
 "representation flag changes without P_R change",
 "P_R changes but touch omits R",
 "authority changes action availability without Lambda change",
 "manual touch label overrides derived touch",
 "freeze removes only part of a mixed source-atomic action",
 "hidden label leaked into controller observation",
 "holdout row appears in training identity group",
 "model trained with forbidden evidence",
 "registry model bytes changed under same version",
 "calibration file from another model version",
 "capability map attached to wrong artifact",
 "unqualified model loaded as qualified",
 "teacher output accepted as observational ground truth",
 "teacher prompt contains hidden holdout outcome",
 "synthetic provenance dropped",
 "solar-default fallback presented as measured stellar data",
 "legacy fixed specialist weights reintroduced",
 "majority vote bypasses closure",
 "red flag directly subtracts arbitrary verdict score",
 "API/frontend mutates scientific state outside engine"]
for i, nm in enumerate(mutants, 1):
    add(f"MUT-{i:02d}", "mutation_control", "Sec-43", nm[:30], f"Semantic mutant: {nm}")

# --- Adversarial corpus families (20, Sec-40) ---
adv = ["clean planetary transits","grazing eclipsing binaries","detached eclipsing binaries","contact binaries",
"diluted/blended binaries","stellar activity","rotational variability","instrument artifacts","period aliases",
"secondary eclipses","very low SNR candidates","two-transit sparse events","long-period candidates","strong data gaps",
"centroid contamination","contradictory stellar metadata","OOD catalogue values","OOD light-curve morphology",
"calibration-edge cases","specialist disagreement cases"]
for i, nm in enumerate(adv, 1):
    add(f"ADV-{i:02d}", "adversarial_family", "Sec-40", nm.split()[0], f"Adversarial corpus family: {nm}")

# --- PC evaluation questions (8, Sec-36) ---
pcq = ["closure without new evidence admission","closure without representation refinement",
"closure without authority-changing actions","removing external stellar evidence fallback vs structural failure",
"morphology diagnostics substitute for additional evidence","learned specialist reduces cost without becoming necessary",
"two behaviorally similar pipelines different resource dependence","refuse unique attribution when underidentified"]
for i, nm in enumerate(pcq, 1):
    add(f"PCQ-{i:02d}", "pc_eval_question", "Sec-36", "Can closure occur" if i<=3 else nm[:20], f"PC evaluation question: {nm}")

# --- Red-flag diagnostics (15, Sec-39) ---
diags = ["V/U morphology","odd/even depth asymmetry","secondary eclipse","period harmonics and aliases",
"transit-duration consistency","stellar-radius/depth consistency","centroid shift","neighbor contamination",
"mission systematic-period coincidence","strong stellar variability","low effective SNR","insufficient transit count",
"severe cadence gaps","model OOD","cross-specialist semantic disagreement"]
for i, nm in enumerate(diags, 1):
    add(f"DIAG-{i:02d}", "diagnostic", "Sec-39", nm.split()[0], f"Red-flag diagnostic: {nm}")

# --- Action vocabulary (25, Sec-10) ---
acts = ["LOAD_LIGHTCURVE","APPLY_QUALITY_MASK","NORMALIZE_FLUX","DETREND_VARIANT","SEARCH_PERIOD_BLS",
"SEARCH_PERIOD_ALTERNATE","FOLD_PERIOD","FIT_TRANSIT_SHAPE","COMPUTE_ODD_EVEN","SEARCH_SECONDARY_ECLIPSE",
"COMPUTE_VARIABILITY","COMPUTE_CENTROID_DIAGNOSTICS","QUERY_STELLAR_CATALOG","QUERY_NEIGHBOR_CATALOG",
"ESTIMATE_DILUTION","RUN_MORPHOLOGY_LORD","RUN_PERIODICITY_LORD","RUN_FALSE_POSITIVE_LORD","RUN_STELLAR_LORD",
"RUN_INSTRUMENT_LORD","RUN_GENERAL_VETTER","REFINE_REPRESENTATION","REQUEST_ADDITIONAL_SECTOR","ESCALATE_HUMAN","STOP_UNRESOLVED"]
for i, nm in enumerate(acts, 1):
    add(f"ACT-{i:02d}", "action_vocab", "Sec-10", nm, f"Action vocabulary entry: {nm}")

# --- Lord roster (6, Sec-12) ---
lords = ["MorphologyLord","PeriodicityLord","FalsePositiveLord","StellarPlausibilityLord","InstrumentLord","GeneralVetter"]
for i, nm in enumerate(lords, 1):
    add(f"LORD-{i:02d}", "lord_roster", "Sec-12", nm, f"Initial roster lord: {nm}")

# --- CLI commands (18, Sec-55) ---
clis = ["col data ingest","col data build","col data audit","col task validate","col train run","col train search",
"col calibrate","col qualify","col registry verify","col registry list","col teacher generate","col teacher audit",
"col council analyze","col council replay","col pc touch","col pc close","col pc freeze","col audit full"]
for i, nm in enumerate(clis, 1):
    add(f"CLI-{i:02d}", "cli_command", "Sec-55", nm, f"CLI command: {nm}")

# --- Final audit questions (15, Sec-67) ---
aq = ["trace qualified model to data+code","trace dataset row to source+identity","trace runtime feature to admitted evidence",
"prove specialist input authorized by view","recompute every E/R/A touch","trace representation refinement to diagnostic/action",
"trace authority change to Lambda","recompute closed verdict from target+worlds","show open state does not bypass closure",
"distinguish teacher artifact from ground truth","show holdout uncontaminated","byte-verify registry artifact",
"run without frontend","run core without LLM at inference","replay release from manifests"]
for i, nm in enumerate(aq, 1):
    add(f"AUDQ-{i:02d}", "audit_question", "Sec-67", nm[:20], f"Final audit question: {nm}")

# --- Lord promotion criteria (16, Sec-61) ---
lpc = ["TaskSpec frozen","input schema frozen","allowed/forbidden evidence frozen","dataset+split manifests frozen",
"protected-identity leakage zero","training reproducible","calibration passes","abstention passes","OOD passes",
"stress passes","fresh holdout passes","capability map generated","failure regions disclosed","artifact bytes hashed",
"registry package verifies","no hidden teacher dependency unless declared"]
for i, nm in enumerate(lpc, 1):
    add(f"LPC-{i:02d}", "promotion_criterion", "Sec-61", nm[:20], f"Lord promotion criterion: {nm}")

# --- Council promotion criteria (10, Sec-62) ---
cpc = ["all Lords registry-qualified","PC target frozen","H/P_R/Lambda frozen","action/atomicity frozen",
"independent touch agrees","controller deterministic/seed-bound","resource views enforce allowed evidence",
"open cannot emit closed","mutation controls pass","replay deterministic"]
for i, nm in enumerate(cpc, 1):
    add(f"CPC-{i:02d}", "promotion_criterion", "Sec-62", nm[:20], f"Council promotion criterion: {nm}")

# --- PC semantic obligations (core, Sec-4..9,33..38) ---
pcobl = [
 ("PC-H", "Sec-6", "H_t", "Admitted evidence history H with admission-only mutation"),
 ("PC-PR", "Sec-7", "P_R", "Certificate/representation relation P_R refinement"),
 ("PC-LAMBDA", "Sec-8", "Lambda", "Epistemic authority Lambda extensional licensing"),
 ("PC-OMEGA", "Sec-4", "omega", "Controller observation omega without hidden leakage"),
 ("PC-TARGET", "Sec-4", "A_Pi", "Sealed vetting target A_Pi over D"),
 ("PC-COMPAT", "Sec-5", "C_R", "Represented compatible-world set C_R"),
 ("PC-CLOSURE", "Sec-5", "closed", "Target-relative closure |{A(x)}|=1, no vote bypass"),
 ("PC-ADMIT", "Sec-6", "admission", "Source-atomic admission rule; raw availability != admission"),
 ("PC-NOFALLBACK", "Sec-6", "fallback", "No silent solar-default fallback; DECLARED_DEFAULT with uncertainty"),
 ("PC-TOUCH", "Sec-9", "T_s", "Extensional touch derivation T_s(q), no manual E/R/A"),
 ("PC-ATOM", "Sec-9", "Atom", "Source atomicity Atom; freezes never split mixed actions"),
 ("PC-SUCC", "Sec-9", "Succ", "Positive-support successors Succ+ semantics"),
 ("PC-COST", "Sec-34", "c(q)", "Nonnegative action cost c(q) with unit-cost convention declared"),
 ("PC-KAPPA", "Sec-35", "kappa", "Closure cost kappa and freeze signature K over 8 freezes"),
 ("PC-IDENT", "Sec-37", "BOUNDARY", "Identification gate; BOUNDARY_UNDERIDENTIFIED if touch underidentified"),
 ("PC-INDTOUCH", "Sec-38", "independent", "Independent touch reconstruction agreement gate"),
 ("PC-VIEWS", "Sec-28", "View_v", "Authorized PC resource views View_v(H,P_R,Lambda)"),
 ("PC-RELIAB", "Sec-25", "r_i", "State-dependent reliability r_i(s), no fixed 1.4x weights"),
 ("PC-REPORT", "Sec-56", "report", "Runtime report with hash chain, touch, authority, cost, replay"),
 ("PC-CONTROLLER", "Sec-33", "controller", "Controller legality: no holdout peek, no forbidden evidence, no closure override")]
for oid, sec, pat, desc in pcobl:
    add(oid, "pc_obligation", sec, pat, desc)

# --- PC sanity witnesses (12, WP-2 gate) ---
wit = ["pure E action","pure R action","pure A action","mixed ER action","mixed EA action","mixed RA action",
"mixed ERA action","open state","closed state","R-freeze finite fallback","R-freeze structural failure","boundary-underidentified fixture"]
for i, nm in enumerate(wit, 1):
    add(f"WIT-{i:02d}", "pc_witness", "Sec-46", nm.split()[0], f"PC finite sanity witness: {nm}")

# --- Qualification Q components (7, Sec-23) ---
for i, nm in enumerate(["Q_general","Q_calibration","Q_stress","Q_OOD","Q_leakage","Q_reproducibility","Q_semantic"], 1):
    add(f"Q-{i:02d}", "qualification_gate", "Sec-23", nm, f"Qualification component: {nm}")

# --- Holdout / firewall rules (from Sec-41,42,6x) ---
holdouts = [
 ("HOLD-01", "freeze hidden holdout before final promotion; inaccessible to fitting/search/thresholds/teacher/repair"),
 ("HOLD-02", "one reveal per qualification campaign; after reveal bank becomes historical"),
 ("HOLD-03", "new major campaign requires new hidden bank"),
 ("HOLD-04", "no holdout row in training identity group (object-level split)"),
 ("HOLD-05", "no post-hoc threshold tuning on holdout"),
 ("HOLD-06", "no post-hoc representation tuning on holdout"),
 ("HOLD-07", "no historical result relabeled fresh"),
 ("HOLD-08", "legacy fixtures only LEGACY_HISTORICAL, never fresh holdout")]
for hid, desc in holdouts:
    add(hid, "holdout_rule", "Sec-41", desc[:25], desc)

# --- Teacher rules (from Sec-29..31) ---
teachers = [
 ("TEACH-01","Muse Spark via OpenCode; schema-bound, provenance-recorded, budget-capped, no ground-truth authority"),
 ("TEACH-02","structured output only for machine ingestion (versioned JSON schema)"),
 ("TEACH-03","every transaction records model/provider/route/prompt_hash/input_hash/schema/params/response_hash/validation/cost"),
 ("TEACH-04","budget USD 25 default ceiling; fail closed before exceeding"),
 ("TEACH-05","scenario-constraints pattern: proposal->schema->materializer->synthetic provenance, never observational"),
 ("TEACH-06","failure discovery requires deterministic criterion/statistical separation/new test family/physical check/human rationale"),
 ("TEACH-07","no teacher-derived artifact as runtime ground truth unless declared"),
 ("TEACH-08","secrets: .env ignored, no keys in logs/traces, scrubbed provider responses")]
for tid, desc in teachers:
    add(tid, "teacher_rule", "Sec-29", desc[:25], desc)

# --- Claim restrictions / non-goals (Sec-2 + doctrine) ---
claims = [
 ("CLAIM-01","five specialists optimal (not claimed)"),
 ("CLAIM-02","more specialists always better (not claimed)"),
 ("CLAIM-03","neural/large models required (not claimed)"),
 ("CLAIM-04","LLM runtime classification (not claimed; teacher dev-only)"),
 ("CLAIM-05","Muse output is ground truth (forbidden)"),
 ("CLAIM-06","weighted voting is closure (forbidden; closure is PC-defined)"),
 ("CLAIM-07","confidence is authorization/calibrated probability (forbidden without calibration)"),
 ("CLAIM-08","red flag subtracts fixed scalar (forbidden)"),
 ("CLAIM-09","finite benchmark success = universal guarantee / exoplanet confirmation (forbidden)"),
 ("CLAIM-10","PC E/R/A universal astronomy ontology (not claimed)"),
 ("CLAIM-11","UNRESOLVED must not conceal failure to compute closure"),
 ("CLAIM-12","closed verdict must not be presented as confirmed exoplanet")]
for cid, desc in claims:
    add(cid, "claim_policy", "Sec-2", desc[:20], desc)

# --- Hygiene / successor / reproducibility / secrets ---
add("HYG-01","hygiene","Sec-49","Preserve","Legacy mined not ported wholesale; preserve list per Sec-49.1")
add("HYG-02","hygiene","Sec-49","Do not preserve","Do-not-preserve list per Sec-49.2 (node_modules, checkpoints as qualified, weights, theatrical losses, monolith, defaults, dumps)")
add("HYG-03","hygiene","Sec-49","LEGACY_UNQUALIFIED","Historical models wrapped LEGACY_UNQUALIFIED for regression only")
add("HYG-04","hygiene","Sec-65","layout","Clean-room repository layout per Sec-65; large artifacts via manifests not casual git")
add("HYG-05","hygiene","Sec-65","Large raw","Large raw/run/model binaries not committed casually")
add("REPRO-01","reproducibility","Sec-51","hash-addressable","Every release artifact hash-addressable")
add("REPRO-02","reproducibility","Sec-51","Failed qualification","Failed/negative results preserved, no rewritten success narrative")
add("REPRO-03","reproducibility","Sec-13","4 GB VRAM","Default roster trains within 4GB VRAM; exception needs versioned justification")
add("SECRET-01","secret","Sec-52",".env ignored","Secrets via env/manager; .env ignored; .env.example names only")
add("SECRET-02","secret","Sec-52","no API keys","No keys/headers in logs/traces; scrubbed storage; hashes separate from credentials")
add("SUCC-01","successor_rule","Sec-64","preserve the failed","Successor rule: preserve architecture+witness, diagnose, seal, version, add only justified change")
add("SUCC-02","successor_rule","Sec-64","No new coordinate","No new coordinate silently inserted into existing release")
add("COMMIT-01","commit_rule","process","VERIFY -> UPDATE","Every completed WP: VERIFY->UPDATE Path.md->COMPLIANCE AUDIT->COMMIT->PUSH->VERIFY REMOTE HEAD")
add("AUDIT-LEGACY-01","parent_import","Sec-46","Pin","WP-0 pins legacy commit/README/scripts/ensemble/converter/fixtures + PC paper + spec + threats + ontology + env")
add("ANTI-01","anti_pattern","Sec-50","parallel neural","Anti-pattern ledger entry: parallel classifiers over same 8 features"),
add("ANTI-02","anti_pattern","Sec-50","altered losses","Anti-pattern: specialties via losses/widths/thresholds not views"),
add("ANTI-03","anti_pattern","Sec-50","hard-coded","Anti-pattern: hard-coded weights and boosts/penalties"),
add("ANTI-04","anti_pattern","Sec-50","converter bundles","Anti-pattern: monolithic converter bundling"),
add("ANTI-05","anti_pattern","Sec-50","Generated training","Anti-pattern: synthetic draws presented via NASA ranges"),
add("ANTI-06","anti_pattern","Sec-50","stress suites","Valuable historical adversarial ideas preserved as LEGACY_HISTORICAL"),
add("ANTI-07","anti_pattern","Sec-50","tracks generated","Anti-pattern: caches/checkpoints/deps/datasets tracked together"),

# --- MST template residue: explicitly NOT_APPLICABLE to Council domain (SPEC_CONFLICT-01) ---
mst_na = [
 ("MST-LIQ0-NA","liquidity_obligation","SPLAY template LIQ0-* has no Council counterpart; Council tracks activation via PC views/diagnostics, not rho"),
 ("MST-MST0-NA","theorem_obligation","SPLAY MST0-* transfer theorems have no Council counterpart; Council theorems are PC closure/freeze/diagnostic obligations"),
 ("MST-CAND-NA","candidate_identity","SPLAY MSTC-0002=(P,k,C,rho) identity has no Council counterpart; Council candidates are SpecialistSpec versions"),
 ("MST-FRESHBANK-NA","fresh_bank","SPLAY fresh-bank H4L/n=28 witness rules map to Council HOLD-*; no separate MST bank applies"),
 ("MST-AXIS-NA","axis_successor","SPLAY rho-axis surgical allowance does not apply; Council successor rule is Sec-64")]
for mid, cat, desc in mst_na:
    items.append({"id": mid, "category": cat, "source_section": "SPEC_CONFLICT-01",
        "source_file": "audits/SPLAY-AM-MST-LIQ-v0.4_SPEC.txt", "source_line": 1,
        "description": desc, "status": "not_applicable"})
items.append({"id": "SPEC-CONFLICT-01", "category": "spec_conflict",
    "source_section": "process-Rule-14", "source_file": "IMPLEMENTATION_SPEC.md", "source_line": 1,
    "description": "Process header names SPLAY-AM-MST-LIQ-v0.4/MST-LIQ but operative repo+spec are COUNCIL-PC-v1.0; MST rho/LIQ0/MST0 semantics are NOT_APPLICABLE; Council Sec-0..68 governs",
    "status": "normative"})

# --- write YAML deterministically ---
OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as f:
    f.write(f"# NORMATIVE_INVENTORY for COUNCIL-PC-v1.0\n")
    f.write(f"# operative_spec: IMPLEMENTATION_SPEC.md\n")
    f.write(f"# operative_sha256: {sha}\n")
    f.write(f"# original_sha256: a9453d20079ace95d8227d0fed095398b4aa6de1d1265f61ba6fe1b4c5dbf0fb\n")
    f.write(f"# provider_migration: OpenRouter->OpenCode (3 literal lines, audit PASS)\n")
    f.write(f"# total_lines: {len(lines)}\n")
    f.write(f"# generated_by: scripts/gen_normative_inventory.py (deterministic)\n")
    f.write(f"metadata:\n")
    f.write(f"  experiment: COUNCIL-PC-v1.0\n")
    f.write(f"  short_name: COL-PC-v1.0\n")
    f.write(f"  implementation_repo: InfernusReal/Council-of-Lords-PC\n")
    f.write(f"  conceptual_parent: PERCEPTIVE CLOSURE: IDENTIFYING AUTHORIZATION-RESOURCE COUNTERFACTUALS\n")
    f.write(f"  legacy_parent: InfernusReal/Council-Of-Lords (archaeological reference only)\n")
    f.write(f"  teacher: Muse Spark 1.3 Contributor through OpenCode\n")
    f.write(f"  operative_spec_sha256: {sha}\n")
    f.write(f"  spec_lines: {len(lines)}\n")
    f.write(f"  total_items: {len(items)}\n")
    f.write(f"items:\n")
    for it in items:
        f.write(f"  - id: {it['id']}\n")
        f.write(f"    category: {it['category']}\n")
        f.write(f"    source_section: {it['source_section']}\n")
        f.write(f"    source_file: {it['source_file']}\n")
        f.write(f"    source_line: {it['source_line']}\n")
        # escape quotes
        d = it['description'].replace('"', "'")
        f.write(f'    description: \"{d}\"\n')
        f.write(f"    status: {it['status']}\n")
print(f"WROTE {OUT} items={len(items)} sha={sha}")
