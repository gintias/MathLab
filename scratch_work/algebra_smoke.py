from __future__ import annotations

if __package__ is None or __package__ == "":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logic.induction_and_recursion import (
    Algebra,
    AtomTerm,
    Malformed,
    Signature,
    term,
)


def main() -> None:
    arith_sig = Signature({"add": 2, "mul": 2, "neg": 1})

    # (2 + 3) * -(4)
    expr = term(
        "mul",
        term("add", AtomTerm(2), AtomTerm(3)),
        term("neg", AtomTerm(4)),
    )

    eval_int = Algebra(
        signature=arith_sig,
        base=lambda atom: atom,
        operations={
            "add": lambda left, right: left + right,
            "mul": lambda left, right: left * right,
            "neg": lambda value: -value,
        },
    ).extend()

    pretty = Algebra(
        signature=arith_sig,
        base=str,
        operations={
            "add": lambda left, right: f"({left} + {right})",
            "mul": lambda left, right: f"({left} * {right})",
            "neg": lambda value: f"(-{value})",
        },
    ).extend()

    size = Algebra(
        signature=arith_sig,
        base=lambda atom: 1,
        operations={
            "add": lambda left, right: 1 + left + right,
            "mul": lambda left, right: 1 + left + right,
            "neg": lambda value: 1 + value,
        },
    ).extend()

    depth = Algebra(
        signature=arith_sig,
        base=lambda atom: 0,
        operations={
            "add": lambda left, right: 1 + max(left, right),
            "mul": lambda left, right: 1 + max(left, right),
            "neg": lambda value: 1 + value,
        },
    ).extend()

    assert eval_int(expr) == -20
    assert pretty(expr) == "((2 + 3) * (-4))"
    assert size(expr) == 6
    assert depth(expr) == 2

    bad = term("add", AtomTerm(1))
    try:
        eval_int(bad)
    except Malformed:
        pass
    else:
        raise AssertionError("bad arity should raise Malformed")

    print("algebra smoke test passed")
    print("value :", eval_int(expr))
    print("pretty:", pretty(expr))
    print("size  :", size(expr))
    print("depth :", depth(expr))


if __name__ == "__main__":
    main()
