from dataclasses import dataclass, field
from typing import Any, Optional, Generic, TypeVar
from abc import ABC, abstractmethod

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
    """
    Container for facts about an object.
    """

    def __init__(self):
        self._facts: list[Fact] = []

    def add(self, fact: Fact) -> None:
        """
        Add a fact.
        
        """
        self._facts.append(fact)

    def has(self, claim: str, *, context: Optional[dict[str, Any]] = None) -> bool:
        """
        Check if a claim exists, optionally with specific context.
    
        """
        for fact in self._facts:
            if fact.claim == claim:
                if context is None:
                    return True
                if fact.context == context:
                    return True
            
        return False
    
    def all(self) -> list[Fact]:
        """
        Return all facts.

        """
        return self._facts.copy()
    

class RegimeStore:
    """
    Container for regime certificates.

    """

    def __init__(self):
        self._regimes: dict[str, RegimeCertificate] = {}

    def add(self, regime: RegimeCertificate) -> None:
        """
        Add a regime certifiate by name.

        """
        self._regimes[regime.name] = regime

    def has(self, name: str) -> bool:
        """
        Check if a regime is certified.
        """
        return name in self._regimes

    def get(self, name: str) -> RegimeCertificate:
        """
        Retrieve a regime certificate.
        Raises KeyError if not found.
        """
        return self._regimes[name]

    def all(self) -> list[RegimeCertificate]:
        """
        Return all regime certificates.
        """
        return list(self._regimes.values())
    

@dataclass
class ObjectRecord:
    """
    Workspace-loal ledger entry for an introduced object.

    Amalgamates names, definitions, construction events, facts, regimes, 
    facets, equality, links, and status.
    
    """
    record_id: int
    obj: MathObject

    kind: str = field(init=False)
    canonical_key: tuple = field(init=False)

    #names and aliases
    names: set[str] = field(default_factory=set)
    aliases: set[str] = field(default_factory=set)

    # Mathematical metadata
    presentations: list[Presentation] = field(default_factory=list)
    definitions: list[DefinitionalSchema] = field(default_factory=list)
    provenance: list[ConstructionRecord] = field(default_factory=list)

    # Knowledge stores
    facts: FactStore = field(default_factory=FactStore)
    regimes: RegimeStore = field(default_factory=RegimeStore)

    # Specialized APIs
    facets: dict[str, Any] = field(default_factory=dict)

    # Construction history (Workspace maintains this)
    construction_events: list[Any] = field(default_factory=list)

    # Equality tracking
    equal_to: set[int] = field(default_factory=set)
    equivalent_to: set[int] = field(default_factory=set)

    # Lifecycle
    status: str = "active"


    def __post_init__(self):
        """
        Called after datalass initialization.
        Extract kind and canonical_key from the underlying object.
        
        """
        self.kind = self.obj.object_kind
        self.canonical_key = self.obj.canonical_key()

    def absorb_initial_metadata(self, metadata: InitialMetadata) -> None:
        """
        Copy instantiation metadata into the ledger record.

        """
        self.presentations.extend(metadata.presentations)
        self.definitions.extend(metadata.definitions)
        self.provenance.extend(metadata.provenance)

        for fact in metadata.facts:
            self.facts.add(fact)
        for regime in metadata.regimes:
            self.regimes.add(regime)

    def add_name(self, name: str) -> None:
        """
        Add a primary name.

        """
        self.names.add(name)

    def add_alias(self, alias: str) -> None:
        """
        Add an alias.

        """
        self.aliases.add(alias)

    def add_fact(self, fact: Fact) -> None:
        """
        Certify a fact about this object.

        """
        self.facts.add(fact)

    def add_regime(self, regime: RegimeCertificate) -> None:
        """
        Certify a regime.

        """
        self.regimes.add(regime)

    def add_facet(self, name: str, facet: Any) -> None:
        """
        Attach a facet (specialized API).

        """
        self.facets[name] = facet

    def absorb_record(self, other: "ObjectRecord") -> None:
        """
        Merge another record into this one.
        Used only under merge policy or explicit user request.

        """
        self.names.update(other.names)
        self.aliases.update(other.aliases)
        self.presentations.extend(other.presentations)
        self.definitions.extend(other.definitions)
        self.provenance.extend(other.provenance)
        # TODO: merge facts and regimes
        self.equal_to.update(other.equal_to)
        self.equivalent_to.update(other.equivalent_to)

    def display(self) -> str:
        """
        Basic record display.

        """
        names_str = ", ".join(self.names) if self.names else "(unnamed)"
        payload_str = self.obj.display_payload()
        return f"{names_str}: {payload_str}"
