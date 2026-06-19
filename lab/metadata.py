from dataclasses import dataclass, field
from typing import Any, Optional, Generic, TypeVar
from abc import ABC, abstractmethod

@dataclass
class Presentation:
    """
    How the object is presented/computed/displayed/

    Examples:
        extensional
        predicate
        table
        generated
        symbolic
        infinite family
    """
    kind: str
    data: dict[str, Any] = field(default_factory=dict)
    description: Optional[str] = None


# Examples of presentation dataclass
ext_pres = Presentation(
    kind="Extensional",
    data={"elements": frozenset({2,4,6})},
    description="Explicit element listsing"
)

predicate_pres = Presentation(
    kind="Prediate",
    data={"universe": frozenset({1,2,3,4,5}), "predicate": "x % 2 == 0"}
)

@dataclass
class DefinitionalSchema:
    """
    Broad-grained mode of definition

    Examples:
        Set roster
        Set comprehension
        Function value at a point
        Predicate condition of a relation
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
    Operator-level payload inside a definition
    """
    operator: str
    args: tuple[Any, ...] = ()
    kwargs: dict[str, Any] = field(default_factory=dict)
    

@dataclass
class ConstructionRecord:
    """
    Records the procedure that produced an objet
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
    Certified or asserted claim. May be object-local / context sensitive.
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
    Siginificant certified mathematical mode.

    Examples:
        partial order
        lattice
        closure operator
    """
    name: str
    subject: Any = None
    context: dict[str, Any] = field(default_factory = dict)
    requirements: list[str] = field(default_factory=list)
    reason: Optional[str] = None
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class InitialMetadata:
    """
    Metadata admitted at instantiation time.
    Initial data packet handed to ObjectRecord.
    """
    presentations: list[Presentation] = field(default_factory=list)
    definitions: list[DefinitionalSchema] = field(default_factory=list)
    provenance: list[ConstructionRecord] = field(default_factory=list)
    facts: list[Fact] = field(default_factory=list)
    regimes: list[RegimeCertificate] = field(default_factory=list)