# Search-to-Logic Integration for the Mathematical Workspace

## 0. Executive Summary

The core idea is to add a **search/evidence engine** beside the existing mathematical workspace and logical layer.

The search engine explores a large finite or symbolic space, but instead of returning only raw candidates, it returns a structured bundle of **facts, witnesses, counterexamples, counts, residual constraints, and coverage certificates**. The logical layer then translates that bundle into `FactKey`, `Fact`, `Certificate`, and possibly new `ObjectDraft`s. The workspace absorbs these into its `FactIndex`, `ConstructionGraph`, `ObjectRecord`s, theorem-rule engine, structural-node recognizer, and facets.

```text
Search explores spaces.
Logic translates results into durable facts.
Workspace stores, propagates, explains, and reuses those facts.
```

This turns search from a one-off computation into a reusable mathematical knowledge source.

---

## 1. Current Architecture Assumption

The existing architecture already has four major layers:

```text
MathObject      = mathematical payload / instantiation template
ObjectRecord    = workspace-local ledger entry
Registry        = equality / canonical-key machinery
Workspace       = public mathematical environment / object ledger
```

The logical layer adds:

```text
Formula AST
PredicateSpec
FactKey
Fact
Certificate
CheckerSpec
TheoremRule
StructuralNodeSpec
Facet
```

The proposed search layer adds:

```text
SearchSpace
SearchQuery
SearchResultBundle
SearchCoverage
FactDelta
SearchEngine
SearchTranslator
```

So the full pipeline becomes:

```text
MathObject payloads compute concrete data.
Formula ASTs describe mathematical meaning.
PredicateSpecs register vocabulary.
SearchEngines explore spaces and produce evidence.
SearchTranslators convert evidence into logical facts.
FactIndex stores known claims.
TheoremRules propagate consequences.
StructuralNodeSpecs certify regimes.
Facets expose APIs unlocked by certified regimes.
Workspace.explain shows what is known and why.
```

---

## 2. Core Insight

A search result should not be treated as merely:

```text
list[candidate]
```

It should be treated as:

```text
mathematical evidence package
```

A good search result says:

```text
what space was searched
what assumptions were imposed
whether the search was exhaustive
how many candidates survived
which facts are true of all survivors
which facts are false, with counterexamples
which witnesses were found
which constraints remain unresolved
which objects can be introduced into the workspace
which formulas should be stored for later use
```

This is exactly what the logical layer needs.

---

## 3. Why This Matters

Without the search-to-logic bridge, a computation dies after it returns an answer.

Example:

```text
Search all binary relations on A and find 15 equivalence relations.
```

If this only returns a Python list, the workspace learns very little.

With the bridge, the workspace can store:

```text
S = {R ∈ Rel(A,A) : EquivalenceRelation(R,A)}
Cardinality(S) = 15
∀R ∈ S, Relation(R)
∀R ∈ S, ReflexiveOn(R,A)
∀R ∈ S, SymmetricOn(R,A)
∀R ∈ S, TransitiveOn(R,A)
```

Now future computations can reuse this information.

The search result becomes a reusable object of knowledge, not a temporary result.

---

## 4. Search as a Generalized Checker

A normal checker answers one predicate instance:

```text
Is TransitiveOn(R,A) true?
```

A search engine answers broader questions:

```text
Among all R ∈ Rel(A,A), which satisfy ReflexiveOn(R,A) and SymmetricOn(R,A)?
How many survive?
Do all survivors satisfy TransitiveOn(R,A)?
Find one counterexample if not.
Find one witness if yes/existential.
```

So:

```text
CheckerSpec
  certifies one claim

SearchEngine
  explores a family and emits many claims
```

The search engine is not separate from the logical layer. It is a high-powered evidence producer.

---

## 5. Main Data Flow

```text
User / program issues query
        ↓
Formula AST represents the query
        ↓
Search planner builds SearchSpace
        ↓
SearchEngine explores candidates
        ↓
SearchResultBundle is returned
        ↓
SearchTranslator emits FactDelta
        ↓
Workspace.absorb_fact_delta(delta)
        ↓
FactIndex stores facts
        ↓
RuleEngine propagates consequences
        ↓
StructuralNodeSpecs certify regimes
        ↓
Facets become available
        ↓
Workspace.explain can explain all of it
```

---

## 6. Core Objects

### 6.1 `SearchSpace`

A `SearchSpace` describes the universe being explored.

Examples:

```text
Rel(A,A)
Func(A,B)
P(P(A))
All binary operations on A
All partitions of A
All structures with carrier A and one binary relation
```

Sketch:

```python
@dataclass
class SearchSpace:
    key: str
    variables: tuple["SearchVariable", ...]
    ambient_formula: Formula
    estimated_size: object | None = None
    presentations: list[Presentation] = field(default_factory=list)
    data: dict = field(default_factory=dict)
```

Example:

```python
SearchSpace(
    key="binary_relations_on_A",
    variables=(SearchVariable("R", Rel(A, A)),),
    ambient_formula=PredCall("BinaryRelationOn", (Var("R"), ObjRef(A_id))),
    estimated_size=2 ** (len(A) * len(A)),
)
```

---

### 6.2 `SearchQuery`

A `SearchQuery` says what to impose and what to ask.

```python
@dataclass
class SearchQuery:
    space: SearchSpace
    assumptions: tuple[Formula, ...] = ()
    asks: tuple[Formula, ...] = ()
    mode: str = "exhaustive"
    limits: dict = field(default_factory=dict)
```

Example:

```python
SearchQuery(
    space=Rel(A, A),
    assumptions=(
        PredCall("ReflexiveOn", (Var("R"), ObjRef(A_id))),
        PredCall("SymmetricOn", (Var("R"), ObjRef(A_id))),
    ),
    asks=(
        PredCall("TransitiveOn", (Var("R"), ObjRef(A_id))),
        PredCall("EquivalenceRelation", (Var("R"), ObjRef(A_id))),
    ),
    mode="exhaustive",
)
```

---

### 6.3 `SearchCoverage`

Coverage is crucial. It says whether the result is proof, evidence, or conjecture.

```python
@dataclass
class SearchCoverage:
    exhaustive: bool
    searched_count: int | None = None
    total_count: int | None = None
    bounds: dict = field(default_factory=dict)
    method: str | None = None
    engine: str | None = None
```

Examples:

```text
exhaustive = true
searched_count = 65536
total_count = 65536
```

This can certify universal claims over the searched space.

But:

```text
exhaustive = false
bounds = {"carrier_size": "<= 5"}
```

This cannot certify a theorem. It can only produce conjectural or bounded evidence.

Design rule:

```text
No coverage, no strong certificate.
```

---

### 6.4 `SearchResultBundle`

The search result bundle is the raw result before workspace absorption.

```python
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
```

The bundle is not yet necessarily part of the workspace. It is an evidence artifact.

---

### 6.5 `FactDelta`

A `FactDelta` is what gets absorbed into the workspace.

```python
@dataclass
class FactDelta:
    source: str
    facts: list[Fact] = field(default_factory=list)
    generated_objects: list[ObjectDraft] = field(default_factory=list)
    construction_events: list[ConstructionEvent] = field(default_factory=list)
    residual_constraints: list[Formula] = field(default_factory=list)
    explanation: str | None = None
```

The workspace method:

```python
def absorb_fact_delta(self, delta: FactDelta) -> None:
    ...
```

should:

```text
1. insert facts into FactIndex
2. introduce generated ObjectDrafts if requested
3. attach witnesses and counterexamples to certificates
4. update ObjectRecord summaries
5. run theorem propagation
6. attempt structural-node certification
7. refresh facets if new regimes became available
```

---

## 7. Certificate Statuses

Search results should use the existing fact-status discipline:

```text
TRUE
FALSE
UNKNOWN
INAPPLICABLE
BLOCKED
ASSUMED
CONJECTURAL
STALE
```

Important cases:

### Exhaustive search proving truth

```text
FactStatus.TRUE
Certificate.source_type = COMPUTED
coverage.exhaustive = true
```

### Found counterexample

```text
FactStatus.FALSE
Certificate.source_type = FAILED_WITH_WITNESS
certificate.witness = counterexample
```

### Bounded search found no counterexample

```text
FactStatus.CONJECTURAL
Certificate.source_type = CONJECTURAL
coverage.exhaustive = false
```

### Meaningful but unresolved

```text
FactStatus.UNKNOWN
Certificate.source_type = UNKNOWN
residual_formula = ...
```

---

## 8. Hypothetical 1: Binary Relation Search

Let:

```text
A = {a,b,c,d}
```

Search:

```text
S = {R ∈ Rel(A,A) : ReflexiveOn(R,A) ∧ SymmetricOn(R,A)}
```

The raw relation space has size:

```text
|Rel(A,A)| = 2^(4*4) = 65536
```

Reflexivity forces four diagonal bits:

```text
(a,a), (b,b), (c,c), (d,d)
```

Symmetry pairs off the twelve off-diagonal bits into six independent choices:

```text
{a,b}, {a,c}, {a,d}, {b,c}, {b,d}, {c,d}
```

So the search result says:

```text
candidate_count = 2^6 = 64
```

The logical translation stores:

```text
SearchFamily(S)
SubsetOf(S, Rel(A,A))
Cardinality(S) = 64
∀R ∈ S, ReflexiveOn(R,A)
∀R ∈ S, SymmetricOn(R,A)
```

If later refined by transitivity:

```text
T = {R ∈ S : TransitiveOn(R,A)}
```

then:

```text
Cardinality(T) = 15
∀R ∈ T, EquivalenceRelation(R,A)
```

Now `T` can be introduced as a mathematical object, explained, used as input to another search, or exported to another program.

---

## 9. Hypothetical 2: Obstruction-First Structural Certification

Goal:

```text
Certify PartialOrderRelation(R,A)
```

A structural node has requirements:

```text
BinaryRelationOn(R,A)
ReflexiveOn(R,A)
AntisymmetricOn(R,A)
TransitiveOn(R,A)
```

The search engine first tries cheap obstructions.

For transitivity it searches:

```text
∃a∈A ∃b∈A ∃c∈A
  (aRb ∧ bRc ∧ not aRc)
```

If it finds:

```text
a = 1
b = 2
c = 4
1 R 2
2 R 4
not 1 R 4
```

then it emits:

```python
Fact(
    key=FactKey("TransitiveOn", args=(R_id, A_id)),
    status=FactStatus.FALSE,
    certificate=Certificate(
        source_type="FAILED_WITH_WITNESS",
        source_key="transitivity_obstruction_search",
        witness={"a": 1, "b": 2, "c": 4},
        explanation="Found aRb and bRc but not aRc."
    )
)
```

Then the workspace can store:

```text
PartialOrderRelation(R,A) = BLOCKED
PreorderRelation(R,A) = BLOCKED
PosetStructure(S) = BLOCKED
```

This is extremely useful. A failed search becomes a reusable mathematical counterexample.

---

## 10. Hypothetical 3: Function Search

Let:

```text
A = {a,b,c,d}
B = {0,1}
```

Search:

```text
f ∈ Func(A,B)
f(a) = 1
f(b) = 1
SurjectiveFunction(f,A,B)
```

Without constraints:

```text
|Func(A,B)| = 2^4 = 16
```

The assignments `f(a)=1` and `f(b)=1` leave:

```text
f(c), f(d)
```

free, so there are four remaining functions.

Surjectivity requires at least one of `f(c), f(d)` to be `0`.

So the surviving assignments are:

```text
f(c)=0, f(d)=0
f(c)=0, f(d)=1
f(c)=1, f(d)=0
```

The search returns:

```text
candidate_count = 3
```

It also determines:

```text
SurjectiveFunction(f,A,B) = TRUE for all survivors
InjectiveFunction(f,A,B) = FALSE for all survivors
BijectiveFunction(f,A,B) = FALSE for all survivors
```

The reason for non-injectivity is already forced:

```text
a ≠ b
f(a) = 1
f(b) = 1
```

That becomes a negative fact with a witness:

```text
InjectiveFunction(f,A,B) = FALSE
witness = (a,b)
```

---

## 11. Hypothetical 4: Search Creates a New Object

Query:

```text
Find f ∈ Func(A,B) such that InjectiveFunction(f,A,B) and not SurjectiveFunction(f,A,B)
```

If the engine finds one, it should emit both:

```text
Existential fact:
∃f ∈ Func(A,B), InjectiveFunction(f,A,B) ∧ not SurjectiveFunction(f,A,B)
```

and:

```text
Witness object:
f0 = {...}
```

The workspace then does:

```python
f0 = W.introduce(result.witness_function, name="f0")
W.absorb_fact_delta(result.to_fact_delta())
```

Stored facts:

```text
Function(f0)
InjectiveFunction(f0,A,B)
SurjectiveFunction(f0,A,B) = FALSE
```

The witness is now a normal workspace object.

---

## 12. Hypothetical 5: Conjecture Mining

Search through all small structures up to some bound:

```text
For all tested structures S of size <= 5,
if P(S), then Q(S).
```

If no counterexample is found, the system must not store a theorem.

It stores:

```text
Conjectural implication:
P(S) -> Q(S)
```

with certificate:

```text
source_type = CONJECTURAL
searched_sizes = [1,2,3,4,5]
counterexamples_found = 0
coverage.exhaustive = false for the unrestricted theorem
coverage.exhaustive = true only within the tested finite bound
```

If later a counterexample is found, the conjecture can be downgraded or marked refuted.

---

## 13. Integration with `FactIndex`

The workspace should use `FactIndex` as the canonical store for cross-object facts.

Search-derived facts should enter exactly like checker-derived or theorem-derived facts:

```python
workspace.fact_index.add(fact)
```

Examples:

```text
TransitiveOn(R,A) = FALSE
Cardinality(S) = 64
EquivalenceRelation(R,A) = TRUE
ForAllIn(S, R, ReflexiveOn(R,A)) = TRUE
ExistsIn(Func(A,B), f, Injective(f) ∧ not Surjective(f)) = TRUE
```

The important point:

```text
Search results become ordinary logical facts once translated.
```

---

## 14. Integration with `ConstructionGraph`

A search can produce a new object, such as:

```text
S = {R ∈ Rel(A,A) : ReflexiveOn(R,A) ∧ SymmetricOn(R,A)}
```

That should create a construction event:

```python
ConstructionEvent(
    name="search_comprehension",
    input_records=[A_id],
    output_record=S_id,
    protocol="exhaustive_relation_search",
    guarantees=[
        "SubsetOf(S, Rel(A,A))",
        "ForAllIn(S, R, ReflexiveOn(R,A))",
        "ForAllIn(S, R, SymmetricOn(R,A))",
    ],
    data={"candidate_count": 64},
)
```

So `Workspace.explain(S)` can say:

```text
S was produced by an exhaustive search over Rel(A,A), filtering for reflexive and symmetric relations.
The search was exhaustive and found 64 candidates.
```

---

## 15. Integration with `PredicateSpec`

The search engine should not invent predicate meanings.

It should use registered `PredicateSpec`s.

Bad:

```text
search says: "R is good"
```

Good:

```text
search says: FactKey("TransitiveOn", (R_id, A_id)) = TRUE
```

Why?

Because `PredicateSpec("TransitiveOn")` already knows:

```text
formal definition
allowed arguments
pretty printer
checkers
expansion behavior
theorem-rule connections
```

Search then becomes one more certification route for registered mathematical vocabulary.

---

## 16. Integration with `TheoremRule`

After a fact delta is absorbed, theorem propagation should run.

Example stored fact:

```text
EquivalenceRelation(R,A) = TRUE
```

Theorem rules derive:

```text
Relation(R)
BinaryRelationOn(R,A)
ReflexiveOn(R,A)
SymmetricOn(R,A)
TransitiveOn(R,A)
```

Each derived fact should receive a certificate:

```text
source_type = THEOREM
premises = [EquivalenceRelation(R,A)]
source_key = equivalence_relation_implies_reflexive_symmetric_transitive
```

This makes the search result multiply its usefulness.

---

## 17. Integration with `StructuralNodeSpec` and Facets

Search can certify the requirements of a structural node.

Example:

```text
PartialOrderRelation(R,A)
```

Requirements:

```text
BinaryRelationOn(R,A)
ReflexiveOn(R,A)
AntisymmetricOn(R,A)
TransitiveOn(R,A)
```

If search/checking certifies all four, then the structural node is certified.

The workspace then attaches:

```text
PosetFacet
```

Now methods become available:

```python
W.facet(S, "poset").covers()
W.facet(S, "poset").minimal_elements()
W.facet(S, "poset").hasse_diagram()
```

The facet should know which certificate unlocked it.

---

## 18. Integration with External Programs

The search bundle can export to other systems.

Possible exports:

```text
SAT clauses
SMT constraints
NetworkX graph
pandas table
JSON evidence bundle
SQL query
Prolog facts
Lean/Coq theorem skeleton
Graphviz diagram
```

Examples:

```python
bundle.as_sat()
bundle.as_networkx()
bundle.as_json()
bundle.as_table()
bundle.as_fact_delta()
```

This makes the workspace an orchestration layer:

```text
external program searches or computes
workspace receives certified facts
logical layer preserves meaning
```

---

## 19. Suggested Module Layout

```text
structlab/
  core/
    formulas.py
    predicates.py
    facts.py
    rules.py
    certification.py
    structural.py

  search/
    spaces.py
      SearchSpace
      SearchVariable
      CandidateFamily

    queries.py
      SearchQuery

    coverage.py
      SearchCoverage

    results.py
      SearchResultBundle
      FactDelta

    engines.py
      SearchEngine
      ExhaustiveSearchEngine
      BacktrackingSearchEngine
      SATSearchEngine
      GraphSearchEngine

    translators.py
      result_to_fact_delta
      witness_to_object_draft
      counterexample_to_certificate
      coverage_to_certificate

    planners.py
      SearchPlanner
      CandidateGenerator

  checkers/
    finite_sets.py
    relations.py
    functions.py
    orders.py

  objects/
    finite_set.py
    relation.py
    function.py
    structure.py

  facets/
    base.py
    poset.py
    function.py
```

---

## 20. Workspace API Additions

Minimal public API:

```python
class Workspace:
    def search(
        self,
        *,
        variables,
        assumptions=(),
        asks=(),
        mode="auto",
        limits=None,
    ) -> SearchResultBundle:
        ...

    def absorb_fact_delta(self, delta: FactDelta) -> None:
        ...

    def absorb_search_result(self, result: SearchResultBundle) -> None:
        return self.absorb_fact_delta(result.to_fact_delta())
```

Possible usage:

```python
result = W.search(
    variables=[R.in_(Rel(A, A))],
    assumptions=[ReflexiveOn(R, A), SymmetricOn(R, A)],
    asks=[TransitiveOn(R, A), EquivalenceRelation(R, A)],
    mode="exhaustive",
)

W.absorb_search_result(result)
```

---

## 21. Minimal Implementation Plan

### Phase S0: Search result containers

Implement:

```text
SearchCoverage
SearchResultBundle
FactDelta
```

No search engine yet. Manually create bundles and test absorption.

### Phase S1: FactDelta absorption

Implement:

```text
Workspace.absorb_fact_delta
Workspace.absorb_search_result
```

Make sure facts go into `FactIndex` and optionally into object-local summaries.

### Phase S2: Exhaustive search over finite sets

Implement a tiny brute-force engine for:

```text
subsets of a finite set
relations on a finite set
functions between finite sets
```

### Phase S3: Translator from search result to facts

Implement:

```text
candidate_count -> Cardinality fact
found counterexample -> FALSE fact with witness
all candidates satisfy P -> ForAllIn fact
exists witness -> ExistsIn fact + ObjectDraft
```

### Phase S4: Relation/order searches

Implement:

```text
ReflexiveOn
SymmetricOn
TransitiveOn
AntisymmetricOn
EquivalenceRelation
PartialOrderRelation
```

Use obstruction-first checking.

### Phase S5: Theorem propagation

After absorption, run theorem rules.

Example:

```text
EquivalenceRelation(R,A)
  -> ReflexiveOn(R,A)
  -> SymmetricOn(R,A)
  -> TransitiveOn(R,A)
```

### Phase S6: Structural node certification

If search certifies all requirements, unlock facets.

Example:

```text
PartialOrderRelation(R,A) -> PosetFacet
```

### Phase S7: External backends

Add optional engines:

```text
SAT
SMT
NetworkX
pandas
custom backtracking
```

Do not start here. Start with brute force and clean certificates.

---

## 22. Key Design Rules

### Rule 1

Search results must not enter the workspace as strings.

They must enter as:

```text
FactKey + FactStatus + Certificate
```

### Rule 2

Every strong fact must have coverage.

```text
exhaustive search -> TRUE/FALSE possible
bounded non-exhaustive search -> CONJECTURAL/UNKNOWN
```

### Rule 3

Negative facts are valuable.

A counterexample should be stored with the failed predicate.

### Rule 4

Generated witnesses should become workspace objects when useful.

Search can introduce objects.

### Rule 5

The search engine should use registered PredicateSpecs.

It should not invent meanings.

### Rule 6

Search-derived facts should trigger theorem propagation.

### Rule 7

Structural nodes and facets should be downstream of facts, not separate custom logic.

### Rule 8

Keep the first implementation small.

Start with finite brute-force search and evidence bundles.

### Rule 9

Store residual constraints.

Not every search fully resolves a formula.

### Rule 10

Make explanations first-class.

The system should be able to say:

```text
I know this because this search was exhaustive over this space and found this witness / checked all candidates.
```

---

## 23. Final Mental Model

The workspace becomes a mathematical memory system.

```text
Objects are introduced.
Definitions give meaning.
Search explores possibilities.
Results become certified facts.
Facts trigger theorem rules.
Rules certify structural nodes.
Structural nodes unlock facets.
Facets generate new constructions and searches.
```

The loop is:

```text
construct → search → certify → store → propagate → unlock → construct more
```

This is the main payoff.

The program is no longer merely a collection of Python classes. It becomes a lightweight mathematical laboratory where computation, search, logic, and explanation feed each other.
