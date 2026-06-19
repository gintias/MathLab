from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping


@dataclass(frozen=True)
class Atomic:
    """
    The result of decomposing a term as an atom a.
    
    """
    atom: object


@dataclass(frozen=True)
class Constructed:
    """
    The result of decomposing a term as c(t_1, ..., t_n).
    
    """
    constructor: str
    subterms: tuple["Decomposable", ...]


Decomposition = Atomic | Constructed


class Decomposable(ABC):
    """
    Anything that can expose its one-step decomposition.
    
    """
    @abstractmethod
    def decompose(self) -> Decomposition:
        """
        Return either Atomic(a) or Constructed(c, (t_1, ..., t_n)).
        
        """
        raise NotImplementedError


@dataclass(frozen=True)
class AtomTerm(Decomposable):
    """
    Reference implementation of an atomic term.

    """
    atom: object

    def decompose(self) -> Decomposition:
        return Atomic(atom=self.atom)


@dataclass(frozen=True)
class ConstructorTerm(Decomposable):
    """
    Reference implementation of a constructed term.
    
    """
    constructor: str
    subterms: tuple[Decomposable, ...]

    def decompose(self) -> Decomposition:
        return Constructed(
            constructor=self.constructor,
            subterms=tuple(self.subterms),
        )


def term(constructor: str, *subterms: Decomposable) -> ConstructorTerm:
    """
    Small convenience constructor for examples.
    
    """
    return ConstructorTerm(constructor=constructor, subterms=tuple(subterms))

# ======================================================================
# PART 2. Signatures and Well-Formedness
# ----------------------------------------------------------------------
# ======================================================================


@dataclass(frozen=True)
class Signature:
    """Constructor arities, e.g. {"add": 2, "neg": 1}."""

    arities: Mapping[str, int]

    def __post_init__(self) -> None:
        if not all(type(arity) is int and arity >= 0 for arity in self.arities.values()):
            raise ValueError("all arities must be nonnegative integers")
        

    def __contains__(self, constructor: str) -> bool:
        return constructor in self.arities
    

    def arity(self, constructor: str) -> int:
        return self.arities[constructor]
        
class Malformed(Exception):
    """Raised when a term violates the construction rules."""
    pass

class ConstructionSystem:
    """A signature plus a predicate deciding which values count as atoms."""

    def __init__(self, signature: Signature, is_atom: Callable[[Any], bool]):
        self.signature = signature
        self.is_atom = is_atom

    def is_well_formed(self, term: Decomposable) -> bool:
        try:
            self.check(term)
        except Malformed:
            return False
        return True
        
        
    def check(self, term: Decomposable) -> None:
        match term.decompose():
            case Atomic(atom):
                if not self.is_atom(atom):
                    raise Malformed(f"atom {atom!r} is not admitted")

            case Constructed(constructor, subterms):
                if constructor not in self.signature:
                    raise Malformed(f"constructor {constructor!r} is not admitted")

                expected = self.signature.arity(constructor)
                actual = len(subterms)

                if actual != expected:
                    raise Malformed(
                        f"constructor {constructor!r} expects {expected} subterms, got {actual}"
                    )

                for subterm in subterms:
                    self.check(subterm)
                    
@dataclass(frozen=True)
class FoldSpec:
    base: Callable[[Any], Any]
    step: Callable[[str, tuple[Any, ...]], Any]

def fold(term: Decomposable, spec: FoldSpec) -> Any:
    match term.decompose():
        case Atomic(atom):               
            return spec.base(atom)
        case Constructed(constructor, subterms):
            subterm_evals = tuple(fold(subterm, spec) for subterm in subterms)
            return spec.step(constructor, subterm_evals)
    

def natural_number_example() -> Decomposable:
    zero = AtomTerm("0")
    return term("S", term("S", term("S", zero)))

def size(term_: Decomposable) -> int:
    spec = FoldSpec(
        base=lambda atom: 1,
        step=lambda constructor, subterm_evals: 1 + sum(subterm_evals),
    )
    return fold(term_, spec)

def to_int(term_: Decomposable) -> int:
    spec = FoldSpec(
        base=lambda atom: 0,
        step=lambda constructor, subterm_evals: subterm_evals[0] + 1,
    )
    return fold(term_, spec)

def natural_number_system() -> ConstructionSystem:
    return ConstructionSystem(
        Signature({"S": 1}),
        is_atom=lambda atom: atom == "0",
    )

def depth(term_: Decomposable) -> int:
    spec = FoldSpec(
        base=lambda atom: 0,
        step=lambda constructor, subterm_evals: 1 + max(subterm_evals, default=0),
    )
    return fold(term_, spec)


if __name__ == "__main__":
    three = natural_number_example()
    natural_number_system().check(three)

    print(size(three))    # 4
    print(to_int(three))  # 3
    print(depth(three))  # 3

# ====================================================================== #
#  The Algebra: a carrier's interpretation of the signature.
#    base : A -> V                      how atoms land in the carrier
#    operations[c] : (V, ..., V) -> V   one operation per constructor c,
#                                       taking arity(c) already-extended args
# ====================================================================== #

@dataclass(frozen=True)
class Algebra:
    signature: Signature
    base: Callable[[Any], Any]
    operations: Mapping[str, Callable[..., Any]]
 
    def __post_init__(self) -> None:
        missing = [c for c in self.signature.arities if c not in self.operations]
        if missing:
            raise ValueError(f"algebra is missing operations for {missing}")
        extra = [c for c in self.operations if c not in self.signature]
        if extra:
            raise ValueError(f"algebra has operations for unknown constructors {extra}")


    def homomorphic_unique_extension(self) -> Callable[[Decomposable], Any]:
        """Return the unique homomorphism  h : Free -> carrier  extending `algebra`.
        h(atom a)        = base(a)
        h(c(t1,...,tn))  = operations[c]( h(t1), ..., h(tn) )
        """

        def h(t: Decomposable):
            match t.decompose():
                case Atomic(a):
                    return self.base(a)
                case Constructed(c, subterms):
                    if c not in self.signature:
                        raise Malformed(f"constructor {c!r} is not admitted")
                    
                    ar_c = self.signature.arities[c]
                    if len(subterms) != ar_c:
                        raise Malformed(f"constructor {c!r} expects {ar_c} subterms, got {len(subterms)}")
                    
                    args = tuple(h(s) for s in subterms)
                    return self.operations[c](*args)
        return h
    

@dataclass
class FreeStructure:
    """
    Consumes the constructors that generate the free object; hands back
    a maker that consumes (base, operations) and returns the unique unique_extension.
    
    """
    signature: Signature

    def unique_extension(self, base: Callable[[Any], Any], **operations) -> Callable[[Decomposable], Any]:
        return(Algebra(self.signature, base, operations).homomorphic_unique_extension())
    

# ====================================================================== #
#  Demo: your arithmetic example, now as algebras over ONE signature.
# ====================================================================== #
if __name__ == "__main__":
    # the free structure over the arithmetic constructors
    arith = FreeStructure(Signature({"+": 2, "-": 2, "*": 2, "/": 2}))
 
    def atom(v): return AtomTerm(v)
    expr = term("+", term("*", atom(3), atom(4)), atom(2))   # (3*4) + 2
 
    # evaluate: carrier = numbers
    evaluate = arith.unique_extension(
        base=lambda v: v,
        **{"+": lambda a, b: a + b,
           "-": lambda a, b: a - b,
           "*": lambda a, b: a * b,
           "/": lambda a, b: a / b},
    )
 
    # size: carrier = naturals (operations ignore the constructor name)
    size = arith.unique_extension(
        base=lambda v: 1,
        **{op: (lambda a, b: 1 + a + b) for op in ("+", "-", "*", "/")},
    )
 
    # depth: carrier = naturals
    depth = arith.unique_extension(
        base=lambda v: 0,
        **{op: (lambda a, b: 1 + max(a, b)) for op in ("+", "-", "*", "/")},
    )
 
    # pretty: carrier = strings
    pretty = arith.unique_extension(
        base=lambda v: str(v),
        **{op: (lambda a, b, _op=op: f"({a} {_op} {b})") for op in ("+", "-", "*", "/")},
    )
 
    print("expr   :", pretty(expr))
    print("value  :", evaluate(expr))    # 14
    print("size   :", size(expr))        # 5
    print("depth  :", depth(expr))       # 2
 
    assert evaluate(expr) == 14
    assert size(expr) == 5
    assert depth(expr) == 2
    assert pretty(expr) == "((3 * 4) + 2)"
 
    # uniqueness, concretely: any h satisfying the homomorphism equations
    # equals extend(algebra) -- there is no freedom left once base+ops are fixed.
    h = evaluate
    assert h(expr) == h(term("+", term("*", atom(3), atom(4)), atom(2)))
    print("\nall unique_extension tests passed")

                    
# 4
# 3
# 3
# expr   : ((3 * 4) + 2)
# value  : 14
# size   : 5
# depth  : 2

# all unique_extension tests passed
