# Mathematical Workspace Recognition Architecture Spine

## Status

This document records the current settled direction of the Python mathematical workspace architecture after reconsidering the original `Facet` idea.

It is a design spine, not a final specification. The point is to capture the architecture we are converging on: what belongs in the core, what belongs in the logical layer, what belongs in search/evidence, and how facets/views fit after certification.

---

## 0. Origin: Reconsidering Facets

The starting idea was:

```text
facts -> regimes -> facets
```

A facet was an API unlocked after the workspace recognized some structure. For example, after certifying that a relation/order/structure is a poset, the workspace could expose:

```python
po = W.facet(S, "poset")

po.lower_set(x)
po.upper_set(x)
po.covers()
po.hasse_diagram()
```

That core idea remains correct, but its role changed.

### 0.1 What was wrong with facets as the center

Facets are too API-facing. They answer:

```text
What can I do with this object now that I know it has this structure?
```

They do not answer:

```text
What does this claim mean?
How was it certified?
What facts support it?
What follows from it?
What should be checked next?
What can be reused later?
```

So facets should not be the core recognition mechanism.

### 0.2 Corrected role of facets

The corrected design is:

```text
Facets / Views / Capabilities are outputs of certification.
```

The core recognition mechanism becomes:

```text
Formula AST
PredicateSpec
FactKey
Fact
Certificate
CheckerSpec
TheoremRule
StructuralNodeSpec
BridgeRule
CertificationPlanner
SearchEvidence
```

A facet is now the last mile: an API attached after the workspace has certified a useful structural node.

---

## 1. High-Level Layer Stack

The architecture should be understood as layered.

```text
MathObject
  raw payload / instantiation template

ObjectDraft
  payload plus initial metadata emitted before workspace introduction

ObjectRecord
  workspace-local ledger entry for a mathematical object

Registry
  equality / canonical-key / record-linking machinery

ConstructionGraph
  provenance graph of how objects were produced

Formula AST
  machine-readable representation of mathematical meanings

PredicateSpec
  registered mathematical vocabulary

DefinitionProfile
  logical/foundational complexity of a predicate definition

ComputationProfile / CheckerSpec
  feasible runtime ways to verify or refute predicate instances

FactKey / Fact / Certificate
  instantiated claims and recorded evidence

TheoremRule
  trusted implication pattern over registered predicates/nodes

StructuralNodeSpec
  certified structural enrichment point in an object-class spine

BridgeRule
  connects certifications across object-class spines

CertificationPlanner / CertificationEngine
  chooses and executes a route to certify or block a target

SearchSpace / SearchQuery / SearchResultBundle / FactDelta
  search/evidence layer for producing durable mathematical facts

Facet / View / Capability
  API unlocked by certified structural nodes
```

Compact slogan:

```text
Objects compute.
Formulas define.
Predicates name.
Checkers verify.
Rules propagate.
Certificates remember.
Structural nodes organize.
Search produces evidence.
Facets expose APIs.
Workspace orchestrates all of it.
```

---

## 2. Existing Core: Object Layer

The existing split remains foundational.

### 2.1 `MathObject`

`MathObject` is only the payload / instantiation template.

It owns:

```text
local mathematical data
local validation
canonical key
display payload
default initial metadata
```

It does not own the living ledger of facts, names, aliases, theorem consequences, regimes, or facets.

Example responsibilities:

```python
class MathObject:
    object_kind: str

    def validate(self) -> None:
        ...

    def canonical_key(self) -> tuple:
        ...

    def display_payload(self) -> object:
        ...

    def default_metadata(self) -> InitialMetadata:
        ...
```

### 2.2 `ObjectDraft`

`ObjectDraft` packages an object with initial metadata before it enters the workspace.

```python
@dataclass
class ObjectDraft:
    obj: MathObject
    metadata: InitialMetadata
```

A construction may return an `ObjectDraft` instead of a bare object so it can carry construction guarantees, presentations, definitions, and initial facts.

### 2.3 `ObjectRecord`

`ObjectRecord` is the workspace-local ledger entry.

It owns:

```text
record_id
payload object
kind
canonical key
names
aliases
presentations
definitions
construction/provenance
local fact summaries
certified structural nodes
facets/views
status
identity/equality information
```

Object-local facts may remain useful as summaries, but the canonical source of cross-object facts should become a workspace-level `FactIndex`.

### 2.4 `Registry`

The registry owns equality/canonical-key machinery.

It should handle:

```text
canonical_key lookup
multiple records with same key if policy permits
record equality classes
canonical representative
known_equal
union/link/merge
```

It should not become the fact system.

### 2.5 `Workspace`

The workspace is the public mathematical environment.

It owns:

```text
records
names
registry
construction graph
predicate registry
fact index
rule registry
structural-node registry
certification engine
search engine
facets/views
explanation API
```

The workspace is where object-level computation becomes durable mathematical knowledge.

---

## 3. Logical Layer: Why It Exists

Without a logical layer, a claim like:

```text
Relation(R)
```

is either:

```text
a string
```

or:

```text
a Python checker
```

Both are insufficient.

A string is readable but dumb. A checker is executable but does not by itself encode meaning.

The logical layer introduces a third representation:

```text
a structured formula AST
```

Example:

```text
Relation(R) :<-> ∀w(w ∈ R -> OrdPair(w))
```

stored as:

```python
ForAll(
    Var("w"),
    Implies(
        In(Var("w"), Var("R")),
        PredCall("OrdPair", (Var("w"),))
    )
)
```

This allows the system to compute:

```text
free variables
bound variables
predicate dependencies
one-step expansion
full primitive expansion
definition depth
quantifier depth
quantifier alternation
membership chase depth
pretty printed explanation
rule-pattern matching
```

The logical layer is not a proof assistant yet. It is a machine-readable meaning layer.

---

## 4. Formula AST

The formula language should begin small.

### 4.1 Terms

```python
class Term:
    pass


@dataclass(frozen=True)
class Var(Term):
    name: str
    sort: str | None = None


@dataclass(frozen=True)
class ObjRef(Term):
    record_id: int
```

`Var("R")` is used in schemas and definitions.

`ObjRef(17)` refers to a concrete object record.

The optional `sort` field can stay unused at first, but it prepares for later typechecking of theorem-rule substitutions.

### 4.2 Formulas

```python
class Formula:
    pass


@dataclass(frozen=True)
class In(Formula):
    left: Term
    right: Term


@dataclass(frozen=True)
class Eq(Formula):
    left: Term
    right: Term


@dataclass(frozen=True)
class PredCall(Formula):
    name: str
    args: tuple[Term, ...]
```

Primitive atomic formulas:

```text
x ∈ y
x = y
```

`PredCall` is for registered predicates such as:

```text
OrdPair(w)
Relation(R)
Function(F)
TransitiveOn(R,A)
```

### 4.3 Connectives and Quantifiers

```python
@dataclass(frozen=True)
class Not(Formula):
    body: Formula


@dataclass(frozen=True)
class And(Formula):
    left: Formula
    right: Formula


@dataclass(frozen=True)
class Or(Formula):
    left: Formula
    right: Formula


@dataclass(frozen=True)
class Implies(Formula):
    left: Formula
    right: Formula


@dataclass(frozen=True)
class Iff(Formula):
    left: Formula
    right: Formula


@dataclass(frozen=True)
class ForAll(Formula):
    var: Var
    body: Formula


@dataclass(frozen=True)
class Exists(Formula):
    var: Var
    body: Formula
```

Bounded quantifiers may be added as sugar:

```text
∀x∈A φ := ∀x(x ∈ A -> φ)
∃x∈A φ := ∃x(x ∈ A ∧ φ)
```

Do not begin with a full first-order language implementation beyond this.

### 4.4 Formula Operations

Minimum operations:

```python
free_vars(formula) -> set[str]
bound_vars(formula) -> set[str]
predicate_dependencies(formula) -> set[str]
substitute(formula, mapping) -> Formula
alpha_rename(formula, taken_names) -> Formula
expand_once(formula, registry) -> Formula
expand_to_depth(formula, registry, depth) -> Formula
expand_to_primitives(formula, registry) -> Formula
quantifier_depth(formula) -> int
pretty(formula, style="unicode") -> str
```

Important rule:

```text
Formula operations analyze and transform meaning.
They do not become the default runtime evaluator of mathematical payloads.
```

---

## 5. Predicate Layer

A predicate is registered mathematical vocabulary.

Examples:

```text
Singleton(s,x)
UnorderedPair(p,x,y)
KuratowskiPair(w,x,y)
OrdPair(w)
Relation(R)
PairIn(R,x,y)
SingleValuedRelation(R)
Function(F)
CartesianProduct(P,A,B)
BinaryRelationOn(R,A)
ReflexiveOn(R,A)
SymmetricOn(R,A)
AntisymmetricOn(R,A)
TransitiveOn(R,A)
InjectiveFunction(f,A,B)
SurjectiveFunction(f,A,B)
BijectiveFunction(f,A,B)
```

### 5.1 `PredicateSpec`

```python
@dataclass
class PredicateSpec:
    key: str
    parameters: tuple[str, ...]
    formal_definition: Formula | None = None
    primitive: bool = False
    definition_profile: DefinitionProfile | None = None
    computation_profiles: list[ComputationProfile] = field(default_factory=list)
    checkers: list[CheckerSpec] = field(default_factory=list)
    equality_invariant: bool = True
    explanation_template: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
```

Rule:

```text
Every PredicateSpec must either have a formal definition or be explicitly declared primitive.
```

This prevents meaningless string predicates.

### 5.2 Formal Definition vs Runtime Checker

A predicate may have:

```text
one formal meaning
many computational routes
many theorem-rule consequences
many possible certificate sources
```

Example:

```text
Function(F) means Relation(F) ∧ SingleValuedRelation(F).
```

But the runtime may certify it by:

```text
construction guarantee
cached fact
theorem rule
finite extensional checker
search result
manual assumption under policy
```

So:

```text
PredicateSpec = meaning + profiles + possible certification routes
```

---

## 6. Foundational Definitions Example

These are useful initial predicate definitions.

### 6.1 Singleton

```text
Singleton(s,x) :<-> ∀u(u ∈ s <-> u = x)
```

### 6.2 Unordered Pair

```text
UnorderedPair(p,x,y) :<-> ∀u(u ∈ p <-> (u = x ∨ u = y))
```

### 6.3 Kuratowski Pair

```text
KuratowskiPair(w,x,y) :<->
  ∀z(z ∈ w <-> (Singleton(z,x) ∨ UnorderedPair(z,x,y)))
```

### 6.4 Ordered Pair

```text
OrdPair(w) :<-> ∃x∃y KuratowskiPair(w,x,y)
```

### 6.5 Relation

```text
Relation(R) :<-> ∀w(w ∈ R -> OrdPair(w))
```

### 6.6 Pair Membership

```text
PairIn(R,x,y) :<-> ∃w(w ∈ R ∧ KuratowskiPair(w,x,y))
```

### 6.7 Single-Valued Relation

```text
SingleValuedRelation(R) :<->
  ∀x∀y1∀y2((PairIn(R,x,y1) ∧ PairIn(R,x,y2)) -> y1 = y2)
```

Important correction:

```text
SingleValuedRelation(R) alone does not imply Relation(R).
```

If `R = {17}`, the single-valued formula may be vacuously true while `R` is not a relation. Therefore:

```text
Function(F) requires Relation(F) and SingleValuedRelation(F).
```

### 6.8 Function

```text
Function(F) :<-> Relation(F) ∧ SingleValuedRelation(F)
```

### 6.9 Cartesian Product

```text
CartesianProduct(P,A,B) :<->
  ∀w(w ∈ P <-> ∃x∃y(x ∈ A ∧ y ∈ B ∧ KuratowskiPair(w,x,y)))
```

---

## 7. Definition Profiles and Predicate Ranking

The predicate expansion work revealed a natural definitional hierarchy.

Example:

```text
membership/equality
  ↓
singleton / unordered pair
  ↓
Kuratowski pair
  ↓
ordered pair
  ↓
relation
  ↓
single-valued relation
  ↓
function
```

This motivates `DefinitionProfile`.

```python
@dataclass
class DefinitionProfile:
    predicate_key: str
    macro_depth: int
    quantifier_depth: int
    quantifier_alternation_depth: int
    membership_chase_depth: int
    primitive_expansion_size: int
    free_variable_count: int
    bound_variable_count: int
    predicate_dependencies: tuple[str, ...]
```

The profile is used for:

```text
explanation
ranking
debugging expansion blowup
understanding foundational dependency
choosing how much to expand in explain()
showing membership-chase depth
```

Important boundary:

```text
Definition rank is not runtime cost.
```

The fully expanded set-theoretic formula may be huge, but a Python checker may certify the predicate efficiently using a concrete payload representation.

---

## 8. Computation Profiles and Checkers

The checker layer records feasible runtime certification routes.

```python
@dataclass
class ComputationProfile:
    applies_when: tuple[str, ...]
    estimated_cost: str | None = None
    finite_only: bool = False
    requires_extensional_data: bool = False
    produces_witness_on_fail: bool = False
    deterministic: bool = True
    cacheable: bool = True


@dataclass
class CheckerSpec:
    key: str
    predicate_key: str
    profile: ComputationProfile
    checker: Callable
    trust_level: str = "COMPUTED"
```

Examples:

```text
check finite extensional relation
check finite extensional single-valuedness
check finite transitivity
check finite antisymmetry
check finite reflexivity
check finite function injectivity
```

Checkers return structured results, not booleans.

```python
@dataclass
class CheckResult:
    status: FactStatus
    certificate: Certificate
```

Failure should include a witness whenever possible.

Example:

```text
TransitiveOn(R,A) = FALSE
witness = (a,b,c)
reason = aRb and bRc but not aRc
```

---

## 9. Facts and Certificates

### 9.1 `FactKey`

A fact key is an instantiated predicate call.

```python
@dataclass(frozen=True)
class FactKey:
    predicate: str
    args: tuple[int, ...]
```

Examples:

```python
FactKey("Function", (F_id,))
FactKey("TransitiveOn", (R_id, A_id))
FactKey("CartesianProduct", (P_id, A_id, B_id))
```

Prefer explicit predicate arguments over vague subject/context:

```text
Preferred:
  ReflexiveOn(R,A)

Less ideal:
  subject=R, claim="reflexive", context={"carrier": A}
```

The explicit form is better for rule matching.

### 9.2 `FactStatus`

```python
class FactStatus(Enum):
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
    INAPPLICABLE = "inapplicable"
    BLOCKED = "blocked"
    ASSUMED = "assumed"
    CONJECTURAL = "conjectural"
    STALE = "stale"
```

### 9.3 `Certificate`

```python
@dataclass
class Certificate:
    source_type: str
    claim: FactKey
    source_key: str | None = None
    premises: tuple[FactKey, ...] = ()
    premise_certificates: tuple["Certificate", ...] = ()
    witness: object | None = None
    coverage: object | None = None
    explanation: str | None = None
    data: dict[str, Any] = field(default_factory=dict)
```

Source types:

```text
DEFINITIONAL
CONSTRUCTION_GUARANTEE
COMPUTED
THEOREM
SEARCH_EXHAUSTIVE
SEARCH_BOUNDED
FAILED_WITH_WITNESS
USER_ASSERTED
CONJECTURAL
UNKNOWN
```

### 9.4 `Fact`

```python
@dataclass
class Fact:
    key: FactKey
    status: FactStatus
    certificate: Certificate | None = None
```

### 9.5 `FactIndex`

Cross-object facts belong in a workspace-level fact index.

```python
class FactIndex:
    def __init__(self):
        self._facts: dict[FactKey, Fact] = {}

    def add(self, fact: Fact) -> None:
        self._facts[fact.key] = fact

    def get(self, key: FactKey) -> Fact | None:
        return self._facts.get(key)

    def status(self, key: FactKey) -> FactStatus:
        ...

    def knows_true(self, key: FactKey) -> bool:
        ...

    def knows_false(self, key: FactKey) -> bool:
        ...
```

`ObjectRecord.facts` may remain as local summaries, but `FactIndex` should become canonical for multi-object facts.

---

## 10. Theorem Rule Layer

The theorem/rule layer is a trusted implication registry.

It is not a proof checker.

```python
@dataclass
class TheoremRule:
    key: str
    premises: tuple[PredCall, ...]
    conclusions: tuple[PredCall, ...]
    trust_level: str = "THEOREM"
    explanation_template: str | None = None
```

Examples:

```text
Function(F) -> Relation(F)

BijectiveFunction(f,A,B) -> InjectiveFunction(f,A,B)
BijectiveFunction(f,A,B) -> SurjectiveFunction(f,A,B)

Function(f,A,B) + InjectiveFunction(f,A,B) + SurjectiveFunction(f,A,B)
  -> BijectiveFunction(f,A,B)

PartialOrderRelation(R,A) -> ReflexiveOn(R,A)
PartialOrderRelation(R,A) -> AntisymmetricOn(R,A)
PartialOrderRelation(R,A) -> TransitiveOn(R,A)
```

This layer is a directed hypergraph:

```text
A + B + C -> D
```

not a tree.

The rule engine must:

```text
match premise patterns against known FactKeys
typecheck substitutions
derive conclusion FactKeys
store theorem certificates
avoid infinite propagation loops
```

---

## 11. Structural Spines

The structural spine layer is the corrected replacement for making facets central.

A structural node is a certified enrichment point that unlocks capabilities.

Examples:

```text
Relation
BinaryRelation
EquivalenceRelation
PreorderRelation
PartialOrderRelation
FunctionObject
OrderedStructure
PosetStructure
LatticeStructure
GroupStructure
```

### 11.1 Design Rule

```text
Predicates provide evidence.
Structural nodes represent useful certified regimes.
Facets expose APIs for certified regimes.
```

### 11.2 `StructuralNodeSpec`

```python
@dataclass
class StructuralNodeSpec:
    key: str
    parameters: tuple[str, ...]
    parent: str | None = None
    hard_gates: tuple[PredCall, ...] = ()
    requirements: tuple[PredCall, ...] = ()
    cheap_obstructions: tuple[PredCall, ...] = ()
    guarantees: tuple[PredCall, ...] = ()
    unlocks: tuple[str, ...] = ()
    explanation_template: str | None = None
```

The parent field gives the tree-shaped structural spine.

The requirements field gives the logical dependency graph.

These must be kept separate.

```text
parent edge = structural tree
requirement edge = logical dependency
```

This is the trick that lets the system remain tree-shaped without lying about mathematical dependencies.

### 11.3 Relation Spine Example

```text
Relation
└── BinaryRelation
    ├── EquivalenceRelation
    └── PreorderRelation
        └── PartialOrderRelation
            ├── TotalOrderRelation
            ├── WellFoundedOrderRelation
            └── LatticeOrderRelation
```

### 11.4 Function Spine Example

```text
FunctionObject
├── InjectiveFunction
├── SurjectiveFunction
├── BijectiveFunction
├── Endofunction
│   ├── IdempotentEndofunction
│   └── FixedPointSystem
└── OrderPreservingFunction
```

### 11.5 Structure Spine Example

```text
Structure
├── RelationalStructure
│   ├── OrderedStructure
│   │   └── PosetStructure
│   │       └── LatticeStructure
│   └── EquivalenceStructure
├── AlgebraicStructure
│   ├── Magma
│   │   └── Semigroup
│   │       └── Monoid
│   │           └── Group
└── MixedStructure
```

---

## 12. Bridge Rules Between Spines

Object-class spines should stay separate, but structures often combine components from different spines.

Example:

```text
PartialOrderRelation(R,A)
Structure S has carrier A and order slot R
------------------------------------------------
PosetStructure(S)
```

```python
@dataclass
class BridgeRule:
    key: str
    inputs: tuple[str, ...]
    required_nodes: tuple[PredCall, ...]
    required_predicates: tuple[PredCall, ...]
    produced_node: PredCall
```

Bridge rules are necessary for:

```text
set + relation -> relational structure
set + partial order relation -> poset structure
set + operation -> algebraic structure
function graph -> relation view
structure slots -> higher structural node
```

This handles the fact that a function is set-theoretically a relation while still letting `Function` have its own computational spine.

---

## 13. Certification Planner / Engine

The planner chooses the cheapest safe route to a target.

Possible sources:

```text
cached fact
construction guarantee
theorem rule
direct checker
search result
definitional decomposition
user assumption
```

### 13.1 Route Order for Minimum Viable Version

Start with:

```text
1. cached fact
2. construction guarantee
3. theorem rule
4. direct checker
5. definitional decomposition
6. unknown / blocked
```

Do not begin with a complicated optimizer.

### 13.2 Later Priority Model

Later, rank candidate routes by:

```text
dependency readiness
estimated check cost
definition complexity
structural payoff
obstruction likelihood
user target relevance
coverage strength
```

Possible score:

```text
priority =
  relevance
+ dependency_readiness
+ payoff
- estimated_cost
- obstruction_penalty
```

But ranking only chooses what to try first.

```text
Ranking does not decide truth.
Certificates decide truth.
```

### 13.3 Candidate States

For a target fact/node:

```text
CERTIFIED
CANDIDATE
BLOCKED
FAILED
UNKNOWN
CONJECTURAL
STALE
```

### 13.4 Obstruction-First Checking

Before full certification, try cheap ways to kill a branch.

For partial order:

```text
hard gates:
  R is relation-like
  A is set-like
  R is binary on A

cheap obstructions:
  missing diagonal pair
  antisymmetry counterexample
  transitivity counterexample

full certification:
  full reflexivity
  full antisymmetry
  full transitivity
```

A negative fact with a witness blocks all nodes requiring it.

---

## 14. Downward Inheritance and Caching

When a high structural node is certified, cache its consequences.

Example:

```text
LatticeStructure(S)
```

should cache:

```text
PosetStructure(S)
OrderedStructure(S)
Structure(S)
```

and through its order relation:

```text
PartialOrderRelation(R,A)
PreorderRelation(R,A)
BinaryRelationOn(R,A)
ReflexiveOn(R,A)
AntisymmetricOn(R,A)
TransitiveOn(R,A)
```

Each cached result should receive a certificate:

```text
source_type = THEOREM or STRUCTURAL_INHERITANCE
premise = LatticeStructure(S)
```

Do not silently add facts.

---

## 15. Search-to-Logic Layer

The search layer produces evidence bundles.

It is a generalized checker.

A normal checker asks:

```text
Is TransitiveOn(R,A) true?
```

A search engine asks:

```text
Among all R in Rel(A,A), which satisfy these assumptions?
How many candidates survive?
Does every survivor satisfy this property?
Can we find a witness?
Can we find a counterexample?
```

### 15.1 Core Search Objects

```python
@dataclass
class SearchSpace:
    key: str
    variables: tuple[SearchVariable, ...]
    ambient_formula: Formula
    estimated_size: object | None = None
    presentations: list[Any] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class SearchQuery:
    space: SearchSpace
    assumptions: tuple[Formula, ...] = ()
    asks: tuple[Formula, ...] = ()
    mode: str = "exhaustive"
    limits: dict[str, Any] = field(default_factory=dict)


@dataclass
class SearchCoverage:
    exhaustive: bool
    searched_count: int | None = None
    total_count: int | None = None
    bounds: dict[str, Any] = field(default_factory=dict)
    method: str | None = None
    engine: str | None = None


@dataclass
class SearchResultBundle:
    query: SearchQuery
    coverage: SearchCoverage
    candidate_count: object | None = None
    surviving_candidates: object | None = None
    true_facts: list[Fact] = field(default_factory=list)
    false_facts: list[Fact] = field(default_factory=list)
    unknown_facts: list[Fact] = field(default_factory=list)
    conjectural_facts: list[Fact] = field(default_factory=list)
    witnesses: list[object] = field(default_factory=list)
    counterexamples: list[object] = field(default_factory=list)
    generated_objects: list[ObjectDraft] = field(default_factory=list)
    residual_constraints: list[Formula] = field(default_factory=list)
    exports: dict[str, object] = field(default_factory=dict)


@dataclass
class FactDelta:
    source: str
    facts: list[Fact] = field(default_factory=list)
    generated_objects: list[ObjectDraft] = field(default_factory=list)
    construction_events: list[ConstructionEvent] = field(default_factory=list)
    residual_constraints: list[Formula] = field(default_factory=list)
    explanation: str | None = None
```

### 15.2 Coverage Rule

```text
No coverage, no strong certificate.
```

If search is exhaustive, it may certify universal claims over the searched space.

If search is bounded/non-exhaustive, it produces conjectural or bounded evidence, not unrestricted truth.

### 15.3 Absorption

Search results enter the workspace through:

```python
Workspace.absorb_fact_delta(delta)
Workspace.absorb_search_result(result)
```

Absorption should:

```text
insert facts into FactIndex
introduce generated witness objects if requested
store construction events
attach witnesses/counterexamples to certificates
run theorem propagation
attempt structural-node certification
refresh facets/views
```

### 15.4 Design Rule

Search results must not enter the workspace as strings or raw lists.

They enter as:

```text
FactKey + FactStatus + Certificate + Coverage
```

---

## 16. Candidate Generation

Do not run every checker on object introduction.

Candidate generation uses cheap shape data:

```text
object kind
arity
slots
carrier
operation count
relation count
declared names
construction provenance
presentations
```

Examples:

```text
Structure(carrier=A, relations={"leq": R})
```

suggests:

```text
RelationalStructure
OrderedStructure
PosetStructure
```

but not:

```text
GroupStructure
MetricSpaceStructure
RingStructure
```

unless the relevant slots exist.

Candidate generation is not proof. It only chooses plausible targets.

---

## 17. Equality, Invariance, and Transfer

The registry knows when two records are equal/equivalent.

The logical layer should not blindly transfer all facts.

Predicates should eventually carry invariance metadata:

```python
PredicateSpec(..., equality_invariant=True)
```

Most mathematical facts transfer across equality. Workspace-history facts do not.

Example transferable:

```text
Cardinality(A,3)
Finite(A)
```

Example not automatically transferable:

```text
introduced_by_roster(A)
```

This preserves the distinction:

```text
mathematical facts
workspace provenance/history facts
```

---

## 18. Workspace API Sketch

```python
class Workspace:
    # Predicate layer
    def register_predicate(self, spec: PredicateSpec) -> None: ...
    def predicate(self, key: str) -> PredicateSpec: ...
    def expand_predicate(self, key: str, *args, depth=None) -> Formula: ...
    def definition_profile(self, key: str) -> DefinitionProfile: ...

    # Fact/certification layer
    def fact_key(self, predicate_key: str, *records) -> FactKey: ...
    def fact(self, predicate_key: str, *records) -> Fact | None: ...
    def knows(self, predicate_key: str, *records) -> bool: ...
    def certify(self, predicate_key: str, *records) -> Fact: ...
    def why(self, predicate_key: str, *records) -> str: ...

    # Rule layer
    def register_theorem_rule(self, rule: TheoremRule) -> None: ...

    # Structural node layer
    def register_structural_node(self, spec: StructuralNodeSpec) -> None: ...
    def certify_node(self, node_key: str, *records) -> Fact: ...

    # Facet/view layer
    def facet(self, record, facet_name: str): ...

    # Search layer
    def search(self, *, variables, assumptions=(), asks=(), mode="auto", limits=None) -> SearchResultBundle: ...
    def absorb_fact_delta(self, delta: FactDelta) -> None: ...
    def absorb_search_result(self, result: SearchResultBundle) -> None: ...
```

---

## 19. Module Layout

```text
structlab/
  core/
    math_object.py
    metadata.py
    records.py
    registry.py
    workspace.py
    construction.py

    formulas.py
    predicates.py
    facts.py
    rules.py
    certification.py
    structural.py

  objects/
    finite_set.py
    relation.py
    function.py
    structure.py

  checkers/
    finite_sets.py
    relations.py
    functions.py
    orders.py

  predicates/
    set_theory.py
    relation_theory.py
    function_theory.py
    order_theory.py
    algebra_theory.py

  facets/
    base.py
    function.py
    poset.py
    lattice.py
    group.py

  search/
    spaces.py
    queries.py
    coverage.py
    results.py
    engines.py
    translators.py
    planners.py

  tests/
    test_formulas.py
    test_predicates.py
    test_facts.py
    test_certification.py
    test_structural_nodes.py
    test_search_absorption.py
```

---

## 20. Minimum Viable Implementation Plan

### Phase A: Stabilize Existing Core

Tasks:

```text
clean metadata examples
fix typos
fix FactStore.has or replace with FactIndex
fix Registry multi-record behavior
fix Workspace name conflict handling
make MathObject clearly payload-only
```

### Phase B: Formula AST

Implement:

```text
Var
ObjRef
In
Eq
Not
And
Or
Implies
Iff
ForAll
Exists
PredCall
```

plus:

```text
pretty
free_vars
bound_vars
substitute
alpha_rename
predicate_dependencies
```

### Phase C: Predicate Registry

Implement:

```text
PredicateSpec
PredicateRegistry
```

Register:

```text
Singleton
UnorderedPair
KuratowskiPair
OrdPair
Relation
PairIn
SingleValuedRelation
Function
CartesianProduct
```

### Phase D: Expansion and Definition Profiles

Implement:

```text
expand_once
expand_to_depth
expand_to_primitives
definition_depth
quantifier_depth
DefinitionProfile
```

### Phase E: Facts and Certificates

Implement:

```text
FactKey
FactStatus
Fact
Certificate
FactIndex
```

### Phase F: Checkers

Implement finite/extensional checkers for:

```text
Relation
SingleValuedRelation
Function
BinaryRelationOn
ReflexiveOn
SymmetricOn
AntisymmetricOn
TransitiveOn
```

### Phase G: Certification Engine

Implement simple route order:

```text
cached
construction guarantee
theorem rule
direct checker
definitional decomposition
unknown/blocked
```

### Phase H: Theorem Rules

Implement pattern-based theorem rules over `PredCall`.

First rules:

```text
Function(F) -> Relation(F)
Function(F) -> SingleValuedRelation(F)

PartialOrderRelation(R,A) -> ReflexiveOn(R,A)
PartialOrderRelation(R,A) -> AntisymmetricOn(R,A)
PartialOrderRelation(R,A) -> TransitiveOn(R,A)
```

### Phase I: Structural Nodes

Implement:

```text
StructuralNodeSpec
StructuralNodeRegistry
```

First nodes:

```text
FunctionObject(F)
EquivalenceRelation(R,A)
PartialOrderRelation(R,A)
PosetStructure(S)
```

### Phase J: Facets

Attach facets after node certification:

```text
FunctionFacet
EquivalenceRelationFacet
PosetFacet
```

### Phase K: Search Evidence

Implement containers first:

```text
SearchCoverage
SearchResultBundle
FactDelta
```

Then add finite brute-force search.

Do not begin with SAT/SMT/external backends.

---

## 21. Non-Goals for First Implementation

Do not build:

```text
full proof checker
full first-order parser
automatic theorem prover
ZFC evaluator
general model checker
SAT/SMT backend
Lean/Coq export
complete structural hierarchy
```

These are later directions.

The near-term kernel is:

```text
formula AST
predicate registry
fact/certificate system
finite checkers
structural-node certification
facets as outputs
```

---

## 22. Future Direction: Proof Kernel

The architecture naturally points toward a proof kernel later.

Possible future layer:

```text
primitive inference rules
definitional unfolding
substitution
modus ponens
universal instantiation
context/type checking
proof objects
proof search over first-order derivations
kernel-checked theorem rules
```

This is not part of the first implementation.

Current policy:

```text
Use trusted theorem rules now.
Maybe kernel-check theorem rules later.
```

---

## 23. Final Mental Model

The workspace becomes a mathematical memory and certification system.

```text
construct -> introduce -> define -> check/search -> certify -> cache -> propagate -> unlock -> explain
```

Expanded:

```text
MathObject payloads compute concrete data.
Formula ASTs describe mathematical meaning.
PredicateSpecs register vocabulary.
Checkers and search engines produce evidence.
Facts store instantiated claims.
Certificates explain why claims are known.
TheoremRules propagate known consequences.
StructuralNodeSpecs organize useful regimes.
BridgeRules combine spines.
Facets expose certified APIs.
Workspace ties everything together.
```

The final correction to the original facet idea is:

```text
Facets are not where recognition happens.
Facets are what recognition earns.
```
