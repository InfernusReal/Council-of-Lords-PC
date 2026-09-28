# COUNCIL-PC-v1.0
## PC-Native Council of Lords Reconstruction
### Governed Exoplanet Vetting, Specialist Forge, Qualification Registry, and Sequential Closure Engine

**Implementation ID:** `COUNCIL-PC-v1.0`

**Short name:** `COL-PC-v1.0`

**Primary target:** rebuild Council of Lords from scratch as a PC-native exoplanet-vetting system in which raw light-curve observations are converted into a versioned, provenance-carrying internal catalogue; representation refinements alter what distinctions are preserved for certification; qualified specialists propose or support epistemic actions; and the system may close only when the sealed vetting target is homogeneous over the represented compatible-world set.

**Primary conceptual parent:** `PERCEPTIVE CLOSURE: IDENTIFYING AUTHORIZATION-RESOURCE COUNTERFACTUALS`

**Legacy implementation parent:** `InfernusReal/Council-Of-Lords`

**Legacy role:** archaeological reference only. The old repository is not a validated scientific parent, not a benchmark authority, and not a source of grandfathered model qualification.

**Hardware target:** local development and model training must remain feasible on a consumer machine with an NVIDIA RTX 3050 4 GB GPU, 32 GB system RAM, and ordinary NVMe storage.

**External teacher target:** Muse Spark 1.3 Contributor through OpenCode, with all teacher use schema-bound, provenance-recorded, budget-capped, and excluded from unverified ground-truth authority.

**Strongest intended terminal artifact:**

\[
\boxed{\texttt{PC\_NATIVE\_COUNCIL\_QUALIFIED}}
\]

meaning that the data, training, registry, runtime, PC semantics, closure logic, qualification gates, adversarial evaluation, and reproducibility obligations in this specification have all closed.

This terminal state does **not** mean that Council confirms exoplanets, replaces established astronomical vetting, or demonstrates production-grade scientific validity. It means the implementation satisfies its own frozen PC-native contract and qualified benchmark program.

---

# 0. Standing scientific rule

This rebuild is a **semantic reconstruction**, not a refactor of the historical repository.

The legacy system remains permanently identified as the historical implementation that approximately followed:

\[
\text{raw light curve}
\rightarrow
\text{manufactured catalogue-like feature vector}
\rightarrow
\text{heuristic red-flag overlay}
\rightarrow
\text{parallel classifiers}
\rightarrow
\text{weighted final verdict}.
\]

Its artifacts, thresholds, model names, handwritten weights, generated fixtures, checkpoints, frontend, backend, and evaluation scripts remain historical evidence of the original idea.

No new artifact may claim that the historical implementation already had the PC semantics introduced here.

No historical classifier is automatically a qualified Lord.

No historical generated dataset is automatically treated as observational data.

No historical confidence value is automatically treated as calibrated probability.

No historical rule such as:

```text
V-shape -> penalty
large radius -> penalty
gas giant -> confidence bonus
specialist X -> 1.4x weight
```

may be silently reinterpreted as a PC representation or authority transition.

The new implementation must define its semantic anchors explicitly and derive resource touch from state change.

The central engineering law is:

\[
\boxed{
\text{Never manually tag an action E/R/A when touch can be derived extensionally.}
}
\]

---

# 1. Purpose

The original Council of Lords contained one genuinely strong architectural idea:

> Raw photometric data should not be passed directly to a generic classifier. A specialized system should first manufacture a task-specific catalogue, expose diagnostics and failure evidence, and then let multiple specialists reason over that structured state.

The old implementation realized this idea immaturely. In the historical repository:

```text
- five named neural classifiers consume essentially the same eight catalogue-style inputs;
- several specialists differ mainly in architecture size, custom loss, threshold, or weighting;
- the final ensemble contains handwritten specialist weights and case-specific boosts/penalties;
- generated parameter distributions are used heavily during training;
- “red flags” alter a scalar decision score instead of changing certificate semantics;
- preprocessing, catalog lookup, false-positive detection, model inference, API behavior,
  and frontend concerns are entangled;
- caches, checkpoints, datasets, node_modules, and exploratory fixtures are tracked together;
- qualification is dominated by aggregate classification metrics and target thresholds.
```

The mature system replaces that with:

\[
\boxed{
\text{Raw Observations}
\rightarrow
\text{Evolving Evidence State}
\rightarrow
\text{PC Representation + Authority}
\rightarrow
\text{Qualified Specialist Actions}
\rightarrow
\text{Sequential Closure}
}
\]

while adding a separate training system:

\[
\boxed{
\text{COL Forge}
\rightarrow
\text{COL Registry}
\rightarrow
\text{Council Engine}
}
\]

The project therefore has two primary scientific products and one binding interface:

```text
COL Forge      -> creates and qualifies specialists
COL Registry   -> freezes qualified specialist artifacts and capability contracts
Council Engine -> performs PC-native sequential vetting using registered specialists
```

---

# 2. Non-goals

This implementation does **not** claim in advance that:

```text
five specialists are optimal;
more specialists are always better;
neural networks are required;
large models are required;
LLMs should participate in runtime classification;
Muse Spark output is ground truth;
weighted voting is an acceptable closure rule;
classifier confidence is authorization;
classifier confidence is calibrated probability;
a red flag should subtract a fixed scalar penalty;
all useful evidence belongs in H immediately;
all represented evidence is authorized for use;
all available catalog metadata may be consumed by every specialist;
all TESS/Kepler-style inputs share one preprocessing path;
synthetic examples can be mixed with observational data without provenance separation;
finite benchmark success identifies a universal scientific guarantee;
PC E/R/A is a universal ontology for astronomy;
closure under this implementation confirms an exoplanet;
frontend polish is part of the scientific core;
API deployment is required before the engine is qualified.
```

A later need for a genuinely new semantic coordinate, evidence type, action boundary, or qualification resource must produce a versioned successor rather than an in-place semantic rewrite.

---

# 3. Architectural parents and frozen source roles

## 3.1 Conceptual parent: Perceptive Closure

The implementation imports the following PC concepts as normative design constraints:

```text
latent worlds X;
sealed target A_Pi;
normalized admitted history H;
representation/certificate relation P_R;
epistemic authority Lambda;
controller observation omega;
source-exposed actions Q;
positive-support successors Succ+;
source atomicity Atom;
extensional E/R/A touch;
target-relative closure;
resource freezes;
closure cost kappa_Pi;
freeze signature K_Pi;
identified-vs-underidentified source semantics.
```

The software may use astronomy-specific names, but semantic equivalence to the frozen PC contract must be documented.

## 3.2 Legacy parent: Council of Lords

The old repository contributes only:

```text
the historical project name;
the raw-light-curve -> internal catalogue ambition;
the idea of heterogeneous specialists;
the existence of adversarial false-positive fixtures;
legacy file formats useful for migration tests;
legacy outputs useful as regression examples;
legacy implementation failures useful as anti-patterns.
```

The old repository does **not** contribute validated model weights, calibrated thresholds, scientific claims, or qualification status.

## 3.3 External teacher

Muse Spark 1.3 Contributor is a development tool.

It may:

```text
propose adversarial scenarios;
propose semantic annotations;
critique training curricula;
cluster or describe failure modes;
propose candidate representation refinements;
write implementation code;
audit manifests;
review dataset leakage reports;
review capability maps;
propose missing diagnostics;
propose deterministic generators.
```

It may not, by itself:

```text
establish observational ground truth;
change sealed benchmark labels;
change a qualified model under the same ID;
authorize a runtime closure;
replace deterministic scientific checks;
rewrite failed evidence as passed evidence;
consume hidden holdout outcomes before model freeze.
```

---

# 4. Core PC object for Council

Fix a finite or finitely represented latent-world universe \(X\) and sealed vetting target:

\[
A_\Pi:X\rightarrow D.
\]

The initial target class set is:

\[
D = \{
\texttt{PLANETARY\_CANDIDATE},
\texttt{ASTROPHYSICAL\_FP},
\texttt{INSTRUMENTAL\_SYSTEMATIC},
\texttt{UNRESOLVED}
\}.
\]

`UNRESOLVED` is an explicit target/output class only when the target definition calls for it. It must not be used to conceal failure to compute closure.

A runtime PC checkpoint is represented conceptually as:

\[
s_t=(H_t,P_{R,t},\Lambda_t,\omega_t,\mathcal C_t,\mathcal M_t),
\]

where:

```text
H_t       normalized authorization-admitted evidence history;
P_R,t     certificate/representation equivalence relation;
Lambda_t  currently licensed epistemic interfaces and conclusion rights;
omega_t   controller-visible observation;
C_t       compatible latent-world set or exact surrogate;
M_t       immutable runtime metadata/provenance not automatically admitted into H.
```

The implementation may use richer internal state, but all theorem-facing/runtime-facing state must project to these semantics.

---

# 5. Target-relative closure

Define the represented compatible-world set:

\[
C_R(s)=\{x:\exists h\in[H(s)]_{P_R(s)}\text{ with }x\sim h\}.
\]

A checkpoint is closed iff:

\[
\boxed{
|\{A_\Pi(x):x\in C_R(s)\}|=1.
}
\]

A closed state may emit only the target class common to the represented compatible worlds.

An open state may:

```text
continue evidence acquisition;
refine representation;
change authority through a legal action;
request another qualified specialist;
abstain;
escalate;
terminate as unresolved under an explicit budget rule.
```

It may not manufacture closure from a majority vote.

---

# 6. Evidence admission H: the custom catalogue becomes an evolving object

The old one-shot catalogue becomes a versioned sequence:

\[
H_0\rightarrow H_1\rightarrow\cdots\rightarrow H_t.
\]

`H` is not a flat NumPy vector.

It is a typed, provenance-carrying evidence object.

Minimum schema:

```text
EvidenceState
├── identity
│   ├── evidence_state_id
│   ├── parent_state_id
│   ├── schema_version
│   └── state_hash
├── observation
│   ├── mission
│   ├── target_id
│   ├── sector_or_quarter
│   ├── cadence
│   ├── time_system
│   ├── flux_definition
│   ├── observation_span
│   └── source_manifest_ref
├── quality
│   ├── mission_quality_flags
│   ├── finite_mask
│   ├── outlier_mask
│   ├── gap_summary
│   └── contamination_flags
├── preprocessing
│   ├── normalization_variant
│   ├── detrending_variant
│   ├── detrending_parameters
│   ├── preserved_raw_reference
│   └── transform_provenance
├── periodicity
│   ├── candidate_periods
│   ├── period_scores
│   ├── alias_graph
│   ├── harmonics
│   └── period_uncertainty
├── transit
│   ├── epoch
│   ├── depth
│   ├── duration
│   ├── ingress_duration
│   ├── egress_duration
│   ├── shape_statistics
│   ├── odd_even_statistics
│   ├── secondary_eclipse_statistics
│   └── transit_uncertainty
├── stellar
│   ├── stellar_radius
│   ├── stellar_mass
│   ├── stellar_temperature
│   ├── source_catalog
│   ├── source_quality
│   └── uncertainty
├── spatial_context
│   ├── centroid_metrics
│   ├── nearby_sources
│   ├── dilution_estimates
│   └── crossmatch_provenance
├── noise
│   ├── robust_scatter
│   ├── red_noise_metrics
│   ├── local_snr
│   └── variability_metrics
├── specialist_observations
│   └── qualified machine-readable evidence only
└── provenance
    ├── per_field_source
    ├── per_field_transform
    ├── producer_version
    ├── creation_time
    └── hash_chain
```

## 6.1 Admission rule

Raw availability is not admission.

A field may exist in:

```text
raw input;
local cache;
external catalog response;
teacher analysis;
intermediate scratch state;
model side channel;
```

without being present in `H`.

Only an explicit source-atomic evidence-admission action may add or change the admitted history.

## 6.2 No silent fallback

Unknown stellar parameters may not silently become solar defaults in theorem-facing or qualification-facing execution.

Fallback values, if supported, must be represented as:

```text
value
fallback=true
fallback_reason
uncertainty
source=DECLARED_DEFAULT
```

and must remain distinguishable from measured/catalog-derived values.

---

# 7. Representation P_R: the red-flag layer becomes certificate refinement

Red flags do **not** alter evidence by subtracting arbitrary penalties.

They affect what histories may remain certificate-equivalent.

Conceptually:

\[
P_R(s)\in Eq(U_H).
\]

Examples of legitimate representation refinements include:

```text
planet-like transit vs grazing eclipsing-binary morphology;
P vs 2P alias distinction;
odd/even depth equality vs inequality;
primary-only vs primary+secondary eclipse structure;
clean target vs contaminated aperture;
stellar-radius-consistent vs inconsistent transit depth;
mission-periodic artifact vs astrophysical periodicity;
high-SNR morphology vs morphology unresolved at current SNR.
```

A diagnostic action may therefore change:

\[
P_R\rightarrow P_R'
\]

without changing the underlying admitted raw evidence.

No fixed score such as `advanced_score += 0.8` is part of the normative representation semantics.

A UI may later display human-friendly warning severities, but those severities are not the certificate relation itself.

---

# 8. Epistemic authority Lambda

`Lambda` encodes what the current system is licensed to consume, invoke, or conclude.

Minimum authority dimensions:

```text
may_use_external_catalogs;
may_use_learned_specialists;
may_use_teacher_derived_development_artifacts;
may_use_synthetic_prior_information;
may_query_additional_observations;
may_emit_planetary_candidate;
may_emit_astrophysical_fp;
may_emit_instrumental_systematic;
may_auto_reject;
may_escalate_to_human;
may_continue_after_budget_warning.
```

Authority is extensional.

A hidden boolean in an orchestration layer is not sufficient if it changes action availability but is not reflected in `Lambda`.

---

# 9. Source-atomic actions and touch derivation

Every source-exposed action \(q\) has a declared pre/post checkpoint boundary.

For every positive-support successor \(s'\):

\[
T_s(q)=
\bigcup_{s'\in Succ^+(s,q)}
\{E:H(s')\neq H(s),\;R:P_R(s')\neq P_R(s),\;A:\Lambda(s')\neq\Lambda(s)\}.
\]

The implementation does not store `touch=["E","R"]` as an authoritative manually authored field.

It stores the relevant pre/post semantic objects and derives touch.

A cached touch field is permitted only when:

```text
it is mechanically generated;
it is bound to the pre/post hashes;
it can be independently recomputed;
it is rejected if recomputation disagrees.
```

Mixed actions remain mixed.

A freeze never invents a partial action that the source interface does not expose.

---

# 10. Initial action vocabulary

The first implementation must support a finite, explicit action vocabulary.

Suggested actions:

```text
LOAD_LIGHTCURVE
APPLY_QUALITY_MASK
NORMALIZE_FLUX
DETREND_VARIANT
SEARCH_PERIOD_BLS
SEARCH_PERIOD_ALTERNATE
FOLD_PERIOD
FIT_TRANSIT_SHAPE
COMPUTE_ODD_EVEN
SEARCH_SECONDARY_ECLIPSE
COMPUTE_VARIABILITY
COMPUTE_CENTROID_DIAGNOSTICS
QUERY_STELLAR_CATALOG
QUERY_NEIGHBOR_CATALOG
ESTIMATE_DILUTION
RUN_MORPHOLOGY_LORD
RUN_PERIODICITY_LORD
RUN_FALSE_POSITIVE_LORD
RUN_STELLAR_LORD
RUN_INSTRUMENT_LORD
RUN_GENERAL_VETTER
REFINE_REPRESENTATION
REQUEST_ADDITIONAL_SECTOR
ESCALATE_HUMAN
STOP_UNRESOLVED
```

Not every deployment must enable every action.

Enabled actions are a function of ordinary preconditions and `Lambda`.

---

# 11. Specialist principle

The core specialist rule is:

\[
\boxed{
\text{A Lord is trained for a scientific role, not merely a different random seed.}
}
\]

A specialist must differ by at least one scientifically meaningful competence axis such as:

```text
task target;
input view;
inductive bias;
training population;
allowed evidence;
loss/objective;
calibration contract;
known applicability domain.
```

Changing only:

```text
seed;
hidden width;
threshold;
custom theatrical loss name;
class weight;
minor activation choice;
```

is insufficient to establish a distinct epistemic role.

---

# 12. Initial Lord roster

The first qualified roster should be small and heterogeneous.

| Lord | Primary role | Preferred model family | Primary input |
|---|---|---|---|
| `MorphologyLord` | transit-shape / eclipsing morphology | small 1D CNN or compact MLP over engineered morphology | folded light curve + morphology features |
| `PeriodicityLord` | period/alias support | gradient boosting or small MLP | period-search summary + alias graph features |
| `FalsePositiveLord` | astrophysical FP discrimination | XGBoost / LightGBM / CatBoost | manufactured catalogue + red-flag diagnostics |
| `StellarPlausibilityLord` | stellar/planet consistency | gradient boosting or small MLP | stellar + inferred transit parameters |
| `InstrumentLord` | mission/systematic signatures | gradient boosting / random forest | quality/systematic/period/noise features |
| `GeneralVetter` | broad learned support | XGBoost / CatBoost or compact MLP | authorized catalogue view |

The roster is a starting point, not a fixed theorem.

No `MetaVetter` may directly convert votes into closure.

A later meta-model may recommend actions or estimate specialist applicability, but closure remains PC-defined.

---

# 13. Hardware and model-size contract

The implementation is intentionally optimized for ordinary classifiers.

## 13.1 Preferred range

Neural specialists should ordinarily remain within:

\[
\boxed{5\times 10^4\text{ to }2\times10^6\text{ trainable parameters}}
\]

A model up to approximately:

\[
\boxed{5\times10^6}
\]

is permitted only with an explicit reason and local training feasibility demonstration.

## 13.2 Preferred model families

```text
Logistic Regression
Linear / kernel SVM where tractable
Random Forest
Extra Trees
XGBoost
LightGBM
CatBoost
small MLP
small 1D CNN
```

Transformers are out of scope for v1.0 unless a specific specialist demonstrates a compelling need.

## 13.3 Resource rule

A specialist architecture is rejected from the default v1.0 search if it requires more than 4 GB VRAM under its frozen training configuration on the target hardware.

CPU training is permitted and expected for classical models.

---

# 14. COL Forge

`COL Forge` is the complete specialist-manufacturing subsystem.

Pipeline:

\[
\text{Raw corpora}
\rightarrow
\text{Dataset Factory}
\rightarrow
\text{Task Factory}
\rightarrow
\text{Training}
\rightarrow
\text{Calibration}
\rightarrow
\text{Stress/Failure Mapping}
\rightarrow
\text{Qualification}
\rightarrow
\text{Registry Promotion}.
\]

Forge may create unlimited experimental candidates.

Only qualification may mint a runtime Lord.

---

# 15. Dataset Factory

The Dataset Factory emits immutable, versioned examples:

\[
D=\{(x_i,y_i,m_i,p_i)\}_{i=1}^{N}
\]

with:

```text
x_i  input view or raw source;
y_i  target label(s);
m_i  metadata and strata;
p_i  provenance and transformation ledger.
```

## 15.1 Dataset classes

Every example must carry exactly one source class:

```text
OBSERVATIONAL_RAW
OBSERVATIONAL_DERIVED
CATALOG_LABELLED
SIMULATED_PHYSICS
SYNTHETIC_STRESS
LLM_PROPOSED_SCENARIO
LEGACY_HISTORICAL
CONTAMINATED_DEVELOPMENT
HIDDEN_HOLDOUT
```

Teacher-generated scenario descriptions are never relabeled as observational data.

## 15.2 Object-level splitting

Train/validation/test splits occur by astrophysical object identity, not by arbitrary rows or windows.

All windows, sectors, derived views, and augmented samples belonging to one protected identity group must remain in the same split unless a specific cross-sector protocol is preregistered.

## 15.3 Mission-aware splitting

Dataset manifests must record mission/source strata so performance can be reported separately for relevant acquisition regimes.

## 15.4 Label confidence

Labels support:

```text
CONFIRMED
HIGH_CONFIDENCE
CATALOG_CANDIDATE
KNOWN_FALSE_POSITIVE
SIMULATED_KNOWN
AMBIGUOUS
UNRESOLVED
```

A task specification decides which label confidence classes are admissible for training and evaluation.

## 15.5 Dataset identity

Each frozen dataset release is identified as:

```text
COL-DATASET-<task>-vMAJOR.MINOR.PATCH
```

with:

```text
manifest.json
source_manifest.json
split_manifest.json
transform_manifest.json
schema.json
checksums.json
leakage_report.json
label_policy.md
```

A changed split, label policy, source population, or transform that can alter results requires a new dataset version.

## 15.6 Exhaustive source-acquisition doctrine (brutal-data foundation)

The scientific intent is:

\[
\boxed{
\text{Acquire broadly, provenance everything, train selectively, test brutally.}
}
\]

Phase 04 is the explicit exhaustive source-acquisition foundation before later task and training phases.
Acquisition is exhaustive-by-default: the implementation must attempt every eligible public data source
family relevant to Council v1.0, record actual acquisition status, and close coverage over a frozen
source registry. Selectivity applies later at training time (TaskSpec populations, allowed evidence,
frozen candidate sets); brutality applies at test time (adversarial suites, stress families, holdout,
mutation controls, clean-room reproduction).

The frozen source registry must contain every eligible public data source family relevant to
Council v1.0, including at minimum the following source-family categories:

```text
OBSERVATIONAL_LIGHTCURVE
PLANET_CANDIDATE_CATALOG
CONFIRMED_PLANET_CATALOG
CERTIFIED_FALSE_POSITIVE
ECLIPSING_BINARY_CATALOG
TCE_CATALOG
ROBOVETTER_METRICS
CENTROID_DIAGNOSTICS
STELLAR_CATALOG
NEIGHBOR_CONTAMINATION_CATALOG
INJECTION_RECOVERY
SCRAMBLED_FALSE_ALARM
INVERTED_FALSE_ALARM
PIPELINE_SYSTEMATIC
SIMULATED_PHYSICS
TEACHER_PROPOSED_ADVERSARIAL
LEGACY_HISTORICAL
```

The registry must explicitly cover relevant public source families such as:

```text
Kepler DR25
Kepler KOIs
Kepler TCEs
Kepler Certified False Positives
Kepler Robovetter metrics
Kepler injection/recovery products
Kepler inverted/scrambled false-alarm products
Kepler eclipsing-binary catalogs
Kepler light curves
K2 candidate/false-positive populations
TESS TOIs
TESS TCE/DV products where eligible/available
TESS light curves
TESS eclipsing-binary sources
MAST mission products
NASA Exoplanet Archive products
Gaia stellar/neighbour/context products
mission-quality/systematics metadata
physically generated adversarial cases
Muse-proposed scenario specifications materialized deterministically
```

These are source families to attempt, not assertions that every named product is guaranteed
available in every environment. No URLs, counts, versions, or availability are asserted here.
The implementation must record actual acquisition status later during execution.

Every frozen source-registry entry must conform to the following entry schema, frozen as version 1
before acquisition begins:

```text
source_id
source_family
source_version_or_release
retrieval_date
retrieval_method
license_or_usage_status
raw_hashes
object_identity_mapping
label_semantics
known_biases
allowed_tasks
split_restrictions
acquisition_status
acquisition_failure_reason
```

Every frozen source entry must terminate in exactly one explicit acquisition state:

```text
INGESTED
INCOMPATIBLE_WITH_DOCUMENTED_REASON
UNAVAILABLE_WITH_ARCHIVED_FAILURE
EXCLUDED_BY_FROZEN_POLICY
```

No silent omission is allowed. A source family that is not attempted, not entered in the registry,
or left in a non-terminal state is a coverage failure, not a scope decision.

This doctrine defines the normative closure gate:

```text
DATASET_SOURCE_COVERAGE_CLOSED
```

The gate requires that every source in the frozen source registry has exactly one of the
terminal acquisition states above, with its status ledger entry, identity reconciliation record,
and acquisition closure audit all frozen and hash-bound. This is coverage closure of the frozen
source registry. It must not be redefined as "all data downloaded."

If full physical acquisition would exceed routine execution resources, the implementation must
distinguish the acquisition framework plus source registry plus status-closure mechanism
(WP-1 foundation) from later actual large data materialization, while still making exhaustive
source coverage explicit and auditable. Large raw products follow the repository hygiene rule:
manifests and hashes are committed; bulky bytes live outside ordinary Git history.

---

# 16. Raw light-curve preservation

The Dataset Factory must retain an immutable reference to the raw observation product used to derive every example.

Derived arrays do not replace raw provenance.

Each transform records:

```text
producer
version
parameters
input_hash
output_hash
random_seed_if_any
quality_mask
units
```

A model artifact that cannot be traced back to its dataset and transformation chain cannot qualify.

---

# 17. Task Factory

A TaskSpec is the unit of supervised learning.

Example:

```yaml
task_id: transit_morphology_v1
inputs:
  - folded_lightcurve
  - transit_duration
  - transit_depth
  - ingress_egress_ratio
allowed_evidence:
  - LIGHTCURVE_NORMALIZED
  - PERIOD_FOLD
  - TRANSIT_GEOMETRY_BASIC
targets:
  - PLANET_LIKE
  - V_SHAPED_EB
  - GRAZING_EB
  - AMBIGUOUS
metric_primary: macro_f1
requires_calibration: true
abstention_required: true
```

## 17.1 Required TaskSpec fields

```text
id
description
input_schema
target_schema
allowed_evidence
forbidden_evidence
population_definition
label_policy
split_policy
augmentation_policy
primary_metric
secondary_metrics
calibration_requirement
abstention_requirement
qualification_thresholds
stress_suites
seed_policy
```

The `allowed_evidence` and `forbidden_evidence` fields are mandatory.

---

# 18. SpecialistSpec

Every trained candidate has a machine-readable SpecialistSpec:

```text
SpecialistSpec
├── id
├── role
├── task
├── input_schema
├── target_schema
├── allowed_evidence
├── forbidden_evidence
├── architecture
├── preprocessing
├── training_distribution
├── seed
├── optimizer_or_estimator
├── calibration_method
├── decision_space
├── abstention_policy
├── applicability_model
├── known_failure_regions
├── benchmark_results
├── artifact_provenance
├── parent_run_ids
└── code_hash
```

Training-time evidence semantics must match runtime evidence semantics.

A model trained using a field that runtime authority later claims is unavailable is disqualified for that runtime view.

---

# 19. Training engine

Training is configuration-driven.

Recommended backend support:

```text
sklearn
xgboost
lightgbm
catboost
pytorch
```

TensorFlow support is optional for legacy migration only; it is not required for v1.0.

Recommended structure:

```text
forge/training/
├── trainers/
│   ├── sklearn.py
│   ├── xgboost.py
│   ├── lightgbm.py
│   ├── catboost.py
│   └── torch.py
├── objectives/
├── losses/
├── schedulers/
├── sampling/
├── search/
├── callbacks/
└── reproducibility/
```

Every run produces:

```text
runs/<run_id>/
├── config.yaml
├── task_spec.json
├── specialist_spec.json
├── dataset_manifest.json
├── split_manifest.json
├── environment.json
├── seed.json
├── checkpoints/
├── raw_metrics.json
├── calibration.json
├── confusion_matrices/
├── strata_metrics.json
├── stress_results.json
├── predictions.parquet
├── failure_cases.parquet
└── run_manifest.json
```

Run IDs are immutable.

---

# 20. Hyperparameter search

The initial search strategy should prefer small structural grids or Bayesian/Optuna-style search with strict resource caps.

No search objective may optimize against the hidden qualification holdout.

Recommended search ordering:

```text
1. semantic input legality;
2. leakage-free split validity;
3. primary validation metric;
4. calibration;
5. abstention quality;
6. stress-family robustness;
7. smaller model;
8. lower inference cost;
9. simpler preprocessing;
10. lower variance across seeds.
```

A larger model does not outrank a smaller one merely because of negligible aggregate metric gain.

---

# 21. Calibration

Every probabilistic Lord must pass calibration analysis.

Required outputs where applicable:

```text
Brier score;
expected calibration error;
reliability bins;
class-conditional calibration;
mission-conditional calibration;
SNR-conditional calibration;
coverage-risk curve;
threshold sensitivity;
abstention coverage.
```

Permitted calibration methods include:

```text
Platt scaling;
isotonic regression;
temperature scaling;
class-conditional calibration when justified.
```

Calibration data must be separate from fitting data.

---

# 22. Abstention

Abstention is first-class.

A Lord output must support:

```text
prediction;
probability_or_score;
uncertainty;
applicability;
abstained;
abstention_reason.
```

The runtime must distinguish:

```text
MODEL_ABSTAIN
MODEL_OOD
EVIDENCE_MISSING
REPRESENTATION_OPEN
AUTHORITY_BLOCKED
CONTROLLER_BUDGET_STOP
```

These are not interchangeable failure modes.

---

# 23. Qualification

A model does not become a Lord because validation accuracy is high.

Qualification is:

\[
\boxed{
Q(M)=
Q_{general}
\land Q_{calibration}
\land Q_{stress}
\land Q_{OOD}
\land Q_{leakage}
\land Q_{reproducibility}
\land Q_{semantic}
}
\]

where each component is an explicit gate.

## 23.1 General performance

Required reporting:

```text
ROC-AUC where meaningful;
PR-AUC where meaningful;
macro/micro F1;
precision;
recall;
confusion matrix;
class support;
confidence intervals or bootstrap intervals when feasible.
```

## 23.2 Conditional performance

At minimum stratify when data permits by:

```text
mission;
SNR;
period;
transit depth;
coverage;
number of observed transits;
stellar type;
contamination regime;
label-confidence class.
```

## 23.3 Stress performance

Each specialist has role-specific adversarial suites.

## 23.4 OOD

Every Lord must expose an OOD/applicability strategy, even if the first implementation is simple.

## 23.5 Leakage

Any detected protected-identity leakage blocks qualification.

## 23.6 Reproducibility

A clean rerun must reproduce the qualifying artifact or reproduce metrics within a frozen tolerance when nondeterminism is unavoidable.

---

# 24. Capability map

Qualification emits a capability map rather than a single score.

Example:

```text
MorphologyLord v2.1
-------------------
V-shaped EB recall               0.96
Planet-like precision            0.93
Low-SNR recall                   0.71
Long-period recall               0.62
Calibration ECE                  0.028
OOD AUROC                        0.81
Abstention coverage at target    0.84

Known weaknesses:
- sparse two-transit events
- strong stellar variability
- severe cadence gaps
```

The exact metrics are illustrative only; the implementation must fill them from sealed evaluation.

The runtime may consume capability metadata to estimate applicability.

It may not convert capability metadata into a hidden fixed ensemble vote weight without a declared controller rule.

---

# 25. Runtime reliability function

If the controller uses specialist reliability, it must be state-dependent and provenance-bound.

A possible interface is:

\[
r_i(s)=f_i(
\text{SNR},
\text{mission},
\text{period regime},
\text{coverage},
\text{OOD score},
\text{calibration region}
).
\]

`r_i(s)` is metadata about expected specialist reliability under the current view.

It is **not** itself the target decision.

The historical pattern:

```text
CHAOS_MASTER = 1.4
CELESTIAL_ORACLE = 1.3
COSMIC_CONDUCTOR = 0.7
```

is forbidden as a default scientific decision rule.

---

# 26. COL Registry

Only qualified artifacts enter the registry.

Recommended layout:

```text
registry/
├── morphology/
│   └── v2.1.0/
│       ├── model.onnx | model.joblib | model.pt
│       ├── specialist_spec.json
│       ├── task_spec.json
│       ├── calibration.json
│       ├── capability_map.json
│       ├── dataset_manifest.json
│       ├── qualification_report.json
│       ├── environment.json
│       ├── signature.json
│       └── checksums.json
└── ...
```

Registry artifacts are immutable.

Any changed model bytes, calibration, preprocessing, evidence contract, target schema, or capability profile requires a new version.

---

# 27. Specialist runtime interface

Every Lord implements a stable interface conceptually equivalent to:

```python
result = lord.evaluate(view)
```

The result schema is:

```text
SpecialistResult
├── specialist_id
├── specialist_version
├── task_id
├── input_view_hash
├── claims
├── probabilities_or_scores
├── uncertainty
├── applicability
├── ood_score
├── abstained
├── abstention_reason
├── diagnostics
├── recommended_actions
├── evidence_refs
├── model_provenance
└── result_hash
```

A specialist may recommend actions.

It may not directly mutate H, P_R, or Lambda.

Only the Council Engine executes source-atomic actions.

---

# 28. PC resource views in training

Forge must be able to construct authorized views:

\[
x_i^{(v)}=View_v(H,P_R,\Lambda).
\]

This permits evaluation under resource restrictions without pretending that every model always sees every feature.

Examples:

```text
PRE_REPRESENTATION_VIEW
POST_ODD_EVEN_REFINEMENT_VIEW
NO_EXTERNAL_STELLAR_VIEW
NO_NEIGHBOR_CATALOG_VIEW
NO_LEARNED_SPECIALIST_VIEW
LIMITED_AUTHORITY_VIEW
```

The system may compare model behavior under these views.

This supports the diagnostic separation:

\[
\boxed{
\text{model failure}
\neq
\text{evidence failure}
\neq
\text{representation failure}
\neq
\text{authority failure}.
}
\]

---

# 29. Muse Spark teacher subsystem

Muse Spark 1.3 Contributor is the default external teacher for v1.0 development.

Recommended structure:

```text
forge/teacher/
├── muse/
│   ├── client.py
│   ├── prompts/
│   ├── schemas/
│   ├── budget.py
│   └── replay.py
├── adversarial_generation/
├── failure_analysis/
├── curriculum/
├── representation_proposals/
└── validation/
```

## 29.1 Teacher jobs

Permitted high-value jobs:

```text
adversarial scenario generation;
hard-negative scenario design;
failure-cluster interpretation;
training curriculum proposals;
missing-diagnostic proposals;
representation-refinement proposals;
code generation and review;
manifest and leakage audit;
specialist critique;
benchmark-case mutation proposals.
```

## 29.2 Structured output only for machine ingestion

Any teacher output entering the pipeline automatically must pass a versioned JSON schema.

Freeform text may be used for human development discussion but may not be machine-ingested as a label without conversion and validation.

## 29.3 Teacher artifact provenance

Every teacher transaction records:

```text
teacher_model
provider
model_route
model_version_if_exposed
prompt_template_id
prompt_hash
input_hash
schema_version
generation_parameters
response_hash
validation_result
review_status
cost_estimate
created_at
```

## 29.4 Budget

The default v1.0 teacher budget is configurable, with an initial project ceiling of:

```text
USD 25.00
```

unless explicitly raised.

The budget tracker must fail closed before exceeding the configured ceiling.

---

# 30. Teacher-generated adversarial scenarios

The preferred teacher pattern is:

\[
\text{Muse proposal}
\rightarrow
\text{schema validation}
\rightarrow
\text{deterministic/physics-aware materializer}
\rightarrow
\text{generated case}
\rightarrow
\text{explicit synthetic provenance}.
\]

The teacher should propose **scenario constraints**, not fabricate trusted telescope measurements.

Example scenario families:

```text
grazing EB resembling a planetary transit;
odd/even asymmetry near detection threshold;
diluted eclipsing binary;
period alias collision;
secondary eclipse near noise floor;
stellar variability aligned with transit period;
mission-periodic instrumental artifact;
contaminated aperture;
sparse two-transit candidate;
contradictory stellar-radius evidence;
high-confidence specialist disagreement;
OOD morphology with plausible catalogue values.
```

Every generated case remains tagged synthetic.

---

# 31. Teacher-assisted failure discovery

After training, collect the failure set:

\[
F=\{x:M(x)\neq y\}
\]

or an analogous continuous-loss subset.

Numerically cluster or stratify failures first.

Muse may then inspect bounded representative summaries and propose semantic hypotheses.

A proposed failure family is not accepted merely because the teacher names it.

Acceptance requires one of:

```text
deterministic feature criterion;
reproducible statistical separation;
new labeled test family;
physical consistency check;
human-reviewed scientific rationale.
```

Accepted failure families are added to the stress suite in a new version.

---

# 32. Runtime Council Engine

Recommended scientific-core package structure:

```text
src/council/
├── pc/
│   ├── contract.py
│   ├── state.py
│   ├── closure.py
│   ├── touch.py
│   ├── freeze.py
│   ├── authority.py
│   ├── representation.py
│   └── atomicity.py
├── data/
│   ├── lightcurve.py
│   ├── provenance.py
│   ├── quality.py
│   └── catalogs.py
├── preprocessing/
│   ├── normalization.py
│   ├── detrending.py
│   └── windows.py
├── detection/
│   ├── period_search.py
│   ├── transit_search.py
│   ├── morphology.py
│   ├── odd_even.py
│   ├── secondary.py
│   └── systematics.py
├── evidence/
│   ├── schema.py
│   ├── state_builder.py
│   ├── admission.py
│   └── views.py
├── lords/
│   ├── base.py
│   ├── loader.py
│   ├── morphology.py
│   ├── periodicity.py
│   ├── false_positive.py
│   ├── stellar.py
│   ├── instrument.py
│   └── general.py
├── controller/
│   ├── policy.py
│   ├── planner.py
│   ├── action_ranker.py
│   └── budget.py
├── registry/
│   ├── reader.py
│   ├── verifier.py
│   └── schemas.py
└── reporting/
    ├── trace.py
    ├── candidate_report.py
    └── audit_report.py
```

The API and frontend are not part of this trusted scientific core.

---

# 33. Controller semantics

The controller chooses among legal source-atomic actions.

It may use:

```text
current PC observation omega;
current open/closed status;
qualified specialist recommendations;
capability metadata;
action cost;
budget;
current compatible-world distinctions;
authorized evidence views.
```

It may not:

```text
peek at hidden labels;
peek at holdout truth;
use forbidden evidence;
call an unqualified model as if registered;
override closure because “confidence is high”;
rewrite P_R after observing target truth.
```

The first controller may be deterministic and heuristic.

A learned controller is a later optional extension.

---

# 34. Action cost

Each action has a nonnegative cost:

\[
c(q)\ge 0.
\]

The initial implementation may use normalized unit costs for controlled PC experiments, while separately tracking real operational cost such as:

```text
CPU time;
GPU time;
external API cost;
catalog-query count;
additional observation requirement;
human escalation.
```

No claim about optimal scientific cost may be made from arbitrary unit costs without stating the convention.

---

# 35. Closure cost and freeze geometry

For a proper closing policy \(\rho\):

\[
\kappa_\Pi(s)
=
\inf_{\rho}
\max_{\tau\in Leaves(\rho)}
\sum_{q\in\tau} c(q).
\]

For each freeze set:

\[
F\subseteq\{E,R,A\},
\]

remove every source action whose mechanically derived touch intersects \(F\).

Compute:

\[
K_\Pi=
(\kappa_\Pi^{\neg F})_{F\subseteq\{E,R,A\}}
\]

in coordinate order:

```text
EMPTY
E
R
A
ER
EA
RA
ERA
```

when exact computation is feasible on the controlled evaluation instance.

These experiments diagnose the implementation's resource dependence.

They are not automatically prevalence claims about astronomy.

---

# 36. Mandatory PC evaluation questions

The v1.0 benchmark program must include controlled cases addressing:

```text
Can closure occur without new evidence admission?
Can closure occur without representation refinement?
Can closure occur without authority-changing actions?
Does removing external stellar evidence create finite fallback or structural failure?
Can morphology diagnostics substitute for additional evidence?
Does a learned specialist reduce closure cost without becoming structurally necessary?
Can two behaviorally similar pipelines have different resource dependence under different anchors?
Does the runtime refuse unique resource attribution when H/P_R/Lambda/Atom are underidentified?
```

---

# 37. Identification gate

PC freezes are meaningful only after the resource counterfactual is identified by the declared semantics.

Before computing a theorem-facing or claim-facing freeze signature, the experiment must freeze:

```text
H semantics;
P_R semantics;
Lambda semantics;
source action identities;
pre/post checkpoints;
positive-support successor semantics;
atomicity boundary;
target A_Pi;
cost convention.
```

If these are not fixed sufficiently to determine touch, the result is:

```text
BOUNDARY_UNDERIDENTIFIED
```

not a guessed E/R/A label.

---

# 38. Independent touch reconstruction

Every release-level PC benchmark must support two differently structured touch derivations.

Example:

```text
primary: direct semantic object comparison;
independent: serialized canonical-state comparison using separately implemented equality logic.
```

Any disagreement blocks the freeze result.

---

# 39. Red-flag diagnostic library

The first representation-diagnostic library should include, where data permits:

```text
V/U morphology;
odd/even depth asymmetry;
secondary eclipse;
period harmonics and aliases;
transit-duration consistency;
stellar-radius/depth consistency;
centroid shift;
neighbor contamination;
mission systematic-period coincidence;
strong stellar variability;
low effective SNR;
insufficient transit count;
severe cadence gaps;
model OOD;
cross-specialist semantic disagreement.
```

A diagnostic has:

```text
diagnostic_id
input evidence requirements
algorithm/version
output schema
uncertainty
representation effect rule
source action boundary
provenance
```

The diagnostic result itself is evidence only if an evidence-admission action admits it.

Its representation consequence is separate.

---

# 40. Adversarial corpus

The development adversarial corpus must contain at minimum:

```text
clean planetary transits;
grazing eclipsing binaries;
detached eclipsing binaries;
contact binaries;
diluted/blended binaries;
stellar activity;
rotational variability;
instrument artifacts;
period aliases;
secondary eclipses;
very low SNR candidates;
two-transit sparse events;
long-period candidates;
strong data gaps;
centroid contamination;
contradictory stellar metadata;
OOD catalogue values;
OOD light-curve morphology;
calibration-edge cases;
specialist disagreement cases.
```

Legacy fixtures may be imported only under:

```text
LEGACY_HISTORICAL
```

and cannot serve as fresh holdout evidence.

---

# 41. Fresh holdout policy

Before final specialist promotion, freeze a new qualification holdout.

The holdout must be inaccessible to:

```text
model fitting;
hyperparameter search;
threshold search;
teacher scenario generation conditioned on outcome;
manual model repair;
feature selection based on holdout residual;
representation-rule tuning based on holdout residual.
```

One reveal per qualification campaign.

After reveal, the bank becomes historical for future model versions.

A new major qualification campaign requires a new hidden bank.

---

# 42. Historical-vs-fresh labels

Every evaluation row carries one of:

```text
LEGACY_HISTORICAL
DEVELOPMENT
INTERNAL_VALIDATION
TEACHER_GENERATED_DEVELOPMENT
CONTAMINATED_CANARY
FRESH_QUALIFICATION_HOLDOUT
CLEANROOM_POST_FREEZE
FORMAL_PC_CONSTRUCTED
OBSERVATIONAL_EXTERNAL_TEST
```

No historical result may be relabeled fresh.

---

# 43. Mutation controls

Mandatory semantic mutants include:

```text
raw scratch field silently admitted into H;
representation flag changes without P_R change;
P_R changes but touch omits R;
authority changes action availability without Lambda change;
manual touch label overrides derived touch;
freeze removes only part of a mixed source-atomic action;
hidden label leaked into controller observation;
holdout row appears in training identity group;
model trained with forbidden evidence;
registry model bytes changed under same version;
calibration file from another model version;
capability map attached to wrong artifact;
unqualified model loaded as qualified;
teacher output accepted as observational ground truth;
teacher prompt contains hidden holdout outcome;
synthetic provenance dropped;
solar-default fallback presented as measured stellar data;
legacy fixed specialist weights reintroduced;
majority vote bypasses closure;
red flag directly subtracts arbitrary verdict score;
API/frontend mutates scientific state outside engine;
```

Every relevant suite must kill its assigned mutants.

---

# 44. Threat matrix

Freeze controls for at least:

```text
COL-T01  train/test identity leakage
COL-T02  sector/window leakage across object split
COL-T03  catalog target leakage
COL-T04  teacher-as-ground-truth contamination
COL-T05  hidden holdout seen before model freeze
COL-T06  post-hoc threshold tuning on holdout
COL-T07  post-hoc representation tuning on holdout
COL-T08  manually authored E/R/A touch
COL-T09  underidentified semantic boundary treated as identified
COL-T10  scratch availability confused with H admission
COL-T11  representation score confused with P_R
COL-T12  action availability changed outside Lambda
COL-T13  mixed atomic action illegally split by freeze
COL-T14  fixed model weight treated as epistemic reliability
COL-T15  classifier confidence treated as closure
COL-T16  calibration omitted but probability language used
COL-T17  synthetic and observational data merged without provenance
COL-T18  legacy checkpoint promoted without requalification
COL-T19  fallback stellar values presented as observations
COL-T20  model artifact not bound to exact dataset manifest
COL-T21  registry artifact mutated under same semantic version
COL-T22  Muse budget exceeded silently
COL-T23  Muse route/model change not recorded
COL-T24  LLM generated numerical astronomy accepted without deterministic validation
COL-T25  frontend/API logic changes target decision semantics
COL-T26  finite benchmark success upgraded to scientific confirmation
COL-T27  unresolved state forced into binary verdict
COL-T28  OOD case receives ordinary confident decision
COL-T29  hidden authority side channel
COL-T30  source atomicity moved after freeze evaluation
```

---

# 45. Stop conditions

```text
COL-STOP-01 conceptual PC contract cannot be pinned
COL-STOP-02 legacy repository source snapshot cannot be pinned for archaeology
COL-STOP-03 target A_Pi changes after benchmark freeze
COL-STOP-04 H semantics change after PC foundation freeze
COL-STOP-05 P_R semantics change after PC foundation freeze
COL-STOP-06 Lambda semantics change after PC foundation freeze
COL-STOP-07 source atomicity changes without successor version
COL-STOP-08 independent touch reconstruction disagrees
COL-STOP-09 holdout accessed before candidate freeze
COL-STOP-10 protected identity leakage detected
COL-STOP-11 teacher output used as unverified ground truth
COL-STOP-12 model uses forbidden evidence
COL-STOP-13 qualification report cannot be reproduced
COL-STOP-14 registered bytes differ from qualification bytes
COL-STOP-15 calibration mismatch
COL-STOP-16 closure bypassed by majority vote or confidence threshold
COL-STOP-17 manual E/R/A labels consumed as truth
COL-STOP-18 synthetic provenance lost
COL-STOP-19 external API key or secret enters repository
COL-STOP-20 teacher budget ceiling exceeded
COL-STOP-21 runtime requires >4 GB VRAM for default qualified roster without versioned exception
COL-STOP-22 frontend/API becomes required for scientific core execution
COL-STOP-23 finite success described as exoplanet confirmation
COL-STOP-24 a newly required semantic coordinate is added in place
COL-STOP-25 resource exhaustion interpreted as scientific impossibility
```

---

# 46. Work packages

The project uses nine work packages.

## WP-0 — Foundation freeze and archaeology

Pin:

```text
legacy repository commit;
legacy README;
legacy training scripts;
legacy ensemble logic;
legacy converter;
legacy fixture inventory;
PC paper version;
this implementation specification;
initial threat matrix;
initial target ontology;
initial software environment.
```

Produce:

```text
LEGACY_ARCHAEOLOGY.md
LEGACY_FILE_MANIFEST.json
PC_PARENT_MANIFEST.json
FOUNDATION_MANIFEST.json
```

Gate:

```text
FOUNDATION_FROZEN
```

## WP-1 — Trusted data core

Implement:

```text
LightCurve type;
raw provenance;
quality handling;
normalization;
detrending interfaces;
immutable transform manifests;
dataset identity grouping;
Dataset Factory skeleton.
```

Tests:

```text
raw bytes preserved;
unit metadata preserved;
no silent defaults;
object grouping exact;
deterministic transforms where declared;
all outputs hashed.
```

Gate:

```text
DATA_CORE_CERTIFIED
```

## WP-2 — PC semantic core

Implement:

```text
H;
P_R;
Lambda;
omega;
A_Pi;
Action;
Atom;
Succ+;
closure;
touch derivation;
freeze masks;
controlled exact planner.
```

Mandatory finite sanity witnesses:

```text
pure E action;
pure R action;
pure A action;
mixed ER action;
mixed EA action;
mixed RA action;
mixed ERA action;
open state;
closed state;
R-freeze finite fallback;
R-freeze structural failure;
boundary-underidentified fixture.
```

Gate:

```text
PC_CORE_CERTIFIED
```

## WP-3 — Catalogue and diagnostic reconstruction

Implement the evolving EvidenceState and first diagnostics.

The old `SupremeTelescopeConverter` must **not** be ported monolithically.

Decompose it into independently testable operators.

Required first outputs:

```text
period candidates;
transit summary;
noise summary;
odd/even diagnostic;
secondary-eclipse diagnostic;
stellar context;
contamination context where available;
provenance for all fields.
```

Gate:

```text
CATALOGUE_ENGINE_CERTIFIED
```

## WP-4 — COL Forge

Implement:

```text
Dataset Factory;
Task Factory;
SpecialistSpec;
training adapters;
run manifests;
calibration pipeline;
stress harness;
capability map builder;
qualification engine.
```

Train only development candidates.

No registry promotion yet.

Gate:

```text
FORGE_OPERATIONAL
```

## WP-5 — Muse teacher and adversarial development

Implement:

```text
OpenCode client;
secret isolation;
budget ceiling;
structured schemas;
prompt hashing;
response caching;
replay ledger;
adversarial scenario generator;
failure-cluster analyst;
representation-proposal schema.
```

Teacher is development-only.

Gate:

```text
TEACHER_PIPELINE_CERTIFIED
```

## WP-6 — Specialist qualification and registry

Freeze:

```text
TaskSpecs;
training populations;
validation populations;
qualification thresholds;
hidden holdout;
model candidate set;
calibration protocol;
stress suites.
```

Train/freeze candidate specialists.

Reveal holdout once.

Promote only qualified artifacts.

Gate:

```text
INITIAL_LORDS_QUALIFIED
```

## WP-7 — Council runtime integration

Integrate registry Lords into the PC engine.

Requirements:

```text
specialists receive only authorized views;
specialists cannot mutate state;
controller executes actions;
red flags act through representation semantics;
closure is PC-defined;
unresolved remains legal;
all runtime transitions are logged and replayable.
```

Gate:

```text
COUNCIL_RUNTIME_CERTIFIED
```

## WP-8 — Freeze geometry, clean-room, final seal

Run:

```text
resource freezes;
controlled closure-cost analysis;
independent touch reconstruction;
clean-room replay;
registry verification;
mutation campaign;
legacy regression import;
adversarial suite;
final reproducibility pass.
```

Terminal gate:

```text
PC_NATIVE_COUNCIL_QUALIFIED
```

---

# 47. Normative phase map

```text
PHASE 00  pin legacy repository + PC parent + implementation spec
PHASE 01  legacy archaeology and anti-pattern ledger
PHASE 02  raw light-curve type + provenance core
PHASE 03  preprocessing primitives
PHASE 04  Dataset Factory foundation + frozen public-source registry + exhaustive source acquisition + source-status ledger + identity reconciliation + acquisition closure audit
PHASE 05  PC state types H/P_R/Lambda/omega/A_Pi
PHASE 06  action/atomicity/touch/closure engine
PHASE 07  exact freeze planner + finite sanity fixtures
PHASE 08  catalogue schema + state builder
PHASE 09  period/transit/noise diagnostic primitives
PHASE 10  representation refinement engine
PHASE 11  Task Factory + SpecialistSpec
PHASE 12  classical trainer adapters
PHASE 13  PyTorch compact neural trainer
PHASE 14  calibration + abstention + OOD interfaces
PHASE 15  qualification harness
PHASE 16  Muse teacher infrastructure
PHASE 17  teacher adversarial/development generation
PHASE 18  initial specialist search
PHASE 19  candidate freeze
PHASE 20  fresh qualification holdout reveal
PHASE 21  registry promotion
PHASE 22  Council controller integration
PHASE 23  authorized resource views
PHASE 24  runtime trace/replay
PHASE 25  PC freeze geometry
PHASE 26  mutation/falsification campaign
PHASE 27  clean-room reproduction
PHASE 28  optional API
PHASE 29  optional frontend
PHASE 30  final seal/release
```

The API/frontend phases may be omitted without blocking the scientific terminal gate.

---

# 48. Gate ladder

```text
COL-GATE-00  FOUNDATION_FROZEN
COL-GATE-01  LEGACY_ARCHAEOLOGY_COMPLETE
COL-GATE-02  DATA_CORE_CERTIFIED
COL-GATE-03  DATASET_FACTORY_CERTIFIED
COL-GATE-04  PC_CORE_CERTIFIED
COL-GATE-05  TOUCH_DERIVATION_INDEPENDENT_AGREEMENT
COL-GATE-06  CATALOGUE_ENGINE_CERTIFIED
COL-GATE-07  REPRESENTATION_ENGINE_CERTIFIED
COL-GATE-08  FORGE_OPERATIONAL
COL-GATE-09  CALIBRATION_PIPELINE_CERTIFIED
COL-GATE-10  QUALIFICATION_HARNESS_CERTIFIED
COL-GATE-11  TEACHER_PIPELINE_CERTIFIED
COL-GATE-12  SPECIALIST_CANDIDATE_SET_FROZEN
COL-GATE-13  FRESH_HOLDOUT_REVEALED_ONCE
COL-GATE-14  INITIAL_LORDS_QUALIFIED
COL-GATE-15  REGISTRY_SEALED
COL-GATE-16  COUNCIL_RUNTIME_CERTIFIED
COL-GATE-17  RESOURCE_VIEW_AUDIT_PASSED
COL-GATE-18  PC_FREEZE_GEOMETRY_RECOMPUTED
COL-GATE-19  MUTATION_SUITE_PASSED
COL-GATE-20  CLEANROOM_REPRODUCTION_PASSED
COL-GATE-21  PC_NATIVE_COUNCIL_QUALIFIED
COL-GATE-22  DATASET_SOURCE_COVERAGE_CLOSED
```

First exact gate failure blocks downstream consumption until fixed in a new artifact version.

---

# 49. Legacy migration policy

The old repository is mined, not ported wholesale.

## 49.1 Preserve

```text
project name;
conceptual history;
raw sample files with provenance labels;
legacy fixtures;
historical model outputs for regression comparison;
historical README and instructions;
training-script snapshots;
ensemble-script snapshots;
converter snapshots.
```

## 49.2 Do not preserve as normative implementation

```text
node_modules;
__pycache__;
.vite build artifacts;
old checkpoints as qualified models;
old scaler pickles as qualified preprocessing;
handwritten model weights;
fixed confidence bonuses;
custom theatrical losses without scientific justification;
monolithic converter architecture;
solar-default substitution as normal evidence;
API exception dumps as scientific output;
frontend-dependent scientific behavior.
```

## 49.3 Legacy model replay

Historical models may be wrapped under:

```text
LEGACY_UNQUALIFIED
```

for side-by-side regression only.

They may never enter a PC closure policy as qualified evidence producers unless retrained/requalified through Forge.

---

# 50. Legacy anti-pattern findings

The archaeology phase should explicitly preserve the following findings from the old source:

```text
The named specialists are largely parallel neural classifiers over the same eight catalogue-style features.
Different “specialties” are often encoded through altered losses, layer widths, thresholds, or class weights rather than independent scientific views.
The ensemble applies hard-coded specialist weights and context-specific boosts/penalties.
The converter bundles catalog lookup, defaults, detrending, period detection, transit characterization, and false-positive scoring.
Generated training distributions are presented using NASA parameter ranges but are still synthetic draws.
Several stress suites and false-positive fixture families are valuable as historical adversarial ideas.
The repository tracks generated caches, binary checkpoints, frontend dependencies, and datasets together.
```

This anti-pattern ledger is a required design input.

---

# 51. Reproducibility and sealing

Every release-level artifact must be hash-addressable.

Minimum release package:

```text
RELEASE_MANIFEST.json
SOURCE_COMMIT.txt
ENVIRONMENT_LOCK.*
DATASET_MANIFESTS/
TASK_SPECS/
SPECIALIST_SPECS/
REGISTRY_MANIFEST.json
QUALIFICATION_REPORTS/
PC_CONTRACT.json
ACTION_SCHEMA.json
ATOMICITY_SCHEMA.json
TOUCH_RECOMPUTATION.json
FREEZE_RESULTS.json
MUTATION_RESULTS.json
TEACHER_BUDGET_LEDGER.json
TEACHER_PROVENANCE_MANIFEST.json
LEGACY_ARCHAEOLOGY.md
FINAL_AUDIT.md
FINAL_RESULT.json
```

Failed qualification attempts and negative results are preserved.

Do not rewrite history into a clean success narrative.

---

# 52. Secrets and external services

OpenCode API keys must never be committed.

Use environment variables or a local secret manager.

Repository rules:

```text
.env ignored;
.env.example contains names only;
no API keys in logs;
no authorization headers in cached HTTP traces;
provider responses stored only after secret scrubbing;
request/response hashes stored separately from credentials.
```

External catalog credentials, if ever required, follow the same rule.

---

# 53. Recommended dependency policy

Use `pyproject.toml` as the root Python package manifest.

Prefer a small scientific stack:

```text
numpy
pandas
scipy
scikit-learn
astropy
lightkurve or equivalent only if justified
xgboost
lightgbm
catboost
pytorch
pydantic
pyyaml
orjson
joblib
pytest
hypothesis
ruff
mypy
```

Optional dependencies are grouped.

The project should not require TensorFlow merely to run the core engine.

---

# 54. Test classes

```text
unit tests;
property tests;
schema tests;
provenance tests;
leakage tests;
model-interface tests;
calibration tests;
registry integrity tests;
PC semantic tests;
touch derivation tests;
freeze tests;
mutation tests;
legacy regression tests;
clean-room reproduction tests.
```

Scientific assertions should not be hidden inside ad hoc scripts named `ultimate_test.py` or `brutal_reality_test.py` without formal test metadata.

Historical names may survive only as fixture labels.

---

# 55. CLI surface

Before any web UI, ship a deterministic CLI.

Suggested commands:

```text
col data ingest
col data build
col data audit
col task validate
col train run
col train search
col calibrate
col qualify
col registry verify
col registry list
col teacher generate
col teacher audit
col council analyze
col council replay
col pc touch
col pc close
col pc freeze
col audit full
```

Each command emits machine-readable JSON in addition to human-readable summaries where appropriate.

---

# 56. Runtime report

A Council analysis report should contain:

```text
target identity;
raw-source provenance;
EvidenceState hash chain;
actions executed;
pre/post checkpoint IDs;
derived touch for each action;
representation refinements;
authority transitions;
specialist versions;
specialist inputs by authorized view hash;
specialist abstentions/OOD flags;
compatible-world or surrogate state summary;
open/closed status at each checkpoint;
terminal target class if closed;
escalation/unresolved reason if not closed;
cost ledger;
replay manifest.
```

It must not present a closed target class as “confirmed exoplanet.”

---

# 57. Optional API

Only after `COUNCIL_RUNTIME_CERTIFIED` may an API be added.

The API is an adapter over the engine.

It may not implement:

```text
scientific preprocessing;
model selection;
red-flag scoring;
closure rules;
authority logic;
representation mutation.
```

Those belong in the core engine.

---

# 58. Optional frontend

The frontend is purely observational/control-plane UI.

It may display:

```text
light curve;
periodogram;
folded transit;
evidence catalogue;
representation distinctions;
specialist outputs;
action trace;
closure state;
provenance;
uncertainty;
freeze diagnostics.
```

It may request legal engine actions.

It may not calculate the verdict independently.

---

# 59. Initial implementation priorities

The first implementation sprint should **not** begin with model training.

Priority order:

```text
1. repository reset / clean branch;
2. pyproject + package skeleton;
3. raw data/provenance types;
4. PC semantic types;
5. closure/touch/freeze finite engine;
6. EvidenceState schema;
7. deterministic catalogue primitives;
8. Dataset Factory;
9. Task Factory;
10. classical baseline specialists;
11. qualification harness;
12. Muse teacher;
13. compact CNN where justified;
14. registry;
15. Council controller;
16. clean-room audit;
17. optional API/frontend.
```

This order prevents an attractive model demo from defining semantics retroactively.

---

# 60. Initial baselines

Before custom neural specialists, train simple baselines for every TaskSpec where possible:

```text
majority/prior baseline;
logistic regression;
random forest / extra trees;
gradient boosting;
XGBoost / LightGBM / CatBoost.
```

A neural model must beat or complement strong classical baselines on its declared role to justify added complexity.

---

# 61. Promotion criteria for a Lord

A candidate may enter the registry only if:

```text
TaskSpec is frozen;
input schema is frozen;
allowed/forbidden evidence is frozen;
dataset and split manifests are frozen;
protected-identity leakage is zero;
training is reproducible;
calibration requirement passes;
abstention requirement passes;
OOD/applicability requirement passes;
role-specific stress suite passes;
fresh qualification holdout requirement passes;
capability map is generated;
known failure regions are disclosed;
artifact bytes are hashed;
registry package verifies cleanly;
no hidden teacher dependency exists at runtime unless explicitly declared.
```

Aggregate accuracy alone can never satisfy this list.

---

# 62. Council candidate promotion criteria

The complete runtime may enter final PC evaluation only if:

```text
all loaded Lords are registry-qualified;
PC target is frozen;
H/P_R/Lambda semantics are frozen;
action/atomicity boundary is frozen;
independent touch derivation agrees;
controller is deterministic or fully seed-bound;
all resource views enforce allowed evidence;
open states cannot emit authoritative closed verdicts;
mutation controls pass;
replay is deterministic under declared conditions.
```

---

# 63. Terminal states

The project may terminate as:

```text
PC_NATIVE_COUNCIL_QUALIFIED
QUALIFIED_WITH_DECLARED_LIMITATIONS
FORGE_QUALIFIED_RUNTIME_BLOCKED
PC_SEMANTICS_UNDERIDENTIFIED
SPECIALIST_QUALIFICATION_FAILED
DATASET_INTEGRITY_FAILED
HOLDOUT_CONTAMINATED
TEACHER_BUDGET_EXHAUSTED
RESOURCE_LIMIT_REACHED
ARCHITECTURE_SUCCESSOR_REQUIRED
```

`RESOURCE_LIMIT_REACHED` is not scientific impossibility.

`SPECIALIST_QUALIFICATION_FAILED` is not evidence that the task is impossible.

`PC_SEMANTICS_UNDERIDENTIFIED` is not permission to guess the missing boundary.

---

# 64. Architecture-successor rule

If a later exact obstruction shows that the frozen architecture requires a genuinely new semantic coordinate or source intervention not expressible within:

\[
(H,P_R,\Lambda,\omega,Q,Succ^+,A_\Pi,Atom),
\]

or requires a materially different target ontology, then:

```text
1. preserve the failed architecture;
2. preserve the exact witness;
3. diagnose the missing resource;
4. seal v1.0 honestly;
5. create COUNCIL-PC-v1.1 or v2.0 as appropriate;
6. add only the newly justified semantic change;
7. rerun affected data/training/qualification/runtime stages.
```

No new coordinate is silently inserted into the existing release.

---

# 65. Formal repository layout

Recommended clean-room repository:

```text
Council-Of-Lords/
├── README.md
├── IMPLEMENTATION_SPEC.md
├── pyproject.toml
├── uv.lock | poetry.lock | requirements.lock
├── .gitignore
├── .env.example
├── LICENSE
├── CITATION.cff
│
├── src/
│   └── council/
│       ├── pc/
│       ├── data/
│       ├── preprocessing/
│       ├── detection/
│       ├── evidence/
│       ├── lords/
│       ├── controller/
│       ├── registry/
│       ├── reporting/
│       └── cli/
│
├── forge/
│   ├── datasets/
│   ├── tasks/
│   ├── training/
│   ├── calibration/
│   ├── qualification/
│   ├── stress/
│   ├── teacher/
│   └── manifests/
│
├── registry/
│   └── .gitkeep
│
├── configs/
│   ├── tasks/
│   ├── specialists/
│   ├── controller/
│   ├── pc/
│   └── teacher/
│
├── benchmarks/
│   ├── development/
│   ├── adversarial/
│   ├── pc_constructed/
│   └── manifests/
│
├── data/
│   ├── README.md
│   ├── manifests/
│   └── .gitkeep
│
├── runs/
│   └── .gitkeep
│
├── audits/
│   ├── legacy/
│   ├── leakage/
│   ├── qualification/
│   ├── pc/
│   ├── mutation/
│   └── release/
│
├── scripts/
│   ├── migrate_legacy_fixtures.py
│   ├── build_dataset.py
│   ├── train_specialist.py
│   ├── qualify_specialist.py
│   ├── run_council.py
│   └── final_audit.py
│
├── tests/
│   ├── unit/
│   ├── property/
│   ├── integration/
│   ├── pc/
│   ├── forge/
│   ├── registry/
│   ├── mutation/
│   └── legacy_regression/
│
└── legacy/
    ├── README.md
    └── manifests/
```

Large raw data, generated run outputs, model binaries, and external corpora should not be committed casually to ordinary Git history.

Use manifests and an external artifact strategy where appropriate.

---

# 66. Initial schemas to freeze

Before significant training, freeze version 1 of:

```text
LightCurveSchema
EvidenceStateSchema
RepresentationSchema
AuthoritySchema
ActionSchema
CheckpointSchema
SpecialistResultSchema
TaskSpecSchema
SpecialistSpecSchema
DatasetManifestSchema
RunManifestSchema
QualificationReportSchema
CapabilityMapSchema
RegistryEntrySchema
TeacherTransactionSchema
CouncilTraceSchema
FreezeResultSchema
```

Schema evolution follows semantic versioning.

---

# 67. Final audit questions

The final auditor must be able to answer yes/no with evidence for:

```text
Can every qualified model be traced to exact training data and code?
Can every dataset row be traced to a source class and protected identity?
Can every runtime feature be traced to admitted evidence?
Can every specialist input be proven authorized by its view?
Can every E/R/A touch be independently recomputed?
Can every representation refinement be traced to a declared diagnostic/action?
Can every authority change be traced to Lambda?
Can every closed verdict be recomputed from the frozen target and represented compatible worlds?
Can every open state be shown not to bypass closure?
Can every teacher-derived artifact be distinguished from ground truth?
Can every holdout claim be shown uncontaminated?
Can every registry artifact be byte-verified?
Can the system run without the frontend?
Can the scientific core run without an LLM at inference time?
Can the final release be replayed from its manifests?
```

Any `NO` must either block the terminal claim or appear as an explicit declared limitation with a weaker terminal state.

---

# 68. Final implementation doctrine

The mature Council of Lords is not:

```text
five classifiers voting on a catalogue.
```

It is:

\[
\boxed{
\textbf{a governed sequential scientific-inference machine}
}
\]

with three separable systems:

\[
\boxed{
\begin{array}{c}
\textbf{COL Forge}\\
\text{datasets + tasks + training + calibration + qualification}\\[4pt]
\downarrow\\[4pt]
\textbf{COL Registry}\\
\text{versioned qualified specialists + capability contracts}\\[4pt]
\downarrow\\[4pt]
\textbf{Council Engine}\\
\text{PC-native evidence admission + representation + authority + closure}
\end{array}
}
\]

The project doctrine is:

\[
\boxed{
\text{Training optimizes specialists; qualification earns registry eligibility; authority licenses their use.}
}
\]

and:

\[
\boxed{
\text{Evidence is admitted; representation is refined; authority is licensed; closure is earned.}
}
\]

That is the reconstruction target for `COUNCIL-PC-v1.0`.
