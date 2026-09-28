"""Deterministic generator for planning/WORKPLAN_COVERAGE.yaml.
Maps every normative inventory item to accountable WP + artifacts.
Phase/gate ownership matches WorkPlan.md Appendix exactly.
"""
import pathlib, re
INV = pathlib.Path("planning/NORMATIVE_INVENTORY.yaml")
OUT = pathlib.Path("planning/WORKPLAN_COVERAGE.yaml")

# --- ownership tables (must match WorkPlan.md) ---
phase_wp = {f"PHASE-{n:02d}": wp for n, wp in [
 (0,"WP-0"),(1,"WP-0"),(2,"WP-1"),(3,"WP-1"),(4,"WP-1"),
 (5,"WP-2"),(6,"WP-2"),(7,"WP-2"),(8,"WP-3"),(9,"WP-3"),(10,"WP-3"),
 (11,"WP-4"),(12,"WP-4"),(13,"WP-4"),(14,"WP-4"),(15,"WP-4"),
 (16,"WP-5"),(17,"WP-5"),(18,"WP-6"),(19,"WP-6"),(20,"WP-6"),(21,"WP-6"),
 (22,"WP-7"),(23,"WP-7"),(24,"WP-7"),(25,"WP-8"),(26,"WP-8"),(27,"WP-8"),
 (28,"WP-8"),(29,"WP-8"),(30,"WP-8")]}
gate_wp = {f"COL-GATE-{n:02d}": wp for n, wp in [
 (0,"WP-0"),(1,"WP-0"),(2,"WP-1"),(3,"WP-4"),(4,"WP-2"),(5,"WP-2"),
 (6,"WP-3"),(7,"WP-3"),(8,"WP-4"),(9,"WP-4"),(10,"WP-4"),(11,"WP-5"),
 (12,"WP-6"),(13,"WP-6"),(14,"WP-6"),(15,"WP-6"),(16,"WP-7"),(17,"WP-7"),
 (18,"WP-8"),(19,"WP-8"),(20,"WP-8"),(21,"WP-8")]}
# section primary owners (at least one; appendix-compatible)
sec_wp = {
 "SEC-00":"WP-0","SEC-01":"WP-0","SEC-02":"WP-0","SEC-03":"WP-0","SEC-04":"WP-2",
 "SEC-05":"WP-2","SEC-06":"WP-3","SEC-07":"WP-3","SEC-08":"WP-2","SEC-09":"WP-2",
 "SEC-10":"WP-3","SEC-11":"WP-4","SEC-12":"WP-4","SEC-13":"WP-4","SEC-14":"WP-4",
 "SEC-15":"WP-4","SEC-16":"WP-1","SEC-17":"WP-4","SEC-18":"WP-4","SEC-19":"WP-4",
 "SEC-20":"WP-4","SEC-21":"WP-4","SEC-22":"WP-4","SEC-23":"WP-4","SEC-24":"WP-4",
 "SEC-25":"WP-7","SEC-26":"WP-6","SEC-27":"WP-7","SEC-28":"WP-4","SEC-29":"WP-5",
 "SEC-30":"WP-5","SEC-31":"WP-5","SEC-32":"WP-7","SEC-33":"WP-7","SEC-34":"WP-2",
 "SEC-35":"WP-8","SEC-36":"WP-8","SEC-37":"WP-2","SEC-38":"WP-2","SEC-39":"WP-3",
 "SEC-40":"WP-8","SEC-41":"WP-6","SEC-42":"WP-6","SEC-43":"WP-8","SEC-44":"WP-8",
 "SEC-45":"WP-8","SEC-46":"WP-0","SEC-47":"WP-0","SEC-48":"WP-0","SEC-49":"WP-0",
 "SEC-50":"WP-0","SEC-51":"WP-8","SEC-52":"WP-5","SEC-53":"WP-0","SEC-54":"WP-4",
 "SEC-55":"WP-7","SEC-56":"WP-7","SEC-57":"WP-8","SEC-58":"WP-8","SEC-59":"WP-0",
 "SEC-60":"WP-4","SEC-61":"WP-6","SEC-62":"WP-7","SEC-63":"WP-8","SEC-64":"WP-8",
 "SEC-65":"WP-0","SEC-66":"WP-4","SEC-67":"WP-8","SEC-68":"WP-8"}
threat_wp = {
 "COL-T01":"WP-1","COL-T02":"WP-1","COL-T03":"WP-1","COL-T04":"WP-5","COL-T05":"WP-6",
 "COL-T06":"WP-6","COL-T07":"WP-6","COL-T08":"WP-2","COL-T09":"WP-2","COL-T10":"WP-3",
 "COL-T11":"WP-3","COL-T12":"WP-7","COL-T13":"WP-2","COL-T14":"WP-6","COL-T15":"WP-2",
 "COL-T16":"WP-4","COL-T17":"WP-4","COL-T18":"WP-0","COL-T19":"WP-3","COL-T20":"WP-4",
 "COL-T21":"WP-6","COL-T22":"WP-5","COL-T23":"WP-5","COL-T24":"WP-3","COL-T25":"WP-7",
 "COL-T26":"WP-8","COL-T27":"WP-7","COL-T28":"WP-4","COL-T29":"WP-2","COL-T30":"WP-2"}
stop_wp = {
 "COL-STOP-01":"WP-0","COL-STOP-02":"WP-0","COL-STOP-03":"WP-7","COL-STOP-04":"WP-2",
 "COL-STOP-05":"WP-2","COL-STOP-06":"WP-2","COL-STOP-07":"WP-2","COL-STOP-08":"WP-2",
 "COL-STOP-09":"WP-6","COL-STOP-10":"WP-6","COL-STOP-11":"WP-5","COL-STOP-12":"WP-6",
 "COL-STOP-13":"WP-6","COL-STOP-14":"WP-6","COL-STOP-15":"WP-6","COL-STOP-16":"WP-7",
 "COL-STOP-17":"WP-2","COL-STOP-18":"WP-5","COL-STOP-19":"WP-5","COL-STOP-20":"WP-5",
 "COL-STOP-21":"WP-4","COL-STOP-22":"WP-7","COL-STOP-23":"WP-8","COL-STOP-24":"WP-8",
 "COL-STOP-25":"WP-8"}
test_wp = {"TEST-01":"WP-1","TEST-02":"WP-1","TEST-03":"WP-3","TEST-04":"WP-1","TEST-05":"WP-4",
 "TEST-06":"WP-4","TEST-07":"WP-4","TEST-08":"WP-6","TEST-09":"WP-2","TEST-10":"WP-2",
 "TEST-11":"WP-2","TEST-12":"WP-8","TEST-13":"WP-8","TEST-14":"WP-8"}
schema_wp = {"SCHEMA-01":"WP-1","SCHEMA-02":"WP-3","SCHEMA-03":"WP-3","SCHEMA-04":"WP-2",
 "SCHEMA-05":"WP-2","SCHEMA-06":"WP-2","SCHEMA-07":"WP-7","SCHEMA-08":"WP-4",
 "SCHEMA-09":"WP-4","SCHEMA-10":"WP-4","SCHEMA-11":"WP-4","SCHEMA-12":"WP-4",
 "SCHEMA-13":"WP-4","SCHEMA-14":"WP-6","SCHEMA-15":"WP-5","SCHEMA-16":"WP-7","SCHEMA-17":"WP-8"}
# default WP per other categories
cat_default = {
 "terminal_outcome":"WP-8","release_artifact":"WP-8","eval_label":"WP-6","dataset_class":"WP-4",
 "label_confidence":"WP-4","mutation_control":"WP-8","adversarial_family":"WP-8","pc_eval_question":"WP-8",
 "diagnostic":"WP-3","action_vocab":"WP-3","lord_roster":"WP-4","cli_command":"WP-7",
 "audit_question":"WP-8","promotion_criterion":"WP-6","pc_obligation":"WP-2","pc_witness":"WP-2",
 "qualification_gate":"WP-4","holdout_rule":"WP-6","teacher_rule":"WP-5","claim_policy":"WP-8",
 "hygiene":"WP-0","reproducibility":"WP-8","secret":"WP-5","successor_rule":"WP-8",
 "commit_rule":"WP-0","parent_import":"WP-0","anti_pattern":"WP-0","work_package":"WP-0",
 "spec_conflict":"WP-0"}
# overrides where holdout/label need distinct owners
overrides = {"HOLD-07":"WP-4","HOLD-08":"WP-0","LABEL-01":"WP-0",
 "MUT-08":"WP-6","MUT-09":"WP-4","MUT-13":"WP-6","MUT-14":"WP-5","MUT-18":"WP-0",
 "CLI-01":"WP-1","CLI-02":"WP-1","CLI-03":"WP-1","CLI-04":"WP-4","CLI-05":"WP-4",
 "CLI-06":"WP-4","CLI-07":"WP-4","CLI-08":"WP-6","CLI-09":"WP-6","CLI-10":"WP-6",
 "CLI-11":"WP-5","CLI-12":"WP-5","CLI-13":"WP-7","CLI-14":"WP-7","CLI-15":"WP-2",
 "CLI-16":"WP-2","CLI-17":"WP-8","CLI-18":"WP-8",
 "CPC-01":"WP-7","CPC-02":"WP-7","CPC-03":"WP-7","CPC-04":"WP-7","CPC-05":"WP-7",
 "CPC-06":"WP-7","CPC-07":"WP-7","CPC-08":"WP-7","CPC-09":"WP-7","CPC-10":"WP-7",
 "PC-RELIAB":"WP-7","PC-VIEWS":"WP-4","PC-REPORT":"WP-7","PC-CONTROLLER":"WP-7",
 "PC-COST":"WP-2","PC-KAPPA":"WP-8","Q-01":"WP-4","Q-02":"WP-4","Q-03":"WP-4",
 "Q-04":"WP-4","Q-05":"WP-4","Q-06":"WP-4","Q-07":"WP-4",
 "LPC-01":"WP-6","LPC-02":"WP-6","LPC-03":"WP-6","LPC-04":"WP-6","LPC-05":"WP-6",
 "LPC-06":"WP-6","LPC-07":"WP-6","LPC-08":"WP-6","LPC-09":"WP-6","LPC-10":"WP-6",
 "LPC-11":"WP-6","LPC-12":"WP-6","LPC-13":"WP-6","LPC-14":"WP-6","LPC-15":"WP-6","LPC-16":"WP-6"}
wp_files = {
 "WP-0":["FOUNDATION_MANIFEST.json","audits/legacy/LEGACY_ARCHAEOLOGY.md","PC_PARENT_MANIFEST.json","pyproject.toml"],
 "WP-1":["src/council/data/lightcurve.py","forge/datasets/factory.py","configs/schemas/LightCurveSchema_v1.json"],
 "WP-2":["src/council/pc/contract.py","src/council/pc/touch.py","src/council/pc/freeze.py","PC_CONTRACT.json"],
 "WP-3":["src/council/evidence/state_builder.py","src/council/detection/period_search.py","src/council/pc/representation.py"],
 "WP-4":["forge/training/trainers/torch.py","forge/tasks/factory.py","forge/calibration/calibrate.py"],
 "WP-5":["forge/teacher/muse/client.py","forge/teacher/muse/budget.py","TEACHER_BUDGET_LEDGER.json"],
 "WP-6":["scripts/qualify_specialist.py","registry/REGISTRY_MANIFEST.json","forge/manifests/QUALIFICATION_PREREG_v1.json"],
 "WP-7":["src/council/controller/policy.py","src/council/lords/loader.py","src/council/reporting/trace.py"],
 "WP-8":["FREEZE_RESULTS.json","MUTATION_RESULTS.json","RELEASE_MANIFEST.json","FINAL_AUDIT.md","FINAL_RESULT.json"]}
wp_tests = {
 "WP-0":["tests/legacy_regression/test_manifest.py"],"WP-1":["tests/unit/test_lightcurve.py","tests/forge/test_object_grouping.py"],
 "WP-2":["tests/pc/test_touch_derivation.py","tests/pc/test_freeze_masks.py"],"WP-3":["tests/unit/test_evidence_schema.py"],
 "WP-4":["tests/forge/test_trainers.py","tests/forge/test_calibration.py"],"WP-5":["tests/forge/test_teacher_schema.py"],
 "WP-6":["tests/registry/test_immutability.py","tests/forge/test_candidate_freeze.py"],"WP-7":["tests/pc/test_runtime_closure.py"],
 "WP-8":["tests/mutation/test_mutants.py","tests/integration/test_cleanroom.py"]}

# parse inventory ids+categories+status
items=[]
for line in INV.read_text(encoding="utf-8").splitlines():
    if line.strip().startswith("- id:"):
        cur={"id":line.split(":")[1].strip()}
        items.append(cur)
    elif items and line.strip().startswith("category:"):
        items[-1]["category"]=line.split(":")[1].strip()
    elif items and line.strip().startswith("status:"):
        items[-1]["status"]=line.split(":")[1].strip()
print(f"INVENTORY_IDS={len(items)}")

def owner(it):
    i=it["id"]; c=it["category"]
    if c=="phase": return phase_wp[i]
    if c=="gate": return gate_wp[i]
    if c=="spec_section": return sec_wp[i]
    if c=="threat": return threat_wp[i]
    if c=="stop": return stop_wp[i]
    if c=="test_class":
        n=int(i.split("-")[1]); return test_wp[f"TEST-{n:02d}"]
    if c=="schema":
        n=int(i.split("-")[1]); return schema_wp[f"SCHEMA-{n:02d}"]
    if i in overrides: return overrides[i]
    if c in cat_default: return cat_default[c]
    return "WP-0"

# phase anchor per WP for spec_phase field
wp_phase = {"WP-0":"PHASE-00","WP-1":"PHASE-02","WP-2":"PHASE-05","WP-3":"PHASE-08",
 "WP-4":"PHASE-11","WP-5":"PHASE-16","WP-6":"PHASE-18","WP-7":"PHASE-22","WP-8":"PHASE-25"}
# gate anchor per WP
wp_gate = {"WP-0":"COL-GATE-00","WP-1":"COL-GATE-02","WP-2":"COL-GATE-04","WP-3":"COL-GATE-06",
 "WP-4":"COL-GATE-08","WP-5":"COL-GATE-11","WP-6":"COL-GATE-12","WP-7":"COL-GATE-16","WP-8":"COL-GATE-18"}

with OUT.open("w", encoding="utf-8") as f:
    f.write("# WORKPLAN_COVERAGE for COUNCIL-PC-v1.0\n# generated_by: scripts/gen_workplan_coverage.py (deterministic)\n")
    f.write("mappings:\n")
    for it in items:
        i=it["id"]; c=it["category"]; st=it.get("status","normative")
        if st=="not_applicable":
            f.write(f"  - item: {i}\n    category: {c}\n    status: not_applicable\n")
            f.write(f"    resolution: SPEC-CONFLICT-01\n    work_package: NONE\n")
            f.write(f"    reason: MST-template item has no Council counterpart; Council HOLD/Q/PC/Sec-64 governs\n")
            continue
        wp=owner(it)
        # spec_phase: for phase items use self; else WP anchor phase
        sp = i if c=="phase" else wp_phase[wp]
        gate = i if c=="gate" else wp_gate[wp]
        files = ";".join(wp_files[wp])
        tests = ";".join(wp_tests[wp])
        # first consumer hints for key firewall items
        fc="NONE"
        if i=="COL-GATE-13": fc="WP-6:qualification-consumes-reveal-once"
        elif i=="COL-GATE-15": fc="WP-7:runtime-consumes-sealed-registry"
        elif i=="HOLD-01": fc="WP-6:reveal-after-GATE-12"
        elif i=="COL-GATE-12": fc="WP-6:freeze-before-reveal"
        elif c=="pc_obligation" and wp=="WP-2": fc="WP-3/WP-7/WP-8"
        elif c=="promotion_criterion": fc="WP-6-or-WP-7"
        f.write(f"  - item: {i}\n    category: {c}\n    status: normative\n")
        f.write(f"    work_package: {wp}\n    spec_phase: {sp}\n")
        f.write(f"    impl_files: {files}\n    tests: {tests}\n    gate: {gate}\n")
        f.write(f"    inputs: {sp}+{gate}-prereqs\n    outputs: {i}-closed\n")
        f.write(f"    failure: BLOCKED-until-new-version\n    first_consumer: {fc}\n")
print(f"WROTE {OUT}")
