"""
induction_and_recursion.py
==========================

This file is intentionally a template.

The goal is to rebuild the recursion/induction machinery by hand instead of
copying in a finished abstraction. Keep this file small while working through
it. When a section feels too abstract, write one concrete example before adding
more machinery.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping


@dataclass(frozen=True)
class AtomCase:
    """
    The result of decomposing an atomic term.
    
    """
    value: object


@dataclass(frozen=True)
class NodeCase:
    """
    he result of decomposing a constructed term.
    
    """
    tag: str
    children: tuple["Decomposable", ...]


Case = AtomCase | NodeCase


class Decomposable(ABC):
    """
    Anything that can expose itself as either an AtomCase or NodeCase.
    
    """
    @abstractmethod
    def decompose(self) -> Case:
        """
        Return the one-step shape of this object.
        
        """
        raise NotImplementedError


@dataclass(frozen=True)
class Atom(Decomposable):
    """
    Reference leaf implementation.

    """
    value: object

    def decompose(self) -> Case:
        return AtomCase(value=self.value)


@dataclass(frozen=True)
class Node(Decomposable):
    """
    Reference constructor-node implementation.
    
    """
    tag: str
    children: tuple[Decomposable, ...]

    def decompose(self) -> Case:
        return NodeCase(tag=self.tag, children=tuple(self.children))


def node(tag: str, *children: Decomposable) -> Node:
    """
    Small convenience constructor for examples.
    
    """
    return Node(tag=tag, children=tuple(children))

# ======================================================================
# PART 2. Signatures and Well-Formedness
# ----------------------------------------------------------------------
# A signature says which constructor tags exist and how many children each
# constructor takes.
#
# This is the "no junk" check:
#   - atoms must be accepted by is_atom
#   - node tags must exist in the signature
#   - node arities must match
#   - children must themselves be well-formed
# ======================================================================


@dataclass(frozen=True)
class Signature:
    """Constructor arities, e.g. {"add": 2, "neg": 1}."""

    arities: Mapping[str, int]

    def __post_init__(self) -> None:
        # TODO: validate that every arity is a nonnegative int.
        pass

    def __contains__(self, tag: str) -> bool:
        # TODO: return whether tag is a known constructor.
        raise NotImplementedError

    def arity(self, tag: str) -> int:
        # TODO: return the arity for tag.
        raise NotImplementedError


class Malformed(Exception):
    """Raised when a term violates the construction rules."""

    def __init__(self, term: Decomposable, reason: str, path: tuple[int, ...]):
        self.term = term
        self.reason = reason
        self.path = path
        super().__init__(f"malformed at path {path}: {reason}")


class ConstructionSystem:
    """A signature plus a predicate deciding which values count as atoms."""

    def __init__(self, signature: Signature, is_atom: Callable[[Any], bool]):
        self.signature = signature
        self.is_atom = is_atom

    def is_well_formed(self, term: Decomposable) -> bool:
        # TODO: implement as a boolean wrapper around check().
        raise NotImplementedError

    def check(self, term: Decomposable, path: tuple[int, ...] = ()) -> None:
        # TODO:
        #   1. decompose term
        #   2. handle AtomCase
        #   3. handle NodeCase
        #   4. recurse into children, extending path with child indexes
        raise NotImplementedError


# ======================================================================
# PART 3. The Fold
# ----------------------------------------------------------------------
# A fold is the basic structural recursion scheme.
#
# To define a recursive computation, provide:
#   base(atom_value) -> result
#   step(tag, child_results) -> result
#
# Then fold recursively computes child results before applying step.
# ======================================================================


@dataclass(frozen=True)
class FoldSpec:
    """A recursion specification."""

    base: Callable[[Any], Any]
    step: Callable[[str, tuple[Any, ...]], Any]


def fold(term: Decomposable, spec: FoldSpec) -> Any:
    # TODO:
    #   AtomCase(value) -> spec.base(value)
    #   NodeCase(tag, children) ->
    #       child_results = tuple(fold(child, spec) for child in children)
    #       spec.step(tag, child_results)
    raise NotImplementedError


# ======================================================================
# PART 4. First Examples
# ----------------------------------------------------------------------
# Use these after PART 3 works. The point is to learn the fold by writing
# small, visible computations over the same tree.
# ======================================================================


def natural_number_example() -> Decomposable:
    """Build S(S(S(0))) as a tree."""

    # TODO:
    #   zero = Atom("0")
    #   three = node("S", node("S", node("S", zero)))
    #   return three
    raise NotImplementedError


def to_int(term: Decomposable) -> int:
    """Interpret a natural-number tree as a Python int."""

    # TODO: use fold with:
    #   base("0") -> 0
    #   step("S", (n,)) -> n + 1
    raise NotImplementedError


def size(term: Decomposable) -> int:
    """Count atoms and constructor nodes."""

    # TODO: use fold.
    raise NotImplementedError


def depth(term: Decomposable) -> int:
    """Compute maximum constructor nesting depth."""

    # TODO: use fold.
    raise NotImplementedError


# ======================================================================
# PART 5. Target-Enrichment Schemes
# ----------------------------------------------------------------------
# These are later. They are here as signposts, not as a demand to implement
# them now.
#
# The core idea:
#   "advanced recursion" is often just ordinary fold into a richer target.
# ======================================================================


def simultaneous(
    bases: tuple[Callable[[Any], Any], ...],
    steps: tuple[Callable[[str, tuple[Any, ...]], Any], ...],
) -> FoldSpec:
    """Fold into a product target, computing several summaries at once."""

    # TODO later:
    #   base(v) returns a tuple of all base results.
    #   step(tag, child_values) returns a tuple of all step results.
    raise NotImplementedError


def project(index: int) -> Callable[[tuple[Any, ...]], Any]:
    """Project one component out of a simultaneous result."""

    # TODO: return a small lambda.
    raise NotImplementedError


def parameterized(
    base_p: Callable[[Any], Callable[[Any], Any]],
    step_p: Callable[[str, tuple[Any, ...]], Callable[[Any], Any]],
) -> FoldSpec:
    """Fold into a function target, useful for environments/parameters."""

    # TODO later: this may be just FoldSpec(base_p, step_p).
    raise NotImplementedError


def run_param(term: Decomposable, spec: FoldSpec, parameter: Any) -> Any:
    """Run a parameterized fold by applying the folded function."""

    # TODO: fold(term, spec)(parameter)
    raise NotImplementedError


def tracking(
    base: Callable[[Any], Any],
    step: Callable[[str, tuple[tuple[Decomposable, Any], ...]], Any],
) -> Callable[[Decomposable], Any]:
    """Fold while carrying the source subtree beside each computed value."""

    # TODO later:
    #   Target should be (rebuilt_subtree, computed_value).
    #   The final rebuilt_subtree should equal the original term.
    raise NotImplementedError


class InvariantViolation(Exception):
    """Raised when a checked invariant fails at some subtree."""

    def __init__(self, node: Decomposable, value: Any):
        self.node = node
        self.value = value
        super().__init__(f"invariant failed at {node!r} with value {value!r}")


def with_invariant(
    spec: FoldSpec,
    invariant: Callable[[Decomposable, Any], bool],
) -> Callable[[Decomposable], Any]:
    """Run a fold while checking an invariant at every subtree."""

    # TODO later:
    #   This needs tracking, because the invariant wants both node and value.
    raise NotImplementedError


# ======================================================================
# PART 6. Well-Founded Recursion
# ----------------------------------------------------------------------
# Structural recursion only looks at immediate children.
#
# Well-founded recursion is broader: a value may depend on any smaller
# predecessor, as long as there is no infinite descent.
# ======================================================================


def well_founded(
    predecessors: Callable[[Any], Iterable[Any]],
    rule: Callable[[Any, Callable[[Any], Any]], Any],
) -> Callable[[Any], Any]:
    """Build a memoized well-founded recursive function."""

    # TODO later:
    #   Keep a memo dict.
    #   Compute all predecessors before the current value.
    #   Pass a recall function into rule.
    raise NotImplementedError


def immediate_subterms(term: Decomposable) -> tuple[Decomposable, ...]:
    """Return direct children of a term."""

    # TODO:
    #   AtomCase -> ()
    #   NodeCase -> children
    raise NotImplementedError


def course_of_values(
    rule: Callable[[Decomposable, Callable[[Decomposable], Any]], Any],
) -> Callable[[Decomposable], Any]:
    """Well-founded recursion over the subterm relation."""

    # TODO later: specialize well_founded(immediate_subterms, rule).
    raise NotImplementedError


# ======================================================================
# PART 7. Many-Sorted Systems
# ----------------------------------------------------------------------
# A many-sorted signature says not just arity, but input/output sorts.
#
# Example:
#   "add" : Expr x Expr -> Expr
#   "eq"  : Expr x Expr -> Formula
#
# Keep this later unless a concrete formula/term example forces it.
# ======================================================================


@dataclass(frozen=True)
class ManySortedSignature:
    """tag -> (result_sort, (arg_sort, ...))."""

    rules: Mapping[str, tuple[str, tuple[str, ...]]]

    def __contains__(self, tag: str) -> bool:
        # TODO: return whether tag is known.
        raise NotImplementedError

    def result_sort(self, tag: str) -> str:
        # TODO: return the result sort.
        raise NotImplementedError

    def arg_sorts(self, tag: str) -> tuple[str, ...]:
        # TODO: return the argument sorts.
        raise NotImplementedError


class SortError(Exception):
    pass


class ManySortedSystem:
    """Sort checker for decomposable syntax trees."""

    def __init__(
        self,
        signature: ManySortedSignature,
        atom_sort: Callable[[Any], str | None],
    ):
        self.signature = signature
        self.atom_sort = atom_sort

    def sort_of(self, term: Decomposable) -> str:
        # TODO:
        #   AtomCase -> ask atom_sort
        #   NodeCase -> check tag, recurse on children, compare sorts
        raise NotImplementedError

    def is_well_formed(self, term: Decomposable) -> bool:
        # TODO: boolean wrapper around sort_of().
        raise NotImplementedError


# ======================================================================
# PART 8. Pattern-Dispatched Function Specs
# ----------------------------------------------------------------------
# This section points back toward your Python-object-construction goal:
# building recursive Python functions from structured specs.
#
# Do not implement build_function until there is one concrete consumer, e.g.
# a generated size(expr), evaluate(expr), or simplify(expr).
# ======================================================================


@dataclass(frozen=True)
class FunctionSpec:
    name: str
    params: tuple[str, ...]
    cases: tuple["CaseSpec", ...]
    fallback: "FallbackSpec"


@dataclass(frozen=True)
class CaseSpec:
    pattern: "PatternSpec"
    body: "BodyExpr"
    guard: "GuardSpec | None" = None


@dataclass(frozen=True)
class FallbackSpec:
    message: str


class PatternSpec:
    """Base class for pattern templates."""


@dataclass(frozen=True)
class ClassPattern(PatternSpec):
    cls_name: str
    args: tuple[PatternSpec, ...]


@dataclass(frozen=True)
class LiteralPattern(PatternSpec):
    value: Any


@dataclass(frozen=True)
class CapturePattern(PatternSpec):
    name: str


@dataclass(frozen=True)
class WildcardPattern(PatternSpec):
    pass


class BodyExpr:
    """Base class for return-expression templates."""


@dataclass(frozen=True)
class CaptureExpr(BodyExpr):
    name: str


@dataclass(frozen=True)
class ConstantExpr(BodyExpr):
    value: Any


@dataclass(frozen=True)
class RecursiveCallExpr(BodyExpr):
    arg: BodyExpr


@dataclass(frozen=True)
class CallExpr(BodyExpr):
    function_name: str
    args: tuple[BodyExpr, ...]


@dataclass(frozen=True)
class OperatorExpr(BodyExpr):
    operator: str
    left: BodyExpr
    right: BodyExpr


@dataclass(frozen=True)
class ConstructExpr(BodyExpr):
    cls_name: str
    args: tuple[BodyExpr, ...]


class GuardSpec:
    """Placeholder for an optional condition over pattern captures."""


def build_function(
    spec: FunctionSpec,
    namespace: dict[str, Any] | None = None,
) -> Callable[..., Any]:
    """Turn a FunctionSpec into a real Python callable."""

    # TODO much later:
    #   First decide whether this should generate source code, build closures,
    #   or interpret the spec directly. Do not choose before there is a consumer.
    raise NotImplementedError
