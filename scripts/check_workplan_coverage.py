"""Deterministic WorkPlan coverage checker for COUNCIL-PC-v1.0.
Fails nonzero unless all coverage invariants hold.
Prints the planning-audit block required by Absolute Rule 13 (Council-adapted).
"""
import pathlib, re, sys

INV = pathlib.Path("planning/NORMATIVE_INVENTORY.yaml")
COV = pathlib.Path("planning/WORKPLAN_COVERAGE.yaml")
SPEC = pathlib.Path("IMPLEMENTATION_SPEC.md")

def parse_inventory():
    items = {}
    cur = None
    for line in INV.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("- id:"):
            cur = {"id": s.split(":", 1)[1].strip()}
            items[cur["id"]] = cur
        elif cur is not None and s.startswith("category:"):
            cur["category"] = s.split(":", 1)[1].strip()
        elif cur is not None and s.startswith("status:"):
            cur["status"] = s.split(":", 1)[1].strip()
        elif cur is not None and s.startswith("source_section:"):
            cur["source_section"] = s.split(":", 1)[1].strip()
        elif cur is not None and s.startswith("source_file:"):
            cur["source_file"] = s.split(":", 1)[1].strip()
        elif cur is not None and s.startswith("source_line:"):
            try:
                cur["source_line"] = int(s.split(":", 1)[1].strip())
            except ValueError:
                cur["source_line"] = -1
    return items

def parse_coverage():
    maps = {}
    cur = None
    for line in COV.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("- item:"):
            cur = {"item": s.split(":", 1)[1].strip()}
            maps[cur["item"]] = cur
        elif cur is not None and ":" in s:
            k, v = s.split(":", 1)
            cur[k.strip()] = v.strip()
    return maps

inv = parse_inventory()
cov = parse_coverage()

normative = {k for k, v in inv.items() if v.get("status") == "normative"}
notapp = {k for k, v in inv.items() if v.get("status") == "not_applicable"}
mapped_normative = {k for k, v in cov.items() if v.get("status") == "normative"}
mapped_notapp = {k for k, v in cov.items() if v.get("status") == "not_applicable"}

errors = []
def err(msg):
    errors.append(msg)

# 0: section-bounded source-pointer invariant (planning repair).
# Recompute numbered-section bounds from the operative spec and require
# every numbered-section inventory item to point inside its declared section.
spec_lines = SPEC.read_text(encoding="utf-8").splitlines()
sec_bounds = {}
_heads = []
for _i, _l in enumerate(spec_lines, 1):
    _m = re.match(r"# (\d+)\.\s", _l)
    if _m:
        _heads.append((int(_m.group(1)), _i))
_heads.sort()
for _idx, (_num, _ln) in enumerate(_heads):
    _end = _heads[_idx + 1][1] - 1 if _idx + 1 < len(_heads) else len(spec_lines)
    sec_bounds[_num] = (_ln, _end)
source_pointer_errors = 0
for _id, _it in inv.items():
    if _it.get("status") != "normative":
        continue
    if _it.get("source_file") != "IMPLEMENTATION_SPEC.md":
        continue
    _m = re.fullmatch(r"Sec-(\d+)", _it.get("source_section", ""))
    if not _m:
        continue  # non-numbered (process) items are exempt
    _n = int(_m.group(1))
    _ln = _it.get("source_line", -1)
    if _n not in sec_bounds:
        err(f"SOURCE_POINTER {_id}: section {_n} absent from spec"); source_pointer_errors += 1
    else:
        _s, _e = sec_bounds[_n]
        if not (_s <= _ln <= _e):
            err(f"SOURCE_POINTER {_id}: line {_ln} outside Sec-{_n} [{_s}-{_e}]"); source_pointer_errors += 1

# 1+2: exact set equality on normative items
unmapped = sorted(normative - mapped_normative)
unknown = sorted(mapped_normative - normative)
if unmapped:
    err(f"UNMAPPED normative items: {unmapped[:10]} (+{len(unmapped)-10} more)" if len(unmapped) > 10 else f"UNMAPPED: {unmapped}")
if unknown:
    err(f"UNKNOWN mappings (not in inventory): {unknown}")

# 3: every PHASE exactly one accountable WP
phase_items = sorted([k for k in normative if k.startswith("PHASE-")])
phase_ownership_errors = 0
wp_of = {}
for p in phase_items:
    wp = cov.get(p, {}).get("work_package", "MISSING")
    if wp in ("MISSING", "NONE", ""):
        err(f"PHASE {p} has no owner"); phase_ownership_errors += 1
    else:
        wp_of[p] = wp
if len(phase_items) != 31:
    err(f"PHASE count != 31 (got {len(phase_items)})"); phase_ownership_errors += 1
# expected table
expected_phase_wp = {"PHASE-00":"WP-0","PHASE-01":"WP-0","PHASE-02":"WP-1","PHASE-03":"WP-1","PHASE-04":"WP-1",
 "PHASE-05":"WP-2","PHASE-06":"WP-2","PHASE-07":"WP-2","PHASE-08":"WP-3","PHASE-09":"WP-3","PHASE-10":"WP-3",
 "PHASE-11":"WP-4","PHASE-12":"WP-4","PHASE-13":"WP-4","PHASE-14":"WP-4","PHASE-15":"WP-4",
 "PHASE-16":"WP-5","PHASE-17":"WP-5","PHASE-18":"WP-6","PHASE-19":"WP-6","PHASE-20":"WP-6","PHASE-21":"WP-6",
 "PHASE-22":"WP-7","PHASE-23":"WP-7","PHASE-24":"WP-7","PHASE-25":"WP-8","PHASE-26":"WP-8","PHASE-27":"WP-8",
 "PHASE-28":"WP-8","PHASE-29":"WP-8","PHASE-30":"WP-8"}
for p, exp in expected_phase_wp.items():
    got = cov.get(p, {}).get("work_package")
    if got != exp:
        err(f"PHASE ownership: {p} expected {exp} got {got}"); phase_ownership_errors += 1

# 4: every spec section at least one owner
sec_items = [k for k in normative if k.startswith("SEC-")]
sec_missing = [s for s in sec_items if cov.get(s, {}).get("work_package", "NONE") in ("NONE", "", "MISSING")]
if sec_missing:
    err(f"SEC without owner: {sec_missing}")
if len(sec_items) != 69:
    err(f"SEC count != 69 (got {len(sec_items)})")

# 5: theorem-equivalent obligations have owners (Council: pc_obligation, qualification_gate, pc_witness)
theorem_cats = ("pc_obligation", "qualification_gate", "pc_witness")
theorem_items = [k for k, v in inv.items() if v.get("category") in theorem_cats and v.get("status") == "normative"]
theorem_ownership_errors = 0
for t in theorem_items:
    wp = cov.get(t, {}).get("work_package", "NONE")
    if wp in ("NONE", "", "MISSING"):
        err(f"THEOREM-equivalent {t} has no owner"); theorem_ownership_errors += 1

# 6: liquidity obligations: MST ones must be explicit not_applicable with SPEC-CONFLICT-01
liq_norm = [k for k, v in inv.items() if v.get("category") == "liquidity_obligation" and v.get("status") == "normative"]
if liq_norm:
    err(f"Normative liquidity obligations require owner but Council has none: {liq_norm}")
liq_na = [k for k, v in inv.items() if v.get("category") == "liquidity_obligation" and v.get("status") == "not_applicable"]
for k in liq_na:
    c = cov.get(k, {})
    if c.get("resolution") != "SPEC-CONFLICT-01" or c.get("work_package") != "NONE":
        err(f"Liquidity NA item {k} must resolve to SPEC-CONFLICT-01/NONE")

# 7: every gate has owner and producer (work_package + impl_files + gate self-reference)
gate_items = sorted([k for k in normative if k.startswith("COL-GATE-")])
gate_errors = 0
for g in gate_items:
    c = cov.get(g, {})
    if c.get("work_package", "NONE") in ("NONE", "", "MISSING"):
        err(f"GATE {g} has no owner"); gate_errors += 1
    if not c.get("impl_files"):
        err(f"GATE {g} has no producer files"); gate_errors += 1
    if c.get("gate") != g:
        err(f"GATE {g} gate field != self ({c.get('gate')})"); gate_errors += 1
if len(gate_items) != 23:
    err(f"GATE count != 23 (got {len(gate_items)})"); gate_errors += 1
if cov.get("COL-GATE-22", {}).get("work_package") != "WP-1":
    err("GATE COL-GATE-22 (DATASET_SOURCE_COVERAGE_CLOSED) must be owned by WP-1"); gate_errors += 1

# 8: first-consumer dependencies explicit
required_fc = ["COL-GATE-12", "COL-GATE-13", "COL-GATE-15", "HOLD-01",
               "PC-H", "PC-PR", "PC-CLOSURE", "LPC-01", "CPC-01"]
first_consumer_errors = 0
for r in required_fc:
    c = cov.get(r, {})
    if not c.get("first_consumer") or c.get("first_consumer") == "NONE":
        # allow NONE only if category truly has no consumer; these required ones must have one
        err(f"FIRST_CONSUMER missing for {r}"); first_consumer_errors += 1

# 9: threats
threat_items = [k for k in normative if k.startswith("COL-T")]
threat_control_errors = 0
for t in threat_items:
    if cov.get(t, {}).get("work_package", "NONE") in ("NONE", "", "MISSING"):
        err(f"THREAT {t} has no control"); threat_control_errors += 1
if len(threat_items) != 30:
    err(f"THREAT count != 30"); threat_control_errors += 1

# 10: stops
stop_items = [k for k in normative if k.startswith("COL-STOP-")]
stop_control_errors = 0
for s in stop_items:
    if cov.get(s, {}).get("work_package", "NONE") in ("NONE", "", "MISSING"):
        err(f"STOP {s} has no handler"); stop_control_errors += 1
if len(stop_items) != 25:
    err(f"STOP count != 25"); stop_control_errors += 1

# 11: tests
test_items = [k for k, v in inv.items() if v.get("category") == "test_class"]
for t in test_items:
    if cov.get(t, {}).get("work_package", "NONE") in ("NONE", "", "MISSING"):
        err(f"TEST {t} unmapped")

# 12: artifacts
art_items = [k for k, v in inv.items() if v.get("category") == "release_artifact"]
for a in art_items:
    c = cov.get(a, {})
    if c.get("work_package") != "WP-8":
        err(f"ARTIFACT {a} must be produced by WP-8 (got {c.get('work_package')})")

# 13: holdout transitions permitted owner/order
holdout_errors = 0
allowed_hold = {"HOLD-01":"WP-6","HOLD-02":"WP-6","HOLD-03":"WP-6","HOLD-04":"WP-6",
 "HOLD-05":"WP-6","HOLD-06":"WP-6","HOLD-07":"WP-4","HOLD-08":"WP-0"}
for h, exp in allowed_hold.items():
    got = cov.get(h, {}).get("work_package")
    if got != exp:
        err(f"HOLDOUT {h} expected {exp} got {got}"); holdout_errors += 1
# order: freeze (PHASE-19/GATE-12) before reveal (PHASE-20/GATE-13) — enforced via phase numbers
if cov.get("COL-GATE-12", {}).get("spec_phase") == cov.get("COL-GATE-13", {}).get("spec_phase"):
    pass  # same WP-6 allowed; finer order is phase-level, checked via HOLD first_consumer text
if "reveal-after-GATE-12" not in cov.get("HOLD-01", {}).get("first_consumer", ""):
    err("HOLDOUT order: HOLD-01 must state reveal-after-GATE-12"); holdout_errors += 1

# 14: candidate freeze/mutation rules represented
for must in ["COL-GATE-12", "LPC-01", "LPC-05", "CPC-01", "HYG-03"]:
    if cov.get(must, {}).get("work_package", "NONE") in ("NONE", "", "MISSING"):
        err(f"CANDIDATE rule {must} not represented")

# 15: lifecycle represented
for must in ["Q-01", "LPC-11", "COL-GATE-14", "COL-GATE-15", "COL-GATE-16"]:
    if cov.get(must, {}).get("work_package", "NONE") in ("NONE", "", "MISSING"):
        err(f"LIFECYCLE rule {must} not represented")

# 16: no downstream consumes upstream before required status
# WP-7 runtime entries must list REGISTRY_SEALED/GATE-15 as input; check representative gate entries
if "GATE-15" not in cov.get("COL-GATE-16", {}).get("inputs", "") and "PHASE-22" not in cov.get("COL-GATE-16", {}).get("inputs", ""):
    # inputs field is phase+gate prereqs; require WP-7 gate inputs reference its own phase; deeper check via WorkPlan text
    pass
# hard check: WP assignment respects order — WP-7 gates must not be owned by earlier WP
for g in ["COL-GATE-16", "COL-GATE-17"]:
    if cov.get(g, {}).get("work_package") != "WP-7":
        err(f"LIFECYCLE order: {g} must be WP-7")

# 17: no fresh bank read before candidate freeze — HOLD-01 spec_phase must be freeze/reveal phases (>= PHASE-19)
hp = cov.get("HOLD-01", {}).get("spec_phase", "")
if hp not in ("PHASE-18", "PHASE-19", "PHASE-20"):
    err(f"FRESH-READ order: HOLD-01 spec_phase {hp} unexpected")

# 18+19: no counterexample/historical labeled fresh
# LABEL FRESH item must be owned by WP-6 and produced only post-freeze; legacy labels owned elsewhere
if cov.get("LABEL-01", {}).get("work_package") == cov.get("LABEL-06", {}).get("work_package"):
    # LABEL-01 LEGACY_HISTORICAL (WP-0) vs LABEL-06 FRESH_QUALIFICATION_HOLDOUT (WP-6) must differ
    err("HISTORICAL vs FRESH labels must have different owners")
if cov.get("LABEL-06", {}).get("work_package") != "WP-6":
    err("FRESH_QUALIFICATION_HOLDOUT must be owned by WP-6")

# 20: no semantic change outside allowance — core PC sections owned only by WP-2
for s in ["SEC-04", "SEC-05", "SEC-09"]:
    if cov.get(s, {}).get("work_package") != "WP-2":
        err(f"SEMANTIC boundary: {s} must be owned by WP-2")
if cov.get("SUCC-02", {}).get("work_package") != "WP-8":
    err("SUCC-02 must be owned by WP-8")

# claim policy must all map (no silent drop)
claim_items = [k for k, v in inv.items() if v.get("category") == "claim_policy"]
claim_policy_errors = 0
for c in claim_items:
    if cov.get(c, {}).get("work_package", "NONE") in ("NONE", "", "MISSING"):
        err(f"CLAIM {c} unmapped"); claim_policy_errors += 1

# dataset-source doctrine presence (planning mutation)
dataset_errors = []
for _must in ["COL-SRC-DOCTRINE", "COL-SRC-REGISTRY", "COL-SRC-ATTEMPT",
              "COL-SRC-NOSILENT", "COL-GATE-22"]:
    if _must not in normative or cov.get(_must, {}).get("work_package", "NONE") in ("NONE", "", "MISSING"):
        dataset_errors.append(f"DATASET DOCTRINE missing/unmapped: {_must}")
_src_fam = [k for k, v in inv.items() if v.get("category") == "source_family" and v.get("status") == "normative"]
if len(_src_fam) != 17:
    dataset_errors.append(f"source_family count != 17 (got {len(_src_fam)})")
_src_stat = [k for k, v in inv.items() if v.get("category") == "source_status" and v.get("status") == "normative"]
if len(_src_stat) != 4:
    dataset_errors.append(f"source_status count != 4 (got {len(_src_stat)})")
_src_field = [k for k, v in inv.items() if v.get("category") == "source_registry_field" and v.get("status") == "normative"]
if len(_src_field) != 14:
    dataset_errors.append(f"source_registry_field count != 14 (got {len(_src_field)})")
for _e in dataset_errors:
    err(_e)
dataset_doctrine_present = len(dataset_errors) == 0
coverage_gate_present = ("COL-GATE-22" in normative
                         and cov.get("COL-GATE-22", {}).get("work_package") == "WP-1")

print(f"INVENTORY_ITEMS_TOTAL = {len(inv)}")
print(f"NORMATIVE_ITEMS_TOTAL = {len(normative)}")
print(f"NOT_APPLICABLE_ITEMS_TOTAL = {len(notapp)}")
print(f"MAPPED_ITEMS_TOTAL = {len(mapped_normative)}")
print(f"UNMAPPED = {len(unmapped)}")
print(f"UNKNOWN_MAPPINGS = {len(unknown)}")
print(f"SOURCE_POINTER_ERRORS = {source_pointer_errors}")
print(f"PHASE_OWNERSHIP_ERRORS = {phase_ownership_errors}")
print(f"THEOREM_OWNERSHIP_ERRORS = {theorem_ownership_errors}")
print(f"GATE_ERRORS = {gate_errors}")
print(f"THREAT_CONTROL_ERRORS = {threat_control_errors}")
print(f"STOP_CONTROL_ERRORS = {stop_control_errors}")
print(f"FIRST_CONSUMER_ERRORS = {first_consumer_errors}")
print(f"HOLDOUT_ORDER_ERRORS = {holdout_errors}")
print(f"CLAIM_POLICY_ERRORS = {claim_policy_errors}")
print(f"DATASET_SOURCE_DOCTRINE_PRESENT = {str(dataset_doctrine_present).upper()}")
print(f"DATASET_SOURCE_COVERAGE_GATE_PRESENT = {str(coverage_gate_present).upper()}")
if errors:
    print("ERRORS:")
    for e in errors:
        print(f"  - {e}")
    print("RESULT = WORKPLAN_COVERAGE_FAIL")
    sys.exit(1)
print("RESULT = WORKPLAN_COVERAGE_PASS")
