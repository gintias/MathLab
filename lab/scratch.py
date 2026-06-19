from __future__ import annotations

from core.math_object import MathObject, ObjectDraft
from core.metadata import ConstructionRecord, Fact, InitialMetadata, Presentation
from core.records import ObjectRecord


# ObjectDraft principle:
# A producing operation may know construction facts that the raw MathObject
# should not have to know about itself. The draft temporarily carries both:
# the object that was produced and the metadata learned while producing it.
# It does not matter whether the producer is a method, factory, constructor,
# or helper function; the important boundary is object payload vs provenance.


class TinySet(MathObject):
    """
    Minimal concrete MathObject for the scratch demo.

    The core idea: MathObject owns the mathematical payload behavior.
    Metadata lives beside it, not inside it.
    """

    object_kind = "TinySet"

    def __init__(self, elements):
        self.elements = frozenset(elements)
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.elements, frozenset):
            raise TypeError("TinySet.elements must be a frozenset")

    def canonical_key(self) -> tuple:
        return (self.object_kind, self.elements)

    def display_payload(self) -> str:
        return "{" + ", ".join(str(x) for x in sorted(self.elements)) + "}"

    def default_metadata(self) -> InitialMetadata:
        return InitialMetadata(
            presentations=[
                Presentation(
                    kind="roster",
                    data={"elements": self.elements},
                    description="Created directly from a Python iterable.",
                )
            ]
        )


def make_even_subset(universe: TinySet) -> ObjectDraft[TinySet]:
    """
    A factory can return an ObjectDraft when it knows extra construction facts.

    This is the main purpose of ObjectDraft:
    it bundles the new object together with the metadata learned while making it.
    """
    evens = TinySet(x for x in universe.elements if x % 2 == 0)

    metadata = InitialMetadata(
        presentations=[
            Presentation(
                kind="set-builder",
                data={"universe": universe.elements, "predicate": "x % 2 == 0"},
                description="Elements selected by a predicate.",
            )
        ],
        provenance=[
            ConstructionRecord(
                name="make_even_subset",
                inputs={"universe": universe.display_payload()},
                output_kind="TinySet",
                guarantees=["output is a subset of the input universe"],
            )
        ],
        facts=[
            Fact(
                claim="all_elements_even",
                value=True,
                reason="constructed by filtering with x % 2 == 0",
            )
        ],
    )

    return ObjectDraft(obj=evens, metadata=metadata)


def record_from_object(record_id: int, thing: MathObject | ObjectDraft) -> ObjectRecord:
    """
    This is the tiny version of what Workspace.introduce is trying to do.

    If it gets a plain MathObject, it asks the object for default metadata.
    If it gets an ObjectDraft, it uses the richer metadata from the factory.
    """
    if isinstance(thing, ObjectDraft):
        obj = thing.obj
        metadata = thing.metadata
    else:
        obj = thing
        metadata = thing.default_metadata()

    record = ObjectRecord(record_id=record_id, obj=obj)
    record.absorb_initial_metadata(metadata)
    return record


if __name__ == "__main__":
    universe = TinySet([1, 2, 3, 4, 5])
    plain_record = record_from_object(1, universe)

    draft = make_even_subset(universe)
    draft_record = record_from_object(2, draft)

    print("Plain object path:")
    print(" ", plain_record.display())
    print(" ", plain_record.presentations)
    print()

    print("ObjectDraft path:")
    print(" ", draft_record.display())
    print(" ", draft_record.presentations)
    print(" ", draft_record.provenance)
    print(" ", draft_record.facts.all())
