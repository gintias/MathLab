from __future__ import annotations

from core.math_object import MathObject, ObjectDraft
from core.metadata import ConstructionRecord, Fact, InitialMetadata, Presentation
from core.workspace import Workspace


class ToyObject(MathObject):
    """
    Minimal concrete MathObject for exercising Workspace behavior.
    """

    object_kind = "ToyObject"

    def __init__(self, value: str):
        self.value = value
        self.validate()

    def validate(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("ToyObject.value must be a string")

    def canonical_key(self) -> tuple:
        return (self.object_kind, self.value)

    def display_payload(self) -> str:
        return self.value

    def default_metadata(self) -> InitialMetadata:
        return InitialMetadata(
            presentations=[
                Presentation(
                    kind="literal",
                    data={"value": self.value},
                    description="Created directly from a string.",
                )
            ]
        )


def make_marked_object(value: str) -> ObjectDraft[ToyObject]:
    """
    Tiny factory that shows the ObjectDraft path through Workspace.introduce().
    """
    obj = ToyObject(value)
    metadata = InitialMetadata(
        presentations=[
            Presentation(
                kind="factory",
                data={"value": value},
                description="Created through make_marked_object.",
            )
        ],
        provenance=[
            ConstructionRecord(
                name="make_marked_object",
                inputs={"value": value},
                output_kind=ToyObject.object_kind,
            )
        ],
        facts=[
            Fact(
                claim="marked",
                value=True,
                reason="factory attaches this fact",
            )
        ],
    )
    return ObjectDraft(obj=obj, metadata=metadata)


def main() -> None:
    workspace = Workspace(equality_policy="link")

    alpha = workspace.introduce(ToyObject("alpha"), name="alpha")
    alpha_again = workspace.introduce(ToyObject("alpha"), name="alpha_again")
    beta = workspace.introduce(make_marked_object("beta"), name="beta")
    workspace.alias(beta, "b")

    assert alpha.display() == "alpha: alpha"
    assert alpha_again.display() == "alpha_again: alpha"
    assert beta.display() == "beta: beta"

    assert workspace.get("alpha") is alpha
    assert workspace.get("alpha_again") is alpha_again
    assert workspace.get("beta") is beta
    assert workspace.get("b") is beta

    assert workspace.knows_equal(alpha, alpha_again)
    assert not workspace.knows_equal(alpha, beta)

    assert alpha.presentations[0].kind == "literal"
    assert beta.presentations[0].kind == "factory"
    assert beta.provenance[0].name == "make_marked_object"
    assert beta.facts.has("marked")

    print("workspace smoke test passed")
    print(f"  alpha id: {alpha.record_id}")
    print(f"  alpha_again id: {alpha_again.record_id}")
    print(f"  beta id: {beta.record_id}")


if __name__ == "__main__":
    main()
