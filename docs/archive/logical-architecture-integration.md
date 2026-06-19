# Logical Architecture Layer for the Mathematical Workspace

## 0. Purpose

This document specifies an added logical architecture layer for the Python mathematical workspace. It integrates with the existing architecture in which:

```text
MathObject     = mathematical payload / instantiation template
ObjectRecord   = workspace-local ledger entry
Registry       = internal canonical/equality/indexing machinery
Workspace      = public mathematical environment / object ledger
```

The logical layer is not intended to turn the project into a full proof assistant. Its role is to provide a machine-readable semantic layer between concrete Python payloads and workspace-level facts, regimes, certificates, recognizers, and facets.

The core idea is:

```text
MathObject payloads compute.
Formula ASTs describe meaning.
PredicateSpecs register mathematical vocabulary.
Facts record instantiated claims.
Certificates record why claims are known.
Checkers provide feasible computational routes.
TheoremRules propagate known claims.
StructuralNodeSpecs certify useful mathematical regimes.
Facets expose APIs unlocked by certified regimes.
```

This layer makes the system more than a class library. It lets the workspace explain not just that something is a function, relation, partial order, or cartesian product, but what that predicate means, how it was checked or inferred, and what consequences follow.

---

## 1. Design Position in the Existing Architecture

The existing architecture has a strong separation:

```text
MathObject
  owns payload-level mathematical data and local validation

ObjectRecord
  owns workspace-local identity, names, definitions, facts, regimes, facets, and construction history

Registry
  owns internal canonical-key lookup and equality-class tracking

Workspace
  owns the public environment, object ledger, fact ledger, recognition pipeline, and explanation API
```

The logical layer should not replace any of these. It inserts a semantic stratum used by the workspace.

```text
User / code
   ↓
MathObject subclass
   ↓
ObjectDraft / InitialMetadata
   ↓
Workspace.introduce(...)
   ↓
ObjectRecord
   ↓
Logical layer
   - PredicateSpec
   - Formula AST
   - FactKey
   - Certificate
   - CheckerSpec
   - TheoremRule
   - StructuralNodeSpec
   ↓
Recognition / certification
   ↓
Regime / Facet / Explanation
```

The main integration principle:

```text
The logical layer gives meaning and certification structure to facts.
It does not become the payload layer.
```

For example, `FiniteSet` should still compute membership with its internal finite representation. The formula `x ∈ A` is a semantic representation, not necessarily the runtime mechanism for finite membership checks.

---

## 2. Why Formulas Are Needed

Without a formula layer, a predicate such as:

```text
Relation(R)
```

is either a string or a Python checker. Both are insufficient.

A string is readable but not structurally usable:

```text
"Relation(R) means every element of R is an ordered pair"
```

A checker is executable but does not by itself encode mathematical meaning:

```python
def check_relation(R):
    ...
```

The formula layer gives a third thing: a structured formal definition.

```text
Relation(R) :<-> ∀w(w ∈ R -> OrdPair(w))
```

encoded as an abstract syntax tree:

```python
ForAll(
    Var("w"),
    Implies(
        In(Var("w"), Var("R")),
        PredCall("OrdPair", (Var("w"),))
    )
)
```

This makes definitions traversable, expandable, analyzable, printable, and usable by rules.

The formula layer supports:

```text
definition registration
macro expansion
membership-chase generation
free-variable analysis
bound-variable analysis
alpha-renaming
substitution
definition-depth computation
quantifier-depth computation
quantifier-alternation computation
dependency graphs
pretty-printing
explanations
theorem-rule pattern matching
structural-node requirements
checker documentation
certificate explanations
```

---

## 3. Formula AST

The formula language should be deliberately small.

### 3.1 Terms

```python
from dataclasses import dataclass
from typing import tuple


class Term:
    pass


@dataclass(frozen=True)
class Var(Term):
    name: str


@dataclass(frozen=True)
class ObjRef(Term):
    record_id: int
```

`Var("R")` is used inside general predicate definitions.

`ObjRef(record_id=17)` is used when a definition, fact, or theorem pattern is instantiated against a concrete workspace object.

Example distinction:

```text
General definition:
  Relation(R)

Concrete fact:
  Relation(record #17)
```

### 3.2 Atomic Formulas

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

The primitive atoms are:

```text
x ∈ y
x = y
```

`PredCall` represents a registered predicate call, such as:

```text
OrdPair(w)
Relation(R)
Function(F)
TransitiveOn(R,A)
```

### 3.3 Logical Connectives

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
```

### 3.4 Quantifiers

```python
@dataclass(frozen=True)
class ForAll(Formula):
    var: Var
    body: Formula


@dataclass(frozen=True)
class Exists(Formula):
    var: Var
    body: Formula
```

Later, bounded quantifiers can be added as sugar:

```python
ForAllIn(x, A, body)
ExistsIn(x, A, body)
```

but they should desugar into ordinary first-order formulas:

```text
∀x∈A φ   :=   ∀x(x ∈ A -> φ)
∃x∈A φ   :=   ∃x(x ∈ A ∧ φ)
```

---

## 4. PredicateSpec

A `PredicateSpec` is the registered meaning and operational metadata for a predicate.

```python
from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class PredicateSpec:
    key: str
    parameters: tuple[str, ...]
    formal_definition: Optional[Formula] = None
    primitive: bool = False
    definition_profile: Optional["DefinitionProfile"] = None
    computation_profiles: list["ComputationProfile"] = field(default_factory=list)
    checkers: list["CheckerSpec"] = field(default_factory=list)
    explanation_template: Optional[str] = None
    metadata: dict[str, Any] = field(default_factory=dict)
```

Important rule:

```text
Every PredicateSpec must either have a formal definition or be explicitly declared primitive.
```

Examples of primitive predicates or atoms:

```text
∈
=
```

Examples of defined predicates:

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
ReflexiveOn(R,A)
TransitiveOn(R,A)
AntisymmetricOn(R,A)
```

A predicate is not just a checker. A predicate has one meaning but may have many certification routes.

```text
PredicateSpec = meaning + profiles + possible checkers
```

---

## 5. Example Predicate Definitions

### 5.1 Singleton

Mathematical form:

```text
Singleton(s,x) :<-> ∀u(u ∈ s <-> u = x)
```

AST form:

```python
PredicateSpec(
    key="Singleton",
    parameters=("s", "x"),
    formal_definition=ForAll(
        Var("u"),
        Iff(
            In(Var("u"), Var("s")),
            Eq(Var("u"), Var("x"))
        )
    )
)
```

### 5.2 Unordered Pair

```text
UnorderedPair(p,x,y) :<-> ∀u(u ∈ p <-> (u = x ∨ u = y))
```

```python
PredicateSpec(
    key="UnorderedPair",
    parameters=("p", "x", "y"),
    formal_definition=ForAll(
        Var("u"),
        Iff(
            In(Var("u"), Var("p")),
            Or(
                Eq(Var("u"), Var("x")),
                Eq(Var("u"), Var("y"))
            )
        )
    )
)
```

### 5.3 Kuratowski Pair

```text
KuratowskiPair(w,x,y) :<->
  ∀z(z ∈ w <-> (Singleton(z,x) ∨ UnorderedPair(z,x,y)))
```

```python
PredicateSpec(
    key="KuratowskiPair",
    parameters=("w", "x", "y"),
    formal_definition=ForAll(
        Var("z"),
        Iff(
            In(Var("z"), Var("w")),
            Or(
                PredCall("Singleton", (Var("z"), Var("x"))),
                PredCall("UnorderedPair", (Var("z"), Var("x"), Var("y")))
            )
        )
    )
)
```

### 5.4 Ordered Pair Predicate

```text
OrdPair(w) :<-> ∃x ∃y KuratowskiPair(w,x,y)
```

```python
PredicateSpec(
    key="OrdPair",
    parameters=("w",),
    formal_definition=Exists(
        Var("x"),
        Exists(
            Var("y"),
            PredCall("KuratowskiPair", (Var("w"), Var("x"), Var("y")))
        )
    )
)
```

### 5.5 Relation

```text
Relation(R) :<-> ∀w(w ∈ R -> OrdPair(w))
```

```python
PredicateSpec(
    key="Relation",
    parameters=("R",),
    formal_definition=ForAll(
        Var("w"),
        Implies(
            In(Var("w"), Var("R")),
            PredCall("OrdPair", (Var("w"),))
        )
    )
)
```

### 5.6 PairIn

`PairIn` is a useful bridge predicate.

```text
PairIn(R,x,y) :<-> ∃w(w ∈ R ∧ KuratowskiPair(w,x,y))
```

```python
PredicateSpec(
    key="PairIn",
    parameters=("R", "x", "y"),
    formal_definition=Exists(
        Var("w"),
        And(
            In(Var("w"), Var("R")),
            PredCall("KuratowskiPair", (Var("w"), Var("x"), Var("y")))
        )
    )
)
```

### 5.7 Single-Valued Relation

```text
SingleValuedRelation(R) :<->
  ∀x ∀y1 ∀y2((PairIn(R,x,y1) ∧ PairIn(R,x,y2)) -> y1 = y2)
```

```python
PredicateSpec(
    key="SingleValuedRelation",
    parameters=("R",),
    formal_definition=ForAll(
        Var("x"),
        ForAll(
            Var("y1"),
            ForAll(
                Var("y2"),
                Implies(
                    And(
                        PredCall("PairIn", (Var("R"), Var("x"), Var("y1"))),
                        PredCall("PairIn", (Var("R"), Var("x"), Var("y2")))
                    ),
                    Eq(Var("y1"), Var("y2"))
                )
            )
        )
    )
)
```

### 5.8 Function

```text
Function(F) :<-> Relation(F) ∧ SingleValuedRelation(F)
```

```python
PredicateSpec(
    key="Function",
    parameters=("F",),
    formal_definition=And(
        PredCall("Relation", (Var("F"),)),
        PredCall("SingleValuedRelation", (Var("F"),))
    )
)
```

### 5.9 Cartesian Product

```text
CartesianProduct(P,A,B) :<->
  ∀w(w ∈ P <-> ∃x ∃y(x ∈ A ∧ y ∈ B ∧ KuratowskiPair(w,x,y)))
```

```python
PredicateSpec(
    key="CartesianProduct",
    parameters=("P", "A", "B"),
    formal_definition=ForAll(
        Var("w"),
        Iff(
            In(Var("w"), Var("P")),
            Exists(
                Var("x"),
                Exists(
                    Var("y"),
                    And(
                        In(Var("x"), Var("A")),
                        And(
                            In(Var("y"), Var("B")),
                            PredCall("KuratowskiPair", (Var("w"), Var("x"), Var("y")))
                        )
                    )
                )
            )
        )
    )
)
```

---

## 6. Formula Operations

The formula layer should provide structural operations.

### 6.1 Free Variables

```python
def free_vars(formula: Formula) -> set[str]:
    ...
```

Examples:

```text
free_vars(Relation(R)) = {R}
free_vars(∀w(w ∈ R -> OrdPair(w))) = {R}
free_vars(∀u(u ∈ s <-> u = x)) = {s, x}
```

### 6.2 Bound Variables

```python
def bound_vars(formula: Formula) -> set[str]:
    ...
```

Example:

```text
bound_vars(∀w(w ∈ R -> OrdPair(w))) = {w}
```

### 6.3 Alpha-Renaming

When expanding definitions inside other definitions, bound variables must be renamed to avoid capture.

Problem:

```text
Outer formula uses x.
Expanded predicate also binds x.
```

Solution:

```text
rename internal x to x_1 or another fresh variable.
```

Required operation:

```python
def alpha_rename(formula: Formula, taken_names: set[str]) -> Formula:
    ...
```

### 6.4 Substitution

Used to instantiate predicate definitions and theorem rules.

```python
def substitute(formula: Formula, subst: dict[str, Term]) -> Formula:
    ...
```

Example:

```text
Relation(R)
substitute R := ObjRef(17)

Result:
Relation(record #17)
```

For formal definitions:

```text
Relation(R) :<-> ∀w(w ∈ R -> OrdPair(w))

Substitute R := ObjRef(17):
∀w(w ∈ ObjRef(17) -> OrdPair(w))
```

### 6.5 Expansion

```python
def expand_once(formula: Formula, registry: PredicateRegistry) -> Formula:
    ...


def expand_to_depth(formula: Formula, registry: PredicateRegistry, depth: int) -> Formula:
    ...


def expand_to_primitives(formula: Formula, registry: PredicateRegistry) -> Formula:
    ...
```

Example:

```text
Function(F)

expand_once:
Relation(F) ∧ SingleValuedRelation(F)

expand_to_depth 2:
∀w(w ∈ F -> OrdPair(w))
∧
∀x∀y1∀y2((PairIn(F,x,y1) ∧ PairIn(F,x,y2)) -> y1 = y2)

expand_to_primitives:
formula using only ∈, =, quantifiers, and logical connectives
```

Expansion is a view. It should not be the default runtime representation.

### 6.6 Definition Dependencies

```python
def predicate_dependencies(formula: Formula) -> set[str]:
    ...
```

Example:

```text
dependencies(Function) = {Relation, SingleValuedRelation}
dependencies(Relation) = {OrdPair}
dependencies(OrdPair) = {KuratowskiPair}
dependencies(KuratowskiPair) = {Singleton, UnorderedPair}
```

### 6.7 Definition Depth

```python
def definition_depth(predicate_key: str, registry: PredicateRegistry) -> int:
    ...
```

Recursive rule:

```text
depth(primitive) = 0
depth(P) = 1 + max(depth(Q) for Q used in P's definition)
```

Example:

```text
∈, =                         depth 0
Singleton                    depth 1
UnorderedPair                depth 1
KuratowskiPair               depth 2
OrdPair                      depth 3
Relation                     depth 4
SingleValuedRelation         depends on PairIn / KuratowskiPair
Function                     1 + max(Relation, SingleValuedRelation)
CartesianProduct             1 + depth(KuratowskiPair)
```

This depth is not an absolute mathematical property. It depends on the chosen definitional vocabulary.

### 6.8 Quantifier Depth

```python
def quantifier_depth(formula: Formula) -> int:
    ...
```

Example:

```text
∀w ∃x ∃y ∀z ∀u
```

has quantifier depth:

```text
5
```

### 6.9 Pretty Printing

```python
def pretty(formula: Formula, *, style="unicode") -> str:
    ...
```

Examples:

```text
unicode:
  ∀w(w ∈ R -> OrdPair(w))

ascii:
  forall w (w in R -> OrdPair(w))

sexpr:
  (forall w (implies (in w R) (OrdPair w)))
```

---

## 7. DefinitionProfile

A `DefinitionProfile` stores logical/foundational complexity data.

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

This is for meaning, explanation, ranking, and introspection. It is not the same as runtime cost.

Example:

```text
Function(F)

DefinitionProfile:
  macro_depth: high, because it depends on Relation and SingleValuedRelation
  quantifier_depth: based on the fully expanded formula
  dependencies: Relation, SingleValuedRelation, PairIn, OrdPair, KuratowskiPair, Singleton, UnorderedPair
```

Use cases:

```text
show user the definitional dependency tree
rank predicates by foundational complexity
debug expansion blowup
choose how much expansion to show in Workspace.explain(...)
compare surface definitions with primitive expansions
```

---

## 8. ComputationProfile and CheckerSpec

The formal definition is the meaning. A checker is a feasible computational route.

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
```

```python
@dataclass
class CheckerSpec:
    key: str
    predicate_key: str
    profile: ComputationProfile
    checker: callable
    trust_level: str = "COMPUTED"
```

Example checker profile:

```python
ComputationProfile(
    applies_when=("finite_carrier", "extensional_relation"),
    estimated_cost="O(|A|^3)",
    finite_only=True,
    requires_extensional_data=True,
    produces_witness_on_fail=True,
)
```

This separates:

```text
what the predicate means
```

from:

```text
how the program can check it in a particular representation
```

A predicate may be:

```text
formally meaningful but not directly checkable
checkable only for finite objects
checkable only with extensional presentations
checkable symbolically in special cases
derivable by theorem rule
known by construction guarantee
unknown under current workspace capabilities
```

---

## 9. FactKey, Fact, Status, Certificate

### 9.1 FactKey

A `FactKey` is an instantiated predicate claim.

```python
@dataclass(frozen=True)
class FactKey:
    predicate: str
    args: tuple[int, ...]
```

Example:

```python
FactKey("Function", args=(F.record_id,))
FactKey("TransitiveOn", args=(R.record_id, A.record_id))
FactKey("CartesianProduct", args=(P.record_id, A.record_id, B.record_id))
```

Prefer making mathematical context explicit in the predicate signature:

```text
ReflexiveOn(R,A)
```

rather than:

```text
Fact("reflexive", subject=R, context={"carrier": A})
```

The second style is convenient early, but the first is better for theorem matching and recognition.

### 9.2 FactStatus

```python
from enum import Enum


class FactStatus(Enum):
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"
    INAPPLICABLE = "inapplicable"
    BLOCKED = "blocked"
    ASSUMED = "assumed"
    STALE = "stale"
```

Meanings:

```text
TRUE
  certified true

FALSE
  certified false, ideally with witness

UNKNOWN
  meaningful but not currently certified either way

INAPPLICABLE
  predicate does not apply to this object shape

BLOCKED
  target cannot be certified because a required fact is false or missing

ASSUMED
  user asserted or accepted under policy

STALE
  result invalidated by mutation or changed dependencies
```

If mathematical payloads are immutable, `STALE` can mostly be avoided.

### 9.3 Certificate

A `Certificate` records why a fact has its status.

```python
@dataclass
class Certificate:
    source_type: str
    claim: FactKey
    source_key: str | None = None
    premises: tuple[FactKey, ...] = ()
    premise_certificates: tuple["Certificate", ...] = ()
    witness: object | None = None
    explanation: str | None = None
    data: dict = field(default_factory=dict)
```

Source types:

```text
DEFINITIONAL
CONSTRUCTION_GUARANTEE
COMPUTED
THEOREM
USER_ASSERTED
CONJECTURAL
FAILED_WITH_WITNESS
UNKNOWN
```

### 9.4 Fact

```python
@dataclass
class Fact:
    key: FactKey
    status: FactStatus
    certificate: Certificate | None = None
```

Examples:

```python
Fact(
    key=FactKey("Function", args=(F_id,)),
    status=FactStatus.TRUE,
    certificate=Certificate(
        source_type="COMPUTED",
        claim=FactKey("Function", args=(F_id,)),
        source_key="finite_extensional_function_checker",
        explanation="Every input has at most one output."
    )
)
```

Failure with witness:

```python
Fact(
    key=FactKey("SingleValuedRelation", args=(R_id,)),
    status=FactStatus.FALSE,
    certificate=Certificate(
        source_type="FAILED_WITH_WITNESS",
        claim=FactKey("SingleValuedRelation", args=(R_id,)),
        source_key="finite_extensional_single_valued_checker",
        witness={
            "x": "a",
            "y1": 1,
            "y2": 2,
            "pair1": ("a", 1),
            "pair2": ("a", 2),
        },
        explanation="The same input has two distinct outputs."
    )
)
```

---

## 10. FactIndex / CertificateStore

The workspace should eventually maintain a workspace-level fact index rather than only object-local fact stores.

Reason:

```text
Many facts involve multiple records.
```

Examples:

```text
TransitiveOn(R,A)
CartesianProduct(P,A,B)
HomomorphismBetween(f,A,B)
OrderPreservingBetween(f,P,Q)
```

Suggested store:

```python
class FactIndex:
    def __init__(self):
        self._facts: dict[FactKey, Fact] = {}

    def add(self, fact: Fact) -> None:
        self._facts[fact.key] = fact

    def get(self, key: FactKey) -> Fact | None:
        return self._facts.get(key)

    def status(self, key: FactKey) -> FactStatus:
        fact = self.get(key)
        if fact is None:
            return FactStatus.UNKNOWN
        return fact.status

    def knows_true(self, key: FactKey) -> bool:
        return self.status(key) is FactStatus.TRUE

    def knows_false(self, key: FactKey) -> bool:
        return self.status(key) is FactStatus.FALSE
```

The existing `ObjectRecord.facts` can remain useful for local summaries, but cross-object predicate facts should live in a workspace-level `FactIndex`.

---

## 11. TheoremRule

A `TheoremRule` is a trusted inference pattern. It is not a proof search engine.

```python
@dataclass
class TheoremRule:
    key: str
    premises: tuple[PredCall, ...]
    conclusions: tuple[PredCall, ...]
    trust_level: str = "THEOREM"
    explanation_template: str | None = None
```

Example:

```python
TheoremRule(
    key="function_implies_relation",
    premises=(
        PredCall("Function", (Var("F"),)),
    ),
    conclusions=(
        PredCall("Relation", (Var("F"),)),
    ),
)
```

If the workspace knows:

```text
Function(record #17)
```

then the rule engine can derive:

```text
Relation(record #17)
```

with a theorem certificate.

More examples:

```text
BijectiveFunction(f) -> InjectiveFunction(f)
BijectiveFunction(f) -> SurjectiveFunction(f)

Function(f) ∧ InjectiveFunction(f) ∧ SurjectiveFunction(f)
  -> BijectiveFunction(f)

PartialOrderRelation(R,A)
  -> ReflexiveOn(R,A)
PartialOrderRelation(R,A)
  -> AntisymmetricOn(R,A)
PartialOrderRelation(R,A)
  -> TransitiveOn(R,A)
```

Mathematical implication is generally a directed hypergraph, not a tree:

```text
A + B + C -> D
```

So theorem rules should be kept separate from structural spines.

---

## 12. StructuralNodeSpec

A structural node is a certified regime or enrichment point. It is not merely an atomic predicate.

Examples:

```text
PartialOrderRelation(R,A)
PosetStructure(S)
EquivalenceRelation(R,A)
GroupStructure(S)
LatticeStructure(S)
```

A structural node bundles requirements and unlocks APIs.

```python
@dataclass
class StructuralNodeSpec:
    key: str
    parameters: tuple[str, ...]
    hard_gates: tuple[PredCall, ...] = ()
    requirements: tuple[PredCall, ...] = ()
    cheap_obstructions: tuple[PredCall, ...] = ()
    unlocks: tuple[str, ...] = ()
    explanation_template: str | None = None
```

Example:

```python
StructuralNodeSpec(
    key="PartialOrderRelation",
    parameters=("R", "A"),
    hard_gates=(
        PredCall("Relation", (Var("R"),)),
        PredCall("SetLike", (Var("A"),)),
    ),
    requirements=(
        PredCall("BinaryRelationOn", (Var("R"), Var("A"))),
        PredCall("ReflexiveOn", (Var("R"), Var("A"))),
        PredCall("AntisymmetricOn", (Var("R"), Var("A"))),
        PredCall("TransitiveOn", (Var("R"), Var("A"))),
    ),
    unlocks=("PartialOrderRelationFacet",)
)
```

Important distinction:

```text
TransitiveOn(R,A) = predicate/fact
PartialOrderRelation(R,A) = structural node
PosetStructure(S) = structural node
```

Predicates provide evidence. Structural nodes represent useful certified regimes that unlock methods, constructions, diagrams, induced objects, transport rules, and downstream recognition.

---

## 13. Facets / Views / Capabilities

A facet is an API unlocked by a certified structural node.

```python
class Facet:
    facet_name = "abstract"

    def __init__(self, workspace, record, certificate):
        self.workspace = workspace
        self.record = record
        self.certificate = certificate
```

Example:

```python
class PosetFacet(Facet):
    facet_name = "poset"

    def lower_set(self, x):
        ...

    def upper_set(self, x):
        ...

    def covers(self):
        ...

    def hasse_diagram(self):
        ...
```

Rule:

```text
Facets are outputs of certification.
They are not the central recognition mechanism.
```

The central mechanism is:

```text
PredicateSpecs + Facts + Certificates + StructuralNodeSpecs + Rules
```

---

## 14. Recognition / Certification Flow

### 14.1 Certifying a Predicate

Example user call:

```python
W.certify("Function", F)
```

Flow:

```text
1. Build target FactKey:
     Function(F)

2. Check FactIndex:
     Is Function(F) already known?

3. Ask PredicateRegistry:
     What is Function?

4. PredicateRegistry returns PredicateSpec:
     formal definition:
       Relation(F) ∧ SingleValuedRelation(F)

     possible checkers:
       finite_extensional_function_checker

5. Certification engine selects route:
     cached certificate?
     construction guarantee?
     theorem rule?
     direct checker?
     definitional decomposition?

6. Checker or rule runs.

7. Store Fact with Certificate.

8. Propagate theorem consequences if configured.

9. Return Fact / Certificate.
```

### 14.2 Direct Checker Example

```python
def check_finite_extensional_function(workspace, fact_key):
    F_record = workspace.record(fact_key.args[0])
    F_obj = F_record.obj

    if F_obj.object_kind != "Relation":
        return CheckResult.false(
            reason="Object is not relation-like.",
            witness=F_record.record_id,
        )

    seen = {}

    for pair in F_obj.entries():
        x, y = pair.left, pair.right

        if x in seen and seen[x] != y:
            return CheckResult.false(
                reason="Same input has two distinct outputs.",
                witness={
                    "input": x,
                    "first_output": seen[x],
                    "second_output": y,
                },
            )

        seen[x] = y

    return CheckResult.true(
        reason="Every input has at most one output."
    )
```

This corresponds to the formula:

```text
∀x ∀y1 ∀y2((<x,y1> ∈ F ∧ <x,y2> ∈ F) -> y1 = y2)
```

but it does not evaluate the full first-order formula literally. It uses the finite extensional representation.

### 14.3 Certifying a Structural Node

Example call:

```python
W.certify_node("PartialOrderRelation", R, A)
```

Flow:

```text
1. Instantiate StructuralNodeSpec:
     PartialOrderRelation(R,A)

2. Check hard gates:
     Relation(R)
     SetLike(A)

3. Try cheap obstructions:
     find missing diagonal pair
     find antisymmetry counterexample
     find transitivity counterexample

4. Certify requirements:
     BinaryRelationOn(R,A)
     ReflexiveOn(R,A)
     AntisymmetricOn(R,A)
     TransitiveOn(R,A)

5. If all true:
     store StructuralNode certificate
     cache downward implied facts
     attach facet

6. If some requirement false:
     store blocked node result with witness
```

---

## 15. Construction Guarantees

Operations that produce objects should return `ObjectDraft`s with metadata. This already fits the existing design.

Example:

```python
P = A.obj.cartesian_product(B.obj)
P_record = W.introduce(P, name="P")
```

The construction should emit:

```text
ConstructionRecord:
  name = "cartesian_product"
  inputs = {"left": A, "right": B}
  output_kind = "FiniteSet"

Definition:
  operation_expression = CartesianProduct(A,B)

Fact / guarantee:
  CartesianProduct(P,A,B) = TRUE
```

In the new logical layer, the guarantee becomes a certified fact:

```python
Fact(
    key=FactKey("CartesianProduct", args=(P_id, A_id, B_id)),
    status=FactStatus.TRUE,
    certificate=Certificate(
        source_type="CONSTRUCTION_GUARANTEE",
        claim=FactKey("CartesianProduct", args=(P_id, A_id, B_id)),
        source_key="cartesian_product_construction",
        explanation="P was constructed as the cartesian product of A and B."
    )
)
```

This lets the workspace know the product fact without recomputing the full definition.

---

## 16. Integration with Workspace

### 16.1 New Workspace Fields

```python
class Workspace:
    def __init__(self, *, equality_policy="link"):
        self.equality_policy = equality_policy

        self._records = {}
        self._name_to_id = {}
        self._registry = Registry()
        self._construction_graph = ConstructionGraph()

        # Existing / planned recognition machinery
        self._recognizers = []

        # New logical architecture
        self._predicate_registry = PredicateRegistry()
        self._fact_index = FactIndex()
        self._theorem_rules = RuleRegistry()
        self._structural_nodes = StructuralNodeRegistry()
        self._certification_engine = CertificationEngine(self)
```

### 16.2 New Public API

```python
class Workspace:
    def register_predicate(self, spec: PredicateSpec) -> None:
        ...

    def predicate(self, key: str) -> PredicateSpec:
        ...

    def expand_predicate(self, key: str, *args, depth=None):
        ...

    def definition_profile(self, key: str) -> DefinitionProfile:
        ...

    def certify(self, predicate_key: str, *records) -> Fact:
        ...

    def knows(self, predicate_key: str, *records) -> bool:
        ...

    def fact(self, predicate_key: str, *records) -> Fact | None:
        ...

    def why(self, predicate_key: str, *records) -> str:
        ...

    def register_theorem_rule(self, rule: TheoremRule) -> None:
        ...

    def certify_node(self, node_key: str, *records):
        ...
```

Example use:

```python
W.certify("Function", F)
W.why("Function", F)
W.expand_predicate("Function", F, depth=2)
W.definition_profile("Function")
```

### 16.3 ObjectRecord Integration

`ObjectRecord` may continue to store local facts, regimes, and facets, but the canonical source of cross-object facts should be workspace-level.

Suggested adjustment:

```text
ObjectRecord.facts
  local summary / object-centered facts

Workspace.FactIndex
  canonical fact store for all predicate instances
```

When the workspace certifies `Function(F)`, it can:

```text
1. Store FactKey("Function", F_id) in FactIndex.
2. Optionally add a summarized local fact to F_record.facts.
3. Attach a FunctionFacet if desired.
```

---

## 17. Integration with Registry and Equality

The registry already manages canonical keys and known equality. The logical layer should respect workspace-known equality.

If:

```text
W.knows_equal(A, B)
```

then a fact about `A` may be transferable to `B` depending on predicate invariance.

For early versions, keep this conservative:

```text
Do not automatically transfer arbitrary facts across equality classes unless the predicate is marked equality-invariant.
```

Add to `PredicateSpec` later:

```python
@dataclass
class PredicateSpec:
    ...
    equality_invariant: bool = True
```

Most ordinary mathematical predicates are equality-invariant, but some workspace-specific facts may not be.

Example:

```text
cardinality(A) = 3
```

transfers across equality.

But:

```text
introduced_by_roster(A)
```

does not necessarily transfer to every equal record, because it is about construction history, not mathematical equality.

This preserves the distinction between:

```text
mathematical facts
workspace/history facts
```

---

## 18. Integration with ConstructionGraph

The construction graph records how objects were produced. The logical layer should convert construction guarantees into certified facts.

Flow:

```text
Construction protocol runs
   ↓
Produces ObjectDraft
   ↓
Workspace.introduce creates ObjectRecord
   ↓
ConstructionEvent stored in ConstructionGraph
   ↓
Construction guarantees are converted into Facts
   ↓
Facts receive CONSTRUCTION_GUARANTEE certificates
```

Example:

```text
A.union(B) produces C
```

Possible guarantees:

```text
Union(C,A,B)
Finite(C)
A subset_of C
B subset_of C
```

The formal definition of `Union(C,A,B)` can live in `PredicateSpec`, but construction can certify it without rechecking the formula.

---

## 19. Integration with Recognition

The older recognizer model:

```text
Recognizer inspects records/facts/context
Recognizer certifies regimes
Recognizer attaches facets
```

The new model refines this:

```text
RecognitionEngine uses StructuralNodeSpecs.
StructuralNodeSpecs list PredicateSpec requirements.
CertificationEngine certifies missing predicates.
Certificates explain each step.
Facets are attached only after node certification.
```

Old:

```python
W.register_recognizer(PartialOrderRecognizer())
W.recognize(S)
```

New internal flow:

```text
PartialOrderRecognizer becomes either:

1. a StructuralNodeSpec for PartialOrderRelation(R,A), plus checkers for requirements; or
2. a thin adapter that calls W.certify_node("PartialOrderRelation", R, A).
```

This prevents recognizers from becoming opaque piles of custom logic.

---

## 20. Candidate Generation

When an object is introduced, the workspace should not try every possible predicate.

Candidate generation uses cheap shape information:

```text
object kind
arity
slots
carrier data
operation count
relation count
construction provenance
declared names
presentations
```

Examples:

```text
A Relation object suggests:
  Relation
  BinaryRelationOn if arity is 2
  EquivalenceRelation candidates
  PartialOrderRelation candidates

A Structure with carrier and one binary relation named leq suggests:
  OrderedStructure
  PosetStructure

A Structure with carrier and one binary operation suggests:
  Magma
  Semigroup
  Monoid
  Group
```

Candidate generation does not decide truth. It only chooses what might be worth certifying.

```text
Ranking chooses what to try first.
Certificates decide what is true.
```

---

## 21. Obstruction-First Checking

For structural nodes, checking should separate:

```text
hard gates
cheap obstructions
full certifying checks
```

Example for partial order:

```text
hard gates:
  R is relation-like
  A is set-like
  R is binary on A

cheap obstructions:
  find a ∈ A such that <a,a> ∉ R
  find a,b ∈ A such that aRb and bRa and a ≠ b
  find a,b,c ∈ A such that aRb and bRc and not aRc

full checks:
  full reflexivity
  full antisymmetry
  full transitivity
```

If obstruction found:

```text
store negative fact with witness
block target structural node
explain failure path
```

Example stored fact:

```text
TransitiveOn(R,A) = FALSE
witness = (a,b,c)
reason = aRb and bRc but not aRc
```

This failure should block:

```text
PreorderRelation(R,A)
PartialOrderRelation(R,A)
LatticeOrderRelation(R,A)
PosetStructure(S)
```

until the relevant object changes.

---

## 22. Downward Inheritance and Caching

Once a strong structural node is certified, cache its weaker consequences.

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

This avoids recomputation and improves explanation.

Every cached fact should carry a theorem or structural-inheritance certificate, not just appear silently.

---

## 23. Bridge Rules Between Spines

Separate spines are useful:

```text
Relation spine
Function spine
Structure spine
Set spine
Operation spine
```

But many certifications require bridges.

Example:

```text
PartialOrderRelation(R,A)
Structure S has carrier A and order slot R
------------------------------------------------
PosetStructure(S)
```

Bridge rule skeleton:

```python
@dataclass
class BridgeRule:
    key: str
    inputs: tuple[str, ...]
    required_nodes: tuple[PredCall, ...]
    required_predicates: tuple[PredCall, ...]
    produced_node: PredCall
```

Bridge rules keep object-class spines separate while allowing higher structures to be certified from components.

---

## 24. Suggested Module Layout

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
      free_vars
      substitute
      alpha_rename
      pretty

    predicates.py
      PredicateSpec
      PredicateRegistry
      DefinitionProfile
      ComputationProfile
      CheckerSpec
      expand_once
      expand_to_depth
      expand_to_primitives
      definition_depth
      quantifier_depth

    facts.py
      FactKey
      FactStatus
      Fact
      Certificate
      FactIndex

    rules.py
      TheoremRule
      RuleRegistry
      RuleEngine
      BridgeRule

    certification.py
      CheckResult
      CertificationEngine
      CertificationPlan
      CertificationStep

    structural.py
      StructuralNodeSpec
      StructuralNodeRegistry
      RecognitionEngine

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

  facets/
    base.py
    function.py
    poset.py
    lattice.py

  predicates/
    set_theory.py
    relation_theory.py
    function_theory.py
    order_theory.py
```

---

## 25. Minimum Viable Implementation Plan

### Phase L0: Formula AST

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

and:

```text
pretty
free_vars
bound_vars
substitute
alpha_rename
```

### Phase L1: Predicate Registry

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

### Phase L2: Expansion and Profiles

Implement:

```text
expand_once
expand_to_depth
expand_to_primitives
predicate_dependencies
definition_depth
quantifier_depth
DefinitionProfile
```

This gives immediate payoff for the membership-chase work.

### Phase L3: Facts and Certificates

Implement:

```text
FactKey
FactStatus
Fact
Certificate
FactIndex
```

Use these for cross-object facts.

### Phase L4: Checkers

Implement checkers for finite/extensional objects:

```text
Relation(R)
SingleValuedRelation(R)
Function(F)
CartesianProduct(P,A,B)
BinaryRelationOn(R,A)
ReflexiveOn(R,A)
SymmetricOn(R,A)
TransitiveOn(R,A)
AntisymmetricOn(R,A)
```

### Phase L5: CertificationEngine

Implement route order:

```text
1. cached fact
2. construction guarantee
3. theorem rule
4. direct checker
5. definitional decomposition
6. unknown / blocked
```

Keep it simple. No expensive planning yet.

### Phase L6: Structural Nodes

Implement:

```text
StructuralNodeSpec
StructuralNodeRegistry
RecognitionEngine
```

First nodes:

```text
FunctionObject(F)
EquivalenceRelation(R,A)
PartialOrderRelation(R,A)
PosetStructure(S)
```

### Phase L7: Facets

Attach facets only after structural certification:

```text
FunctionFacet
EquivalenceRelationFacet
PosetFacet
```

---

## 26. Example End-to-End: Function Certification

### 26.1 Setup

```python
W = Workspace()
register_set_theory_predicates(W)
register_relation_predicates(W)
register_function_predicates(W)
register_finite_relation_checkers(W)

F = W.introduce(
    Relation.from_entries({("a", 1), ("b", 2)}),
    name="F"
)
```

### 26.2 Certify

```python
fact = W.certify("Function", F)
```

### 26.3 Internal Meaning

```text
Function(F)
:<-> Relation(F) ∧ SingleValuedRelation(F)
```

### 26.4 Certification Route

```text
1. Relation(F)
   known by construction or checked from relation payload

2. SingleValuedRelation(F)
   checked by finite extensional checker

3. Function(F)
   certified by definitional decomposition
```

### 26.5 Stored Facts

```text
Relation(F) = TRUE
SingleValuedRelation(F) = TRUE
Function(F) = TRUE
```

### 26.6 Explanation

```text
F is a function because:

1. F is a relation.
2. F is single-valued.
3. Single-valued means no input appears with two distinct outputs.
4. The finite checker inspected all entries and found no conflict.
```

### 26.7 Optional Facet

```python
func = W.facet(F, "function")
func.domain()
func.range()
func.evaluate("a")
```

The facet is unlocked by the certified `Function(F)` fact or `FunctionObject(F)` structural node.

---

## 27. Example End-to-End: Cartesian Product

### 27.1 Setup

```python
A = W.introduce(FiniteSet.from_roster({1, 2}), name="A")
B = W.introduce(FiniteSet.from_roster({"x", "y"}), name="B")

P = W.introduce(A.obj.cartesian_product(B.obj), name="P")
```

### 27.2 Construction Guarantee

The `cartesian_product` operation should emit:

```text
CartesianProduct(P,A,B) = TRUE
```

with certificate:

```text
source_type = CONSTRUCTION_GUARANTEE
source_key = cartesian_product
```

### 27.3 Formal Meaning

The predicate still has the formal definition:

```text
CartesianProduct(P,A,B) :<->
  ∀w(w ∈ P <-> ∃x ∃y(x ∈ A ∧ y ∈ B ∧ KuratowskiPair(w,x,y)))
```

### 27.4 Explanation

```text
P is the cartesian product of A and B because it was produced by the cartesian_product construction.
The registered meaning of CartesianProduct(P,A,B) is that every member of P is exactly a Kuratowski pair <x,y> with x ∈ A and y ∈ B.
```

The workspace does not need to recompute the full formula unless explicitly requested.

---

## 28. Design Rules

### Rule 1

Do not make formulas the runtime representation of mathematical objects.

```text
Formula = meaning
MathObject = payload
Checker = feasible computation
```

### Rule 2

Do not make predicates random strings.

```text
PredicateSpec owns registered meaning.
```

### Rule 3

Do not make each predicate have exactly one checker.

```text
One predicate can have many certification routes.
```

### Rule 4

Do not confuse structural nodes with ordinary predicates.

```text
Predicates provide evidence.
Structural nodes unlock capabilities.
```

### Rule 5

Do not automatically run every checker.

```text
Candidate generation filters relevance.
Ranking chooses order.
Certificates decide truth.
```

### Rule 6

Store negative results with witnesses.

```text
False facts are useful mathematical information.
```

### Rule 7

Keep construction guarantees explicit.

```text
A constructed object should carry certified facts explaining what construction produced.
```

### Rule 8

Keep theorem rules separate from structural spines.

```text
Structural spines are tree-ish.
Logical implication is a hypergraph.
```

### Rule 9

Keep workspace-history claims separate from mathematical claims.

```text
A = B may transfer mathematical properties.
A = B does not mean both were introduced the same way.
```

### Rule 10

Start with a small kernel.

```text
Formula AST
PredicateSpec
FactKey
Certificate
CheckerSpec
```

Everything else should grow out of actual pressure from use cases.

---

## 29. Final Architecture Diagram

```text
                           ┌──────────────────────────────┐
                           │          Workspace            │
                           │  public mathematical ledger   │
                           └──────────────┬───────────────┘
                                          │
             ┌────────────────────────────┼────────────────────────────┐
             │                            │                            │
             v                            v                            v
   ┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
   │   ObjectRecord   │        │     Registry     │        │ ConstructionGraph│
   │ ledger entry     │        │ equality/index   │        │ provenance graph │
   └────────┬─────────┘        └──────────────────┘        └──────────────────┘
            │
            v
   ┌──────────────────┐
   │    MathObject    │
   │ payload object   │
   └──────────────────┘


   Logical Architecture inside Workspace:

   ┌─────────────────────┐
   │   PredicateRegistry │
   │ PredicateSpec       │
   │ FormalDefinition    │
   └──────────┬──────────┘
              │
              v
   ┌─────────────────────┐
   │     Formula AST     │
   │ Var, In, Eq, ...    │
   └──────────┬──────────┘
              │
              v
   ┌─────────────────────┐
   │ DefinitionProfile   │
   │ dependencies/depth  │
   └─────────────────────┘

   ┌─────────────────────┐
   │      FactIndex      │
   │ FactKey -> Fact     │
   └──────────┬──────────┘
              │
              v
   ┌─────────────────────┐
   │     Certificate     │
   │ why fact is known   │
   └──────────┬──────────┘
              │
              v
   ┌─────────────────────┐
   │ CertificationEngine │
   │ cached / guarantee  │
   │ theorem / checker   │
   └──────────┬──────────┘
              │
              v
   ┌─────────────────────┐
   │ StructuralNodeSpec  │
   │ regimes / APIs      │
   └──────────┬──────────┘
              │
              v
   ┌─────────────────────┐
   │    Facet / View     │
   │ certified API       │
   └─────────────────────┘
```

---

## 30. One-Sentence Summary

The added logical architecture makes predicate meanings first-class: formulas define what claims mean, checkers and theorem rules certify concrete instances, certificates preserve why the workspace knows them, and structural nodes/facets turn certified knowledge into usable mathematical APIs.
