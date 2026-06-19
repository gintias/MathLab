Exactly. Here is the rough class skeleton I’d use now. This is not final implementation; it is a **shape guide**. It follows your current spine: `MathObject` is the instantiation template; `ObjectRecord` is the ledger entry; `Workspace` is the mathematical environment. That matches the architecture in your uploaded spine. 

# 0. Suggested module layout

```text
structlab/
  core/
    math_object.py
    metadata.py
    records.py
    registry.py
    workspace.py
    construction.py
  objects/
    finite_set.py
  recognizers/
    base.py
  facets/
    base.py
```

For now, only `FiniteSet` is real. Everything else is scaffolding.

---

# 1. Metadata skeletons

These are dumb containers. No cleverness yet.

```python
# core/metadata.py

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Presentation:
    """
    How the object is presented/computed/displayed.
    Example kinds:
        extensional
        predicate
        table
        generated
        symbolic
    """
    kind: str
    data: dict[str, Any] = field(default_factory=dict)
    description: Optional[str] = None


@dataclass
class DefinitionalSchema:
    """
    Broad-grained mode of definition.

    Good kinds:
        roster
        comprehension
        operation_expression
        generated_closure
        quotient
        kernel
        image
        preimage
    """
    kind: str
    expression: Any = None
    variables: tuple[str, ...] = ()
    condition: Any = None
    data: dict[str, Any] = field(default_factory=dict)
    description: Optional[str] = None


@dataclass
class Expression:
    """
    Operator-level payload inside a definition.

    Examples:
        union(A, B)
        intersection(A, B)
        powerset(A)
        image(f, A)
        kernel(f)
    """
    operator: str
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] = field(default_factory=dict)


@dataclass
class ConstructionRecord:
    """
    Records the procedure that produced an object.
    """
    name: str
    inputs: dict[str, Any] = field(default_factory=dict)
    output_kind: Optional[str] = None
    guarantees: list[str] = field(default_factory=list)
    description: Optional[str] = None
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class Fact:
    """
    Certified or asserted claim.

    Important:
        Facts may be object-local or context-sensitive.
    """
    claim: str
    value: Any = True
    subject: Any = None
    context: dict[str, Any] = field(default_factory=dict)
    witness: Any = None
    reason: Optional[str] = None
    certificate: Any = None


@dataclass
class RegimeCertificate:
    """
    Significant certified mathematical mode.

    Examples:
        partial_order
        poset
        lattice
        closure_operator
    """
    name: str
    subject: Any = None
    context: dict[str, Any] = field(default_factory=dict)
    requirements: list[str] = field(default_factory=list)
    reason: Optional[str] = None
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class InitialMetadata:
    """
    Metadata emitted at instantiation time.

    This is not the living ledger.
    This is the initial packet handed to the ObjectRecord.
    """
    presentations: list[Presentation] = field(default_factory=list)
    definitions: list[DefinitionalSchema] = field(default_factory=list)
    provenance: list[ConstructionRecord] = field(default_factory=list)
    facts: list[Fact] = field(default_factory=list)
    regimes: list[RegimeCertificate] = field(default_factory=list)
```

The key idea here is `InitialMetadata`. That lets `MathObject` stay a template while still allowing constructors like `FiniteSet.from_roster(...)` to emit metadata.

---

# 2. Object draft / instantiation packet

This is the bridge between object creation and workspace introduction.

```python
# core/math_object.py

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from .metadata import InitialMetadata


T = TypeVar("T", bound="MathObject")


@dataclass
class ObjectDraft(Generic[T]):
    """
    A newly instantiated mathematical payload plus its initial metadata.

    Fact:
        This is not yet a workspace object.
        It becomes a ledger entry only after Workspace.introduce(...).
    """
    obj: T
    metadata: InitialMetadata


class MathObject(ABC):
    """
    Abstract instantiation template for mathematical payloads.

    This is not the ledger.
    This is not the registry.
    This is not the workspace.

    Subclasses implement actual mathematical payload behavior.
    """

    object_kind: str = "MathObject"

    @abstractmethod
    def validate(self) -> None:
        """
        Check that the payload is internally well-formed.
        """
        raise NotImplementedError

    @abstractmethod
    def canonical_key(self) -> tuple:
        """
        Return a hashable key for object-level equality.

        For FiniteSet:
            ("FiniteSet", frozenset(elements))
        """
        raise NotImplementedError

    @abstractmethod
    def display_payload(self) -> str:
        """
        Human-facing mathematical display of the payload.
        """
        raise NotImplementedError

    def default_metadata(self) -> InitialMetadata:
        """
        Fallback metadata if object was instantiated directly
        rather than through a rich factory.
        """
        return InitialMetadata()
```

This makes `MathObject` exactly what you said: an instantiation template.

---

# 3. Stores

Very simple for now.

```python
# core/records.py

from dataclasses import dataclass, field
from typing import Any, Optional

from .metadata import (
    Presentation,
    DefinitionalSchema,
    ConstructionRecord,
    Fact,
    RegimeCertificate,
    InitialMetadata,
)
from .math_object import MathObject


class FactStore:
    def __init__(self):
        self._facts: list[Fact] = []

    def add(self, fact: Fact) -> None:
        ...

    def has(self, claim: str, *, context: Optional[dict[str, Any]] = None) -> bool:
        ...

    def all(self) -> list[Fact]:
        ...


class RegimeStore:
    def __init__(self):
        self._regimes: dict[str, RegimeCertificate] = {}

    def add(self, regime: RegimeCertificate) -> None:
        ...

    def has(self, name: str) -> bool:
        ...

    def get(self, name: str) -> RegimeCertificate:
        ...

    def all(self) -> list[RegimeCertificate]:
        ...
```

---

# 4. ObjectRecord

This is where the living memory starts.

```python
# core/records.py continued


@dataclass
class ObjectRecord:
    """
    Workspace-local ledger entry for an introduced object.

    This is where names, definitions, construction events,
    facts, regimes, facets, equality links, and status accumulate.
    """

    record_id: int
    obj: MathObject

    kind: str = field(init=False)
    canonical_key: tuple = field(init=False)

    names: set[str] = field(default_factory=set)
    aliases: set[str] = field(default_factory=set)

    presentations: list[Presentation] = field(default_factory=list)
    definitions: list[DefinitionalSchema] = field(default_factory=list)
    provenance: list[ConstructionRecord] = field(default_factory=list)

    facts: FactStore = field(default_factory=FactStore)
    regimes: RegimeStore = field(default_factory=RegimeStore)

    facets: dict[str, Any] = field(default_factory=dict)

    construction_events: list[Any] = field(default_factory=list)

    equal_to: set[int] = field(default_factory=set)
    equivalent_to: set[int] = field(default_factory=set)

    status: str = "active"

    def __post_init__(self):
        self.kind = self.obj.object_kind
        self.canonical_key = self.obj.canonical_key()

    def absorb_initial_metadata(self, metadata: InitialMetadata) -> None:
        """
        Copy instantiation metadata into the ledger record.
        """
        ...

    def add_name(self, name: str) -> None:
        ...

    def add_alias(self, alias: str) -> None:
        ...

    def add_fact(self, fact: Fact) -> None:
        ...

    def add_regime(self, regime: RegimeCertificate) -> None:
        ...

    def add_facet(self, name: str, facet: Any) -> None:
        ...

    def absorb_record(self, other: "ObjectRecord") -> None:
        """
        Merge another record into this one.

        Used only under merge policy or explicit user request.
        """
        ...

    def display(self) -> str:
        """
        Basic object display, delegating payload display to obj.
        """
        ...
```

Important: `ObjectRecord` stores the metadata; `MathObject` emits an initial packet or supplies default hooks.

---

# 5. Registry

The registry is internal identity/equality machinery.

```python
# core/registry.py

from typing import Optional


class Registry:
    """
    Internal canonical-key and equality-class manager.

    It does not own the public API.
    Workspace owns the public API.
    """

    def __init__(self):
        self.key_to_record_id: dict[tuple, int] = {}
        self.parent: dict[int, int] = {}

    def register_record(self, key: tuple, record_id: int) -> None:
        ...

    def has_key(self, key: tuple) -> bool:
        ...

    def lookup_key(self, key: tuple) -> Optional[int]:
        ...

    def make_record_node(self, record_id: int) -> None:
        """
        Initialize union-find node.
        """
        ...

    def canonical_id(self, record_id: int) -> int:
        """
        Union-find find operation.
        """
        ...

    def union_equal(self, left_id: int, right_id: int) -> None:
        """
        Record that two records are known equal.
        """
        ...

    def known_equal(self, left_id: int, right_id: int) -> bool:
        ...
```

Policy decisions do **not** belong in the registry. The registry knows how to register/link. The workspace decides whether to fresh/link/merge/manual.

---

# 6. Workspace

This is the main public interface.

```python
# core/workspace.py

from typing import Any, Optional

from .math_object import MathObject, ObjectDraft
from .metadata import InitialMetadata, Fact
from .records import ObjectRecord
from .registry import Registry
from .construction import ConstructionGraph


class Workspace:
    """
    Public mathematical environment.

    Owns:
        records
        names
        equality policy
        registry
        construction graph
        recognizers
        explanations
    """

    def __init__(self, *, equality_policy: str = "link"):
        self.equality_policy = equality_policy

        self._records: dict[int, ObjectRecord] = {}
        self._name_to_id: dict[str, int] = {}

        self._registry = Registry()
        self._construction_graph = ConstructionGraph()

        self._recognizers: list[Any] = []
        self._next_id = 0

    # ------------------------------------------------------------
    # Introduction
    # ------------------------------------------------------------

    def introduce(
        self,
        thing: MathObject | ObjectDraft,
        *,
        name: Optional[str] = None,
        policy: Optional[str] = None,
    ) -> ObjectRecord:
        """
        Introduce a mathematical object or object draft into the workspace.

        Flow:
            1. extract obj + initial metadata
            2. create ObjectRecord
            3. consult Registry by canonical_key
            4. apply equality policy
            5. bind name
            6. return record
        """
        ...

    def _new_record(
        self,
        obj: MathObject,
        metadata: InitialMetadata,
        *,
        name: Optional[str] = None,
    ) -> ObjectRecord:
        ...

    def _apply_equality_policy(
        self,
        new_record: ObjectRecord,
        existing_record: Optional[ObjectRecord],
        *,
        policy: str,
    ) -> ObjectRecord:
        """
        Policies:
            fresh
            link
            merge
            manual
        """
        ...

    # ------------------------------------------------------------
    # Names
    # ------------------------------------------------------------

    def name(self, record: ObjectRecord, name: str) -> None:
        ...

    def alias(self, record: ObjectRecord, alias: str) -> None:
        ...

    def get(self, name: str) -> ObjectRecord:
        ...

    # ------------------------------------------------------------
    # Equality
    # ------------------------------------------------------------

    def canonical(self, record: ObjectRecord) -> ObjectRecord:
        ...

    def knows_equal(self, left: ObjectRecord, right: ObjectRecord) -> bool:
        ...

    def assert_equal(
        self,
        left: ObjectRecord,
        right: ObjectRecord,
        *,
        reason: Optional[str] = None,
        certificate: Any = None,
    ) -> None:
        ...

    def merge(self, left: ObjectRecord, right: ObjectRecord) -> ObjectRecord:
        """
        Destructively merge records, preserving metadata.
        """
        ...

    # ------------------------------------------------------------
    # Facts
    # ------------------------------------------------------------

    def add_fact(self, record: ObjectRecord, fact: Fact) -> None:
        ...

    def facts(self, record: ObjectRecord) -> list[Fact]:
        ...

    def has_fact(self, record: ObjectRecord, claim: str, *, context=None) -> bool:
        ...

    # ------------------------------------------------------------
    # Recognition / facets
    # ------------------------------------------------------------

    def register_recognizer(self, recognizer: Any) -> None:
        ...

    def recognize(self, record: ObjectRecord) -> None:
        ...

    def has_regime(self, record: ObjectRecord, regime_name: str) -> bool:
        ...

    def facet(self, record: ObjectRecord, facet_name: str) -> Any:
        ...

    # ------------------------------------------------------------
    # Explanation
    # ------------------------------------------------------------

    def explain(self, record: ObjectRecord) -> str:
        ...

    def explain_identity(self, record: ObjectRecord) -> str:
        ...

    def construction_history(self, record: ObjectRecord):
        ...
```

This is the heart of the architecture.

---

# 7. Construction graph

Keep it skeletal.

```python
# core/construction.py

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ConstructionEvent:
    """
    Workspace-level event recording how a record was produced
    from earlier records.
    """

    name: str
    input_records: list[int] = field(default_factory=list)
    output_record: Optional[int] = None

    protocol: Optional[str] = None
    guarantees: list[str] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)


class ConstructionGraph:
    """
    Directed graph of construction dependencies.
    """

    def __init__(self):
        self.events: list[ConstructionEvent] = []
        self.inputs_to_events: dict[int, list[int]] = {}
        self.output_to_event: dict[int, int] = {}

    def add_event(self, event: ConstructionEvent) -> None:
        ...

    def history_of(self, record_id: int) -> list[ConstructionEvent]:
        ...

    def inputs_of(self, record_id: int) -> list[int]:
        ...

    def outputs_depending_on(self, record_id: int) -> list[int]:
        ...
```

---

# 8. FiniteSet payload

This is the first real object.

```python
# objects/finite_set.py

from typing import Any, Callable, Iterable, Optional

from structlab.core.math_object import MathObject, ObjectDraft
from structlab.core.metadata import (
    InitialMetadata,
    Presentation,
    DefinitionalSchema,
    ConstructionRecord,
    Fact,
    Expression,
)


class FiniteSet(MathObject):
    """
    Concrete finite set payload.

    Responsibilities:
        - store finite extensional payload
        - validate payload
        - provide membership/cardinality/basic operations
        - provide canonical key

    Non-responsibilities:
        - workspace names
        - equality links
        - construction graph
        - accumulated ledger history
    """

    object_kind = "FiniteSet"

    # ------------------------------------------------------------
    # Low-level constructor
    # ------------------------------------------------------------

    def __init__(self, elements: Iterable[Any]):
        self._elements = frozenset(elements)
        self.validate()

    def validate(self) -> None:
        """
        Check payload is acceptable.

        Version one:
            - elements materialize finitely
            - elements are hashable if using frozenset
        """
        ...

    def canonical_key(self) -> tuple:
        return ("FiniteSet", self._elements)

    def display_payload(self) -> str:
        ...

    # ------------------------------------------------------------
    # Rich factories returning ObjectDrafts
    # ------------------------------------------------------------

    @classmethod
    def from_roster(
        cls,
        elements: Iterable[Any],
        *,
        description: Optional[str] = None,
    ) -> ObjectDraft["FiniteSet"]:
        """
        Build a finite set from explicit roster data.

        Returns:
            ObjectDraft(FiniteSet, InitialMetadata)
        """
        obj = cls(elements)

        metadata = InitialMetadata(
            presentations=[
                Presentation(
                    kind="extensional",
                    data={"elements": obj._elements},
                    description="Explicit finite element presentation.",
                )
            ],
            definitions=[
                DefinitionalSchema(
                    kind="roster",
                    data={"elements": obj._elements},
                    description=description,
                )
            ],
            provenance=[
                ConstructionRecord(
                    name="from_roster",
                    inputs={"elements": obj._elements},
                    output_kind="FiniteSet",
                )
            ],
            facts=[
                Fact("finite", True, reason="FiniteSet construction"),
                Fact("cardinality", len(obj._elements), reason="counted elements"),
            ],
        )

        return ObjectDraft(obj=obj, metadata=metadata)

    @classmethod
    def from_predicate(
        cls,
        universe: "FiniteSet",
        predicate: Callable[[Any], bool],
        *,
        description: Optional[str] = None,
    ) -> ObjectDraft["FiniteSet"]:
        """
        Build {x in universe : predicate(x)}.

        Requires:
            universe is finite/enumerable.
        """
        ...

    @classmethod
    def empty(cls) -> ObjectDraft["FiniteSet"]:
        ...

    @classmethod
    def singleton(cls, x: Any) -> ObjectDraft["FiniteSet"]:
        ...

    # ------------------------------------------------------------
    # Basic access
    # ------------------------------------------------------------

    def elements(self) -> frozenset[Any]:
        ...

    def cardinality(self) -> int:
        ...

    def contains(self, x: Any) -> bool:
        ...

    def is_empty(self) -> bool:
        ...

    def is_singleton(self) -> bool:
        ...

    def __contains__(self, x: Any) -> bool:
        ...

    def __iter__(self):
        ...

    def __len__(self) -> int:
        ...

    # ------------------------------------------------------------
    # Set comparisons
    # ------------------------------------------------------------

    def is_subset_of(self, other: "FiniteSet") -> bool:
        ...

    def is_proper_subset_of(self, other: "FiniteSet") -> bool:
        ...

    def is_superset_of(self, other: "FiniteSet") -> bool:
        ...

    def is_disjoint_from(self, other: "FiniteSet") -> bool:
        ...

    # ------------------------------------------------------------
    # Set operations returning ObjectDrafts
    # ------------------------------------------------------------

    def union(self, other: "FiniteSet") -> ObjectDraft["FiniteSet"]:
        """
        Return self union other with metadata.
        """
        result = FiniteSet(self._elements | other._elements)

        metadata = InitialMetadata(
            presentations=[
                Presentation(
                    kind="extensional",
                    data={"elements": result._elements},
                )
            ],
            definitions=[
                DefinitionalSchema(
                    kind="operation_expression",
                    expression=Expression("union", args=(self, other)),
                )
            ],
            provenance=[
                ConstructionRecord(
                    name="union",
                    inputs={"left": self, "right": other},
                    output_kind="FiniteSet",
                    guarantees=[
                        "contains all elements of left",
                        "contains all elements of right",
                    ],
                )
            ],
            facts=[
                Fact("finite", True, reason="union of finite sets is finite"),
                Fact("cardinality", len(result._elements), reason="counted elements"),
            ],
        )

        return ObjectDraft(obj=result, metadata=metadata)

    def intersection(self, other: "FiniteSet") -> ObjectDraft["FiniteSet"]:
        ...

    def difference(self, other: "FiniteSet") -> ObjectDraft["FiniteSet"]:
        ...

    def symmetric_difference(self, other: "FiniteSet") -> ObjectDraft["FiniteSet"]:
        ...

    def power_set(self) -> ObjectDraft["FiniteSet"]:
        ...

    def cartesian_product(self, other: "FiniteSet") -> ObjectDraft["FiniteSet"]:
        ...

    def filter(self, predicate: Callable[[Any], bool]) -> ObjectDraft["FiniteSet"]:
        ...
```

The big design move here is: **operations return `ObjectDraft`s**, not just raw payloads. That way every construction carries its metadata into the workspace.

---

# 9. Recognizer base, for later

Do not implement these yet beyond the skeleton.

```python
# recognizers/base.py

from structlab.core.records import ObjectRecord
from structlab.core.workspace import Workspace


class RegimeRecognizer:
    """
    Designed recognizer for significant mathematical regimes.

    Not random certification.
    Not arbitrary property scanning.
    """

    name: str = "abstract_recognizer"

    def applies_to(self, workspace: Workspace, record: ObjectRecord) -> bool:
        ...

    def check(self, workspace: Workspace, record: ObjectRecord):
        """
        Perform checks and return result/certificate data.
        """
        ...

    def certify(self, workspace: Workspace, record: ObjectRecord):
        """
        Attach regime certificate and facet if successful.
        """
        ...
```

---

# 10. Facet base, for later

```python
# facets/base.py

from structlab.core.records import ObjectRecord
from structlab.core.workspace import Workspace
from structlab.core.metadata import RegimeCertificate


class Facet:
    """
    Specialized API unlocked by a certified regime.
    """

    facet_name: str = "abstract_facet"

    def __init__(
        self,
        workspace: Workspace,
        record: ObjectRecord,
        certificate: RegimeCertificate,
    ):
        self.workspace = workspace
        self.record = record
        self.certificate = certificate
```

---

# 11. First usage target

This is the first thing the skeleton should support conceptually:

```python
from structlab.core.workspace import Workspace
from structlab.objects.finite_set import FiniteSet


W = Workspace(equality_policy="link")

U = W.introduce(
    FiniteSet.from_roster({1, 2, 3, 4, 5, 6}),
    name="U",
)

A = W.introduce(
    FiniteSet.from_roster({2, 4, 6}),
    name="A",
)

Even = W.introduce(
    FiniteSet.from_predicate(
        U.obj,
        lambda x: x % 2 == 0,
        description="{x in U : x is even}",
    ),
    name="Even",
)

W.knows_equal(A, Even)
W.explain(Even)
W.canonical(Even)
```

Expected conceptual state:

```text
U:
  FiniteSet {1,2,3,4,5,6}

A:
  FiniteSet {2,4,6}
  introduced by roster

Even:
  FiniteSet {2,4,6}
  introduced by comprehension over U

Workspace:
  knows A and Even are equal by canonical key
  preserves both construction paths under link policy
```

---

# 12. Minimal build order

I’d implement in this order:

```text
1. Metadata containers
2. MathObject + ObjectDraft
3. FiniteSet.from_roster
4. ObjectRecord
5. Registry
6. Workspace.introduce
7. Workspace.get / name / knows_equal / canonical
8. FiniteSet.from_predicate
9. FiniteSet.union/intersection/difference
10. Workspace.explain
```

Do not touch relations yet. Do not touch regimes yet. Do not touch facets yet.

The first win is:

[
\boxed{
A = {2,4,6},\quad
Even = {x\in U:x\text{ even}},
\quad
W \text{ knows } A=Even \text{ while preserving both introductions.}
}
]
