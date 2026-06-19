from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Generic, TypeVar

from .language import OperationProfile, Sort

SymbolT = TypeVar("SymbolT")


@dataclass(frozen=True, slots=True)
class SortedFamily:
    """
    A sorted family A = (A_s)_{s ∈ S} of carriers.

    Each sort is associated with one carrier object. The carrier may be any
    Python object that represents the values of that sort.
    """

    carriers: dict[Sort, Any]

    def __post_init__(self) -> None:
        if not isinstance(self.carriers, dict):
            raise TypeError("carriers must be a dict[Sort, Any]")
        if not all(isinstance(sort, Sort) for sort in self.carriers):
            raise TypeError("carriers must have Sort keys")

    @property
    def sorts(self) -> tuple[Sort, ...]:
        return tuple(self.carriers)

    def __getitem__(self, sort: Sort) -> Any:
        return self.carriers[sort]

    def __contains__(self, sort: Sort) -> bool:
        return sort in self.carriers


@dataclass(frozen=True, slots=True)
class ProfileCorrectMap:
    """
    A profile-correct map h : A -> B.

    It is a family of component maps h_s : A_s -> B_s for each sort s.
    """

    source: SortedFamily
    target: SortedFamily
    components: dict[Sort, Callable[[Any], Any]]

    def __post_init__(self) -> None:
        if set(self.source.sorts) != set(self.target.sorts):
            raise ValueError("source and target must have the same sorts")
        if set(self.components) != set(self.source.sorts):
            raise ValueError("components must provide one map for each sort")
        if not all(callable(func) for func in self.components.values()):
            raise TypeError("components must all be callable")

    def apply(self, sort: Sort, value: Any) -> Any:
        if sort not in self.components:
            raise KeyError(f"no component for sort {sort}")
        return self.components[sort](value)

    __call__ = apply


@dataclass
class SigmaAlgebra(Generic[SymbolT]):
    """
    A Σ-algebra over a many-sorted signature.

    The signature gives an operation profile for each operation symbol, and the
    operations interpretation gives a concrete function for that symbol.
    """

    signature: dict[SymbolT, OperationProfile]
    carriers: SortedFamily
    operations: dict[SymbolT, Callable[..., Any]]

    def __post_init__(self) -> None:
        if set(self.signature) != set(self.operations):
            raise ValueError("operations must interpret every operation symbol in the signature")
        for symbol, profile in self.signature.items():
            if profile.output_sort not in self.carriers:
                raise ValueError("output sort of every operation must be present in carriers")
            for sort in profile.input_sorts:
                if sort not in self.carriers:
                    raise ValueError("input sort of every operation must be present in carriers")

    def evaluate(self, symbol: SymbolT, *args: Any) -> Any:
        if symbol not in self.operations:
            raise KeyError(f"no operation interpretation for symbol {symbol}")
        return self.operations[symbol](*args)


@dataclass(frozen=True, slots=True)
class SigmaHomomorphism(Generic[SymbolT]):
    """
    A candidate homomorphism between two Σ-algebras.

    It is profile-correct as a family of maps, and it can be tested for
    operation preservation on particular argument tuples.
    """

    source: SigmaAlgebra[SymbolT]
    target: SigmaAlgebra[SymbolT]
    underlying: ProfileCorrectMap

    def __post_init__(self) -> None:
        if set(self.source.signature) != set(self.target.signature):
            raise ValueError("source and target must have the same operation symbols")
        if set(self.source.carriers.sorts) != set(self.target.carriers.sorts):
            raise ValueError("source and target algebras must share the same sorts")
        if self.underlying.source != self.source.carriers or self.underlying.target != self.target.carriers:
            raise ValueError("underlying map must connect the carriers of the two algebras")

    def preserves(self, symbol: SymbolT, *args: Any) -> bool:
        profile = self.source.signature[symbol]
        if len(args) != profile.arity:
            raise ValueError("argument tuple length must match operation arity")

        lhs = self.underlying.apply(
            profile.output_sort,
            self.source.evaluate(symbol, *args),
        )
        rhs_args = tuple(
            self.underlying.apply(sort, value)
            for sort, value in zip(profile.input_sorts, args)
        )
        rhs = self.target.evaluate(symbol, *rhs_args)
        return lhs == rhs
