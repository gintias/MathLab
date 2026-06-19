from __future__ import annotations

from typing import Any, Optional

from .math_object import MathObject, ObjectDraft
from .metadata import InitialMetadata
from .records import ObjectRecord
from .registry import Registry
from .construction import ConstructionGraph

class Workspace: 
    """
    Public mathematial environment.

    Owns:
        records
        names
        equaliy policy
        registry
        recognizers
        explanations
    """

    def __init__(self, *, equality_policy: str = "link"):
        """
        Initialize a workspae.

        equality_policy options:
            "fresh" – always create new records, never merge
            "link" – records are separate but known equal by key
            "merge" – merge records with same key into one
            "manual" – user decides on equality
        
        """
        self.equality_policy = equality_policy
        self._records: dict[int, ObjectRecord] = {}
        self._name_to_id: dict[str, int] = {}

        self._registry = Registry()
        self._construction_graph = ConstructionGraph()
        self._recognizers: list[Any] = []
        self._next_id = 0

    # ============================================================
    # Introduction
    # ============================================================

    def introduce(
        self,
        thing: MathObject | ObjectDraft,
        *,
        name: Optional[str] = None,
        policy: Optional[str] = None,
    ) -> ObjectRecord:
        """
        Introduce a mathematical object or object draft into the workspace.
        
        """
        # Extract object and metadata
        if isinstance(thing, ObjectDraft):
            obj = thing.obj
            metadata = thing.metadata
        else:
            obj = thing
            metadata = obj.default_metadata()

        key = obj.canonical_key()
        existing_record = None
        if self._registry.has_key(key):
            existing_id = self._registry.lookup_key(key)
            existing_record = self._records[existing_id]

        # Create new record
        new_record = self._new_record(obj, metadata, name=name)

        # Apply policy
        policy_to_use = policy or self.equality_policy
        final_record = self._apply_equality_policy(
            new_record, existing_record, policy=policy_to_use
        )

        # Bind name if provided
        if name:
            self.name(final_record, name)

        return final_record

    def _new_record(
        self,
        obj: MathObject,
        metadata: InitialMetadata,
        *,
        name: Optional[str] = None,
    ) -> ObjectRecord:
        """
        Create a fresh ObjectRecord and store it.
        
        """
        record_id = self._next_id
        self._next_id += 1

        record = ObjectRecord(record_id=record_id, obj=obj)
        record.absorb_initial_metadata(metadata)

        if name:
            record.add_name(name)

        self._records[record_id] = record
        self._registry.register_record(obj.canonical_key(), record_id)

        return record

    def _apply_equality_policy(
        self,
        new_record: ObjectRecord,
        existing_record: Optional[ObjectRecord],
        *,
        policy: str,
    ) -> ObjectRecord:
        """
        Apply the workspace equality policy to records with the same key.
        
        """
        if existing_record is None:
            return new_record

        if policy == "fresh":
            return new_record

        if policy == "link":
            self._registry.union_equal(new_record.record_id, existing_record.record_id)
            new_record.equal_to.add(existing_record.record_id)
            existing_record.equal_to.add(new_record.record_id)
            return new_record

        if policy == "merge":
            existing_record.absorb_record(new_record)
            self._registry.register_record(
                existing_record.canonical_key, existing_record.record_id
            )
            del self._records[new_record.record_id]
            return existing_record

        if policy == "manual":
            return new_record

        raise ValueError(f"Unknown equality policy: {policy}")

    # ============================================================
    # Names
    # ============================================================

    def name(self, record: ObjectRecord, name: str) -> None:
        """
        Bind a primary name to a record.
        
        """
        record.add_name(name)
        self._name_to_id[name] = record.record_id

    def alias(self, record: ObjectRecord, alias: str) -> None:
        """
        Bind an alias to a record.
        
        """
        record.add_alias(alias)
        self._name_to_id[alias] = record.record_id

    def get(self, name: str) -> ObjectRecord:
        """
        Retrieve a record by name or alias.
        
        """
        record_id = self._name_to_id[name]
        return self._records[record_id]

    # ============================================================
    # Equality
    # ============================================================

    def canonical(self, record: ObjectRecord) -> ObjectRecord:
        """
        Return the canonical representative of a known-equality class.
        
        """
        canon_id = self._registry.canonical_id(record.record_id)
        return self._records[canon_id]

    def knows_equal(self, left: ObjectRecord, right: ObjectRecord) -> bool:
        """
        Check whether the workspace knows two records are equal.
        
        """
        return self._registry.known_equal(left.record_id, right.record_id)
    
    def assert_equal(
        self,
        left: ObjectRecord,
        right: ObjectRecord,
        *,
        reason: Optional[str] = None,
        certificate: Any = None,
    ) -> None:
        """
        Assert that two records are equal

        """
        self._registry.union_equal(left.record_id, right.record_id)
        left.equal_to.add(right.record_id)
        right.equal_to.add(left.record_id)

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