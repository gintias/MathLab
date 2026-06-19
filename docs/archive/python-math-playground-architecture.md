# Meta-Level Architecture Spine

Absolutely. This should become the meta-level spine for the project: not the mathematics of sets, relations, and functions themselves, but the architecture that lets mathematical objects carry names, definitions, presentations, construction histories, facts, regimes, and explanations.

This is a working reference.

---

## 0. Governing Principle

The system is not merely a collection of Python classes like `FiniteSet`, `Relation`, `Function`, and `Structure`.

It is a **mathematical workspace**.

A mathematical workspace should remember:

```text
what objects have been introduced
how they were introduced
which names denote them
which definitions specify them
which presentations expose them
which construction paths produced them
which facts have been certified
which regimes have been recognized
which APIs/facets are unlocked
which objects are known equal or equivalent
```

So the top-level architecture is:

```text
MathObject
  the mathematical payload plus portable metadata

ObjectRecord
  the workspace-local record of an introduced object

Registry
  internal canonical/equality/indexing machinery

Workspace
  public mathematical environment / object ledger
```

The central split is:

> `MathObject` owns local mathematical payload. `Workspace` owns introduced mathematical history.

---

## 1. Core Stack

```text
Workspace
├── ObjectRecords
├── NameTable
├── Registry
├── EqualityGraph
├── FactIndex
├── ConstructionGraph
└── Regime / Facet management

ObjectRecord
├── record_id
├── underlying MathObject
├── names / aliases
├── presentations
├── definitional schemas
├── construction records
├── facts / certificates
├── regimes
├── facets
└── links to equal / equivalent records
```

The most important design constraint:

> `MathObject` must stay thin.

It should not become a god class.

---

## 2. Responsibility Boundaries

### 2.1 `MathObject`

A `MathObject` is the base class for mathematical payloads.

Examples:

```text
FiniteSet
FiniteTuple
BlockPair / RelationEntry
Relation
Function
Structure
Partition
QuotientSet
Algebra
ClosureOperator
```

`MathObject` owns:

```text
local name suggestion, if any
local presentations
local definitions
local provenance
local facts
local regimes
local facets
canonical_key hook
display hook
```

But object-specific subclasses own their mathematical invariants.

For example:

```text
FiniteSet owns:
  elements
  membership
  extensional equality
  union/intersection/powerset

Relation owns:
  entries
  arity profile
  domain/range
  inverse/restriction/image

Structure owns:
  carrier
  named relations/functions
  carrier-relative checks

MathObject owns:
  common metadata infrastructure
```

### 2.2 `ObjectRecord`

An `ObjectRecord` is not the mathematical object itself. It is the workspace's ledger entry for an introduced object.

It remembers:

```text
this object was introduced here
under these names
with these definitions
using these presentations
through these constructions
with these certified facts
with these recognized regimes
```

One mathematical object may have multiple records if the workspace is in non-merging/linking mode.

Alternatively, several introduction events may merge into one canonical record.

### 2.3 `Registry`

The `Registry` is internal machinery.

It answers:

```text
Have we seen an object with this canonical key?
Which record is canonical for this key?
Should this new object merge with an old record?
Are these records known equal?
```

The registry should not be the public conceptual API. It supports the workspace.

### 2.4 `Workspace`

The `Workspace` is the user-facing mathematical environment.

It answers:

```python
W.introduce(...)
W.define(...)
W.alias(...)
W.canonical(...)
W.knows_equal(...)
W.explain(...)
W.facts(...)
W.recognize(...)
W.construct(...)
```

It is the object ledger.

---

## 3. Foundational Distinctions

The system must keep these distinct.

### 3.1 Python identity

```python
A is B
```

This means two variables point to the exact same Python object.

Usually not mathematically meaningful.

### 3.2 Object equality

```python
A == B
```

This means the object class's equality method says they are equal.

For `FiniteSet`, this should mean same elements.

For `Relation`, this should mean same entries and same arity profile.

For `Structure`, this may mean same carrier plus same named interpretations.

### 3.3 Canonical-key equality

```python
A.canonical_key() == B.canonical_key()
```

This is what the registry uses for automatic lookup/merge.

The canonical key must be type-sensitive.

```python
("FiniteSet", frozenset({1, 2}))
```

is not the same kind of thing as:

```python
("FiniteTuple", (1, 2))
```

even if their raw Python payloads look related.

### 3.4 Workspace-known equality

```python
W.knows_equal(A, B)
```

This means the workspace has recorded/certified/merged that two records denote the same mathematical object.

This can be stronger or weaker than raw Python equality depending on the workspace policy.

### 3.5 Isomorphism / equivalence

```python
W.knows_isomorphic(A, B)
```

This is not equality.

For structures, algebras, posets, categories, etc., isomorphism matters but should not collapse objects unless explicitly requested.

---

## 4. `MathObject` Spine

### 4.1 Purpose

`MathObject` provides shared metadata infrastructure.

It should be inherited by every substantial mathematical object class.

### 4.2 Minimal responsibilities

```text
store local metadata
provide canonical key hook
provide object kind
provide basic explain hooks
allow facts/regimes/facets to attach
```

### 4.3 Anti-responsibilities

`MathObject` should not know:

```text
how to union sets
how to compose relations
how to check reflexivity
how to compute joins
how to evaluate functions
how to build quotient structures
```

Those belong to subclasses or construction protocols.

### 4.4 Suggested base shape

```python
class MathObject:
    """
    Thin base class for mathematical objects.
    Owns metadata infrastructure.
    Subclasses own mathematical invariants and operations.
    """

    object_kind = "MathObject"

    def __init__(
        self,
        *,
        name=None,
        presentation=None,
        definition=None,
        provenance=None,
    ):
        self.local_name = name
        self.presentations = []
        self.definitions = []
        self.provenance = []
        self.facts = FactStore()
        self.regimes = RegimeStore()
        self.facets = {}

        if presentation is not None:
            self.add_presentation(presentation)
        if definition is not None:
            self.add_definition(definition)
        if provenance is not None:
            self.add_provenance(provenance)

    def canonical_key(self):
        """
        Subclasses override.
        Must return a hashable key representing mathematical equality
        at the object level.
        """
        raise NotImplementedError

    def add_presentation(self, presentation):
        self.presentations.append(presentation)

    def add_definition(self, definition):
        self.definitions.append(definition)

    def add_provenance(self, record):
        self.provenance.append(record)

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_regime(self, regime):
        self.regimes.add(regime)

    def add_facet(self, name, facet):
        self.facets[name] = facet

    def has_fact(self, claim):
        return self.facts.has(claim)

    def has_regime(self, regime_name):
        return self.regimes.has(regime_name)
```

### 4.5 Required subclass hooks

Every major subclass should implement:

```python
canonical_key()
_validate()
_repr_payload()
```

Optional hooks:

```python
primary_presentation()
basic_facts()
default_display()
```

Example for `FiniteSet`:

```python
class FiniteSet(MathObject):
    object_kind = "FiniteSet"

    def __init__(self, elements, **metadata):
        super().__init__(**metadata)
        self._elements = frozenset(elements)
        self._validate()
        self._record_basic_facts()

    def canonical_key(self):
        return ("FiniteSet", self._elements)

    def _validate(self):
        # Usually no extra validation beyond hashability/finite materialization.
        pass

    def _record_basic_facts(self):
        self.add_fact(Fact("finite", True, reason="FiniteSet construction"))
        self.add_fact(
            Fact("cardinality", len(self._elements), reason="counted elements")
        )
```

---

## 5. Metadata Records

The metadata layer should be explicit. Avoid raw dictionaries everywhere once things stabilize.

### 5.1 `Presentation`

A presentation answers:

> How is this object accessed, displayed, computed, or stored?

Examples:

```text
ExtensionalPresentation
PredicatePresentation
CallablePresentation
ComputedPresentation
GeneratedPresentation
TablePresentation
```

Minimal shape:

```python
class Presentation:
    def __init__(self, kind, *, data=None, description=None):
        self.kind = kind
        self.data = data or {}
        self.description = description
```

Eventually, specialized presentations can implement:

```python
contains(...)
elements()
entries()
evaluate(...)
can_enumerate()
reify()
```

But at the meta-level, presentation is just one metadata category.

### 5.2 `DefinitionalSchema`

A definitional schema answers:

> What mode of mathematical definition specifies this object?

Important: this is broad-grained.

Good schema kinds:

```text
roster
comprehension
operation_expression
axiomatic_formation
replacement
image
graph
rule
unique_existence
recursive
generated_closure
named_collection
kernel
pullback
transport
quotient
```

Bad schema design:

```text
UnionSchema
IntersectionSchema
PowerSetSchema
```

Those are too granular. Union/intersection/powerset are expression/operator payloads inside `OperationExpressionDefinition`.

Minimal shape:

```python
class DefinitionalSchema:
    def __init__(
        self,
        kind,
        *,
        expression=None,
        variables=None,
        condition=None,
        data=None,
        description=None,
    ):
        self.kind = kind
        self.expression = expression
        self.variables = variables or ()
        self.condition = condition
        self.data = data or {}
        self.description = description
```

Examples:

```python
DefinitionalSchema(
    kind="roster",
    data={"elements": frozenset({2, 4, 6})},
)
```

```python
DefinitionalSchema(
    kind="comprehension",
    variables=("x",),
    condition=is_even,
    data={"universe": U},
)
```

```python
DefinitionalSchema(
    kind="operation_expression",
    expression=UnionExpression(A, B),
)
```

```python
DefinitionalSchema(
    kind="named_collection",
    expression=("Con", A),
    condition="theta is a congruence on A",
)
```

### 5.3 `Expression` / Operator

An expression/operator is payload inside some definitional schemas.

Examples:

```text
Union(A, B)
Intersection(A, B)
PowerSet(A)
CartesianProduct(A, B)
Image(f, A)
Preimage(f, B)
Composition(g, f)
Kernel(f)
TransitiveClosure(R)
```

An operator expression may know:

```text
operator name
input objects
output kind
membership law
algorithm
guarantees
```

Minimal shape:

```python
class Expression:
    def __init__(self, operator, args=(), *, kwargs=None):
        self.operator = operator
        self.args = tuple(args)
        self.kwargs = kwargs or {}
```

Example:

```python
UnionExpression = Expression("union", args=(A, B))
```

Later, specialized expression classes may be useful:

```python
class UnionExpression(Expression):
    ...
```

But those are expression nodes, not schema kinds.

### 5.4 `ConstructionRecord`

A construction record answers:

> How was this object produced?

It records active mathematical procedure/provenance.

Minimal shape:

```python
class ConstructionRecord:
    def __init__(
        self,
        name,
        *,
        inputs=None,
        output_kind=None,
        guarantees=None,
        data=None,
        description=None,
    ):
        self.name = name
        self.inputs = inputs or {}
        self.output_kind = output_kind
        self.guarantees = guarantees or []
        self.data = data or {}
        self.description = description
```

Examples:

```python
ConstructionRecord(
    name="from_roster",
    inputs={"elements": frozenset({2, 4, 6})},
    output_kind="FiniteSet",
)
```

```python
ConstructionRecord(
    name="filter_finite_universe",
    inputs={"universe": U, "predicate": is_even},
    output_kind="FiniteSet",
    guarantees=["output subset of universe"],
)
```

```python
ConstructionRecord(
    name="equivalence_from_partition",
    inputs={"partition": P},
    output_kind="Relation",
    guarantees=[
        "reflexive on carrier",
        "symmetric on carrier",
        "transitive on carrier",
        "equivalence relation",
    ],
)
```

### 5.5 `Fact`

A fact is a certified or asserted claim about an object.

Minimal shape:

```python
class Fact:
    def __init__(
        self,
        claim,
        value=True,
        *,
        subject=None,
        context=None,
        witness=None,
        reason=None,
        certificate=None,
    ):
        self.claim = claim
        self.value = value
        self.subject = subject
        self.context = context
        self.witness = witness
        self.reason = reason
        self.certificate = certificate
```

Examples:

```python
Fact("finite", True)
Fact("cardinality", 3)
Fact("subset_of", True, subject=A, context={"superset": U})
Fact("reflexive", True, subject=R, context={"carrier": A})
Fact("transitive", False, witness=("a", "b", "c"))
```

Facts should eventually support:

```text
positive facts
negative facts
unknown facts
witnesses
counterexamples
proof/certificate sources
context-sensitive claims
```

### 5.6 `RegimeCertificate`

A regime is a significant certified mathematical mode.

Examples:

```text
equivalence_relation
preorder
partial_order
poset
lattice
complete_lattice
closure_operator
generation_system
recursive_scheme
```

Shape:

```python
class RegimeCertificate:
    def __init__(
        self,
        name,
        *,
        subject=None,
        context=None,
        requirements=None,
        reason=None,
        data=None,
    ):
        self.name = name
        self.subject = subject
        self.context = context
        self.requirements = requirements or []
        self.reason = reason
        self.data = data or {}
```

Example:

```python
RegimeCertificate(
    "partial_order",
    subject=R,
    context={"carrier": A},
    requirements=["reflexive", "antisymmetric", "transitive"],
    reason="all required carrier-relative facts certified",
)
```

### 5.7 `Facet`

A facet is a specialized API unlocked by a regime.

Examples:

```text
PosetFacet
LatticeFacet
CompleteLatticeFacet
ClosureOperatorFacet
GenerationFacet
```

Facet rule:

> Do not expose specialized methods unless the corresponding regime is certified.

For example:

```python
record.facets["poset"].covers()
record.facets["lattice"].join(a, b)
```

---

## 6. Stores

### 6.1 `FactStore`

Purpose:

```text
store facts
retrieve facts by claim/context
avoid silent contradiction
preserve witnesses/reasons
```

Initial simple version:

```python
class FactStore:
    def __init__(self):
        self._facts = []

    def add(self, fact):
        self._facts.append(fact)

    def has(self, claim, *, context=None):
        return any(
            f.claim == claim and f.value is True
            for f in self._facts
        )

    def all(self):
        return list(self._facts)
```

Later version should index by:

```text
claim
subject
context
value
```

### 6.2 `RegimeStore`

Purpose:

```text
store certified regimes
retrieve regime data
attach facets
```

Simple version:

```python
class RegimeStore:
    def __init__(self):
        self._regimes = {}

    def add(self, regime):
        self._regimes[regime.name] = regime

    def has(self, name):
        return name in self._regimes

    def get(self, name):
        return self._regimes[name]
```

---

## 7. `ObjectRecord` Spine

### 7.1 Purpose

An `ObjectRecord` is the workspace-local ledger entry for one introduced object.

It is where names, definitions, facts, regimes, aliases, and construction histories accumulate.

### 7.2 Fields

```python
class ObjectRecord:
    def __init__(self, record_id, obj):
        self.id = record_id
        self.obj = obj
        self.kind = obj.object_kind
        self.canonical_key = obj.canonical_key()
        self.names = set()
        self.aliases = set()
        self.presentations = list(obj.presentations)
        self.definitions = list(obj.definitions)
        self.provenance = list(obj.provenance)
        self.facts = FactStore()
        self.regimes = RegimeStore()
        self.facets = {}
        self.construction_events = []
        self.equal_to = set()
        self.equivalent_to = set()
        self.status = "active"
```

### 7.3 What belongs on `ObjectRecord`

```text
workspace-local names
aliases
introduction events
merged definitions
merged presentations
merged provenance
workspace-certified facts
workspace-certified regimes
facets
links to equal records
links to isomorphic/equivalent records
```

### 7.4 What does not belong on `ObjectRecord`

The actual set elements, relation entries, function graph, etc. belong on the underlying object.

The record should not duplicate mathematical payload unless indexing demands it.

### 7.5 Absorbing metadata

When two records merge, the canonical record absorbs the other's metadata.

When absorbing an object:

```python
def absorb_object(self, obj):
    for p in obj.presentations:
        self.presentations.append(p)
    for d in obj.definitions:
        self.definitions.append(d)
    for r in obj.provenance:
        self.provenance.append(r)
    for fact in obj.facts.all():
        self.facts.add(fact)
    for regime in obj.regimes.all():
        self.regimes.add(regime)
```

When absorbing another record:

```python
def absorb_record(self, other):
    self.names |= other.names
    self.aliases |= other.aliases
    self.presentations.extend(other.presentations)
    self.definitions.extend(other.definitions)
    self.provenance.extend(other.provenance)
    self.construction_events.extend(other.construction_events)

    for fact in other.facts.all():
        self.facts.add(fact)
    for regime in other.regimes.all():
        self.regimes.add(regime)

    self.facets.update(other.facets)
    other.status = "merged"
```

### 7.6 Explanation duties

An `ObjectRecord` should be able to produce raw material for explanation:

```text
object display
names
definitions
presentations
facts
regimes
construction events
equal records
```

But final formatting can belong to `Workspace.explain`.

---

## 8. `Registry` Spine

### 8.1 Purpose

The `Registry` is internal indexing and equality/canonicalization machinery.

It should answer:

```text
Which canonical key maps to which record?
Which record is canonical?
Are two records known equal?
Should a new object merge with an existing one?
```

### 8.2 Internal data

```python
class Registry:
    def __init__(self):
        self.key_to_record_id = {}
        self.parent = {}  # union-find for known equality
```

The union-find lets us maintain known equalities without necessarily destroying records.

### 8.3 Required operations

```python
register_key(key, record_id)
lookup_key(key)
has_key(key)
canonical_id(record_id)
union_equal(record_id_1, record_id_2)
known_equal(record_id_1, record_id_2)
```

### 8.4 Merge versus link

The registry should support policies:

```text
fresh:
  always create a new record

merge:
  if canonical key exists, absorb into existing record

link:
  create a new record, but record known equality

manual:
  detect equality but require explicit merge/link
```

Recommended early default:

```text
link or merge=False while debugging
```

Long-term best:

```text
link records by equality; allow canonical views
```

because it preserves multiple construction paths without destructive merging.

### 8.5 Canonical key lookup

Example:

```python
key = obj.canonical_key()
if key in registry:
    existing_id = registry.lookup_key(key)
```

Then depending on policy:

```text
merge:
  absorb new metadata into existing record

link:
  create new record and union equality classes

fresh:
  create independent record
```

---

## 9. `Workspace` Spine

### 9.1 Purpose

The `Workspace` is the public mathematical environment.

It owns:

```text
records
names
registry
known equalities
construction graph
fact/regime recognition pipeline
explanation API
```

### 9.2 Core fields

```python
class Workspace:
    def __init__(self, *, equality_policy="link"):
        self.equality_policy = equality_policy
        self._records = {}
        self._name_to_id = {}
        self._registry = Registry()
        self._next_id = 0
        self._construction_graph = ConstructionGraph()
        self._recognizers = []
```

### 9.3 Core public API

#### Introduce

```python
W.introduce(obj, name=None, policy=None)
```

Meaning:

```text
Take a MathObject.
Create or update a workspace record.
Optionally bind a name.
Apply equality/canonicalization policy.
Return ObjectRecord or ObjectHandle.
```

#### Name

```python
W.name(record, "A")
```

Meaning:

```text
Bind a workspace-local name to a record.
```

#### Alias

```python
W.alias(record, "Even")
```

Meaning:

```text
Bind another name to the same record.
```

#### Lookup

```python
W.get("A")
```

Meaning:

```text
Return the record denoted by name A.
```

#### Canonical

```python
W.canonical(record)
```

Meaning:

```text
Return canonical representative of record's known-equality class.
```

#### Known equality

```python
W.knows_equal(A, B)
```

Meaning:

```text
Return True iff workspace knows the records denote equal mathematical objects.
```

#### Assert equality

```python
W.assert_equal(A, B, reason=None, certificate=None)
```

Meaning:

```text
Record equality between two records.
Possibly merge or link depending on policy.
```

#### Explain

```python
W.explain(A)
```

Meaning:

```text
Display names, definitions, presentations, provenance, facts, regimes, construction.
```

#### Facts

```python
W.add_fact(A, fact)
W.facts(A)
W.has_fact(A, claim)
```

#### Regimes

```python
W.recognize(A)
W.has_regime(A, "poset")
W.facet(A, "poset")
```

---

## 10. Workspace Introduction Flow

### 10.1 Object-first flow

```python
obj = FiniteSet.from_roster({2, 4, 6})
A = W.introduce(obj, name="A")
```

Flow:

```text
1. Object factory creates MathObject.
2. Object carries local metadata.
3. Workspace computes canonical key.
4. Registry checks if key is known.
5. Workspace creates/links/merges ObjectRecord.
6. Workspace binds name "A".
7. Workspace returns record/handle.
```

### 10.2 Workspace-first flow, later

Eventually:

```python
A = W.define_set("A").by_roster({2, 4, 6})
```

or:

```python
Even = W.define_set("Even").by_comprehension(U, is_even)
```

This is nicer, but not necessary for version one.

### 10.3 Construction flow

```python
C_obj = A.obj.union(B.obj)
C = W.introduce(C_obj, name="C")
```

Later:

```python
C = W.construct("union", A, B, name="C")
```

Flow:

```text
1. Workspace calls construction protocol.
2. Protocol validates inputs.
3. Protocol produces MathObject.
4. Protocol emits metadata/facts/guarantees.
5. Workspace introduces output.
6. Workspace records construction edge.
```

---

## 11. Construction Graph

### 11.1 Purpose

The construction graph records how objects were produced from prior objects.

Examples:

```text
A ----\
       union ---> C
B ----/

A ---> powerset ---> P

Partition ---> equivalence_from_partition ---> Relation

Relation ---> quotient ---> QuotientSet
```

### 11.2 Construction event

```python
class ConstructionEvent:
    def __init__(
        self,
        name,
        *,
        input_records=None,
        output_record=None,
        protocol=None,
        guarantees=None,
        data=None,
    ):
        self.name = name
        self.input_records = input_records or []
        self.output_record = output_record
        self.protocol = protocol
        self.guarantees = guarantees or []
        self.data = data or {}
```

### 11.3 Workspace use

```python
W.construction_history(C)
W.explain_construction(C)
W.paths_to(C)
```

Long-term, this becomes incredibly useful for explanation and debugging.

---

## 12. Equality and Merging Policy

### 12.1 Policies

#### Fresh

```text
Always create a new record.
Never merge automatically.
```

Use for debugging.

#### Merge

```text
If canonical key already exists, absorb metadata into existing record.
Return canonical record.
```

Use for a clean mathematical notebook style.

#### Link

```text
Always create a new record, but if keys match, record known equality.
Canonical view available.
```

Use for preserving construction histories.

#### Manual

```text
Detect equality but require explicit W.merge or W.assert_equal.
```

Use when equality has to be justified.

### 12.2 Recommended early policy

Use `link` or `fresh` early.

Why?

Because you want to inspect different introductions before deciding how aggressive canonicalization should be.

### 12.3 Recommended mature policy

Use `link` as the default.

Reason:

```text
It preserves introduction events and construction paths,
while still allowing canonical equality queries.
```

---

## 13. Naming Model

### 13.1 Names are workspace-local

The object may have a suggested local name, but the workspace owns actual names.

```python
W.name(A, "A")
W.alias(A, "Even")
```

### 13.2 Name table

```python
_name_to_id: dict[str, record_id]
```

### 13.3 Name conflicts

Options:

```text
raise error
shadow name in nested workspace
allow rebinding with explicit overwrite=True
```

For version one:

> raise on duplicate names.

### 13.4 Aliases

An alias is another name for the same record/equality class.

```python
W.alias(A, "Even")
```

Should fail if `"Even"` already denotes a different record unless explicitly forced.

---

## 14. Context-Sensitive Facts

This is crucial for relations and structures.

A bare relation `R` does not own facts like reflexive/transitive in isolation unless a carrier is specified.

Reflexivity means:

```text
∀a ∈ A, (a, a) ∈ R.
```

So the fact should be:

```python
Fact(
    "reflexive",
    subject=R,
    context={"carrier": A},
    value=True,
)
```

Not:

```python
R.add_fact("reflexive")
```

without context.

### 14.1 Fact context examples

```text
R reflexive on A
R transitive on A
f monotone relative to poset P
c extensive relative to order ≤
S closed under operation *
```

### 14.2 Workspace role

The workspace can store indexed facts like:

```python
(subject_id, claim, context_key) -> Fact
```

Version one can keep this simple, but the model should anticipate context.

---

## 15. Regime Recognition Pipeline

### 15.1 Recognizers

A recognizer is a designed object that consumes records and certifies regimes.

Shape:

```python
class RegimeRecognizer:
    name = "abstract"

    def applies_to(self, workspace, record):
        raise NotImplementedError

    def check(self, workspace, record):
        raise NotImplementedError

    def certify(self, workspace, record):
        raise NotImplementedError
```

Examples:

```text
EquivalenceRelationRecognizer
PreorderRecognizer
PartialOrderRecognizer
PosetRecognizer
LatticeRecognizer
CompleteLatticeRecognizer
ClosureOperatorRecognizer
```

### 15.2 Recognizer flow

```text
1. Check input type/context.
2. Verify required facts.
3. If needed, compute facts with witnesses.
4. Add regime certificate.
5. Attach facet.
6. Emit downstream facts.
```

### 15.3 Example: partial order

```text
Input:
  Structure record S
  relation name leq

Requirements:
  leq is relation on carrier
  reflexive on carrier
  antisymmetric on carrier
  transitive on carrier

Output:
  RegimeCertificate("partial_order")
  PosetFacet
```

### 15.4 Workspace API

```python
W.register_recognizer(PartialOrderRecognizer())
W.recognize(S)
W.has_regime(S, "poset")
W.facet(S, "poset")
```

---

## 16. Facet Attachment

Facets are specialized APIs.

Example:

```python
po = W.facet(S, "poset")
po.covers()
po.lower_set(x)
po.hasse_diagram()
```

Facet should retain:

```text
workspace
record
certifying regime
relevant data
```

Shape:

```python
class Facet:
    def __init__(self, workspace, record, certificate):
        self.workspace = workspace
        self.record = record
        self.certificate = certificate
```

---

## 17. Example Walkthrough: Sets

```python
W = Workspace(equality_policy="link")

A = W.introduce(
    FiniteSet.from_roster({2, 4, 6}),
    name="A",
)

U = W.introduce(
    FiniteSet.from_roster({1, 2, 3, 4, 5, 6}),
    name="U",
)

Even = W.introduce(
    FiniteSet.from_predicate(U.obj, lambda x: x % 2 == 0),
    name="Even",
)
```

Expected workspace state:

```text
Records:
  r1: FiniteSet {2,4,6}, name A
  r2: FiniteSet {1,2,3,4,5,6}, name U
  r3: FiniteSet {2,4,6}, name Even

Registry:
  r1 and r3 have same canonical key

Equality:
  r1 = r3 known by canonical key

Definitions:
  r1: roster {2,4,6}
  r3: comprehension {x in U : x even}

Presentations:
  r1: extensional
  r3: extensional and/or predicate
```

```python
W.knows_equal(A, Even) = True
```

If policy is `merge`, then `A` and `Even` may be the same record with two names and two definitions.

If policy is `link`, they remain distinct records but are known equal.

---

## 18. Example Walkthrough: Relation and Structure

```python
R = W.introduce(
    Relation.from_entries({("1", "1"), ("1", "2"), ...}),
    name="divides_relation",
)

S = W.introduce(
    Structure(
        carrier=A.obj,
        relations={"leq": R.obj},
    ),
    name="DivPoset",
)

W.recognize(S)
```

Expected flow:

```text
Relation object:
  validates entries and arity profile

Structure object:
  supplies carrier-relative interpretation

Recognizer:
  checks leq reflexive on carrier
  checks leq antisymmetric on carrier
  checks leq transitive on carrier

Facts:
  reflexive(leq, carrier=A)
  antisymmetric(leq, carrier=A)
  transitive(leq, carrier=A)

Regime:
  partial_order / poset

Facet:
  PosetFacet attached
```

Important:

```text
R itself is not globally “reflexive.”
R is reflexive on carrier A inside structure S.
```

---

## 19. Versioned Implementation Plan

### Phase M0: metadata records

Implement:

```text
Presentation
DefinitionalSchema
Expression
ConstructionRecord
Fact
RegimeCertificate
FactStore
RegimeStore
```

No advanced logic.

### Phase M1: `MathObject`

Implement thin base class.

Required:

```text
presentations
definitions
provenance
facts
regimes
facets
canonical_key hook
```

### Phase M2: `FiniteSet` integration

Make `FiniteSet(MathObject)`.

Implement:

```text
from_roster
from_predicate
union
intersection
difference
powerset
```

Each should attach metadata.

Use broad schemas:

```text
roster
comprehension
operation_expression
```

### Phase M3: `ObjectRecord`

Implement record wrapper.

Store:

```text
id
obj
names
definitions
presentations
provenance
facts
regimes
facets
status
```

### Phase M4: `Registry`

Implement canonical-key lookup and equality tracking.

Support policies:

```text
fresh
merge
link
```

### Phase M5: `Workspace`

Implement:

```text
introduce
name
alias
get
canonical
knows_equal
assert_equal
explain
```

### Phase M6: construction graph

Implement:

```text
ConstructionEvent
ConstructionGraph
W.construction_history(record)
```

### Phase M7: relation/structure integration

Implement:

```text
FiniteTuple
BlockPair / RelationEntry
Relation
Structure
```

Then carrier-relative facts.

### Phase M8: regimes and facets

Implement first recognizers:

```text
EquivalenceRelationRecognizer
PartialOrderRecognizer
PosetFacet
```

Then expand later.

---

## 20. Non-Negotiable Design Rules

### Rule 1

> `MathObject` is metadata infrastructure, not mathematical omniscience.

### Rule 2

> `Workspace` owns names and introduced-object history.

### Rule 3

> `Registry` is internal; `Workspace` is public.

### Rule 4

> Definitional schemas are modes of definition, not one per operation.

### Rule 5

> Operations like union/powerset are expression/operator payloads.

### Rule 6

> Facts must carry context when context matters.

Especially relation facts.

### Rule 7

> Regimes unlock facets; atomic facts do not become random subclasses.

### Rule 8

> Equality, isomorphism, and aliasing are different.

### Rule 9

> Automatic metadata transfer only happens through certified construction guarantees.

### Rule 10

> Start lightweight; let consumers force abstraction.

---

## 21. Final Reference Diagram

```text
User / code introduces object
        |
        v
MathObject subclass
  - validates mathematical payload
  - carries local metadata
  - provides canonical_key
        |
        v
Workspace.introduce
  - creates ObjectRecord
  - binds name
  - consults Registry
  - links/merges equal records
  - stores construction event
        |
        v
ObjectRecord
  - names
  - definitions
  - presentations
  - provenance
  - facts
  - regimes
  - facets
        |
        v
Registry
  - canonical keys
  - known equality
  - canonical representatives
        |
        v
Recognizers
  - inspect records/facts/context
  - certify regimes
  - attach facets
        |
        v
Workspace.explain / Workspace.query
  - object history
  - aliases
  - definitions
  - construction paths
  - certified facts
  - available APIs
```

The spine in one sentence:

> The `Workspace` is the mathematical ledger; `MathObject` is the payload; `ObjectRecord` is the ledger entry.

That should be the main meta-level reference going forward.
