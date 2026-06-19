from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Generic, TypeVar


SymT = TypeVar("SymT", bound="Symbol")


# ======================================================================
# Symbol identity
# ======================================================================

@dataclass(frozen=True, slots=True)
class SymbolKey:
    """
    Local key for a symbol inside one generated family.

    This is not the glyph. It is the cache/request key.
    Example: SymbolKey("0")
    """

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str):
            raise TypeError("SymbolKey.value must be a string")
        if not self.value:
            raise ValueError("SymbolKey.value may not be empty")

    @classmethod
    def from_index(cls, index: int) -> "SymbolKey":
        """
        Build the standard key for the nth generated symbol.
        """
        if type(index) is not int:
            raise TypeError("index must be an integer")
        if index < 0:
            raise ValueError("index must be nonnegative")
        return cls(str(index))


@dataclass(frozen=True, slots=True)
class SymbolId:
    """
    Canonical internal identity of a symbol.

    This is the part that should matter for symbol equality.
    The glyph can change later as presentation/aliasing policy develops.
    """

    family_id: str
    key: SymbolKey

    def __post_init__(self) -> None:
        if not isinstance(self.family_id, str):
            raise TypeError("family_id must be a string")
        if not self.family_id:
            raise ValueError("family_id may not be empty")
        if not isinstance(self.key, SymbolKey):
            raise TypeError("key must be a SymbolKey")


# ======================================================================
# Symbols
# ======================================================================

@dataclass(frozen=True, slots=True)
class Symbol:
    """
    Formal-language symbol.

    Equality is based on symbol_id, not glyph. The glyph is the current
    internal spelling/rendering of the symbol.
    """

    symbol_id: SymbolId
    glyph: str = field(compare=False)

    def __post_init__(self) -> None:
        if not isinstance(self.symbol_id, SymbolId):
            raise TypeError("symbol_id must be a SymbolId")
        if not isinstance(self.glyph, str):
            raise TypeError("glyph must be a string")
        if not self.glyph:
            raise ValueError("glyph may not be empty")

    @classmethod
    def named(cls: type[SymT], *, family_id: str, name: str) -> SymT:
        """
        Convenience constructor for explicitly named finite symbols.

        Example:
            add = FunctionSymbol.named(
                family_id="arith.functions",
                name="add",
            )
        """
        key = SymbolKey(name)
        symbol_id = SymbolId(family_id=family_id, key=key)
        return cls(symbol_id=symbol_id, glyph=name)

    def __str__(self) -> str:
        return self.glyph


@dataclass(frozen=True, slots=True)
class LogicalSymbol(Symbol):
    pass


@dataclass(frozen=True, slots=True)
class RelationSymbol(Symbol):
    pass


@dataclass(frozen=True, slots=True)
class FunctionSymbol(Symbol):
    pass


# ======================================================================
# Symbol family specs
# ======================================================================

@dataclass(frozen=True, slots=True)
class SymbolFamilySpec(Generic[SymT]):
    """
    Immutable recipe for a generated symbol family.

    The spec decides:
      - which symbol subclass is produced;
      - what family identity generated symbols belong to;
      - how a SymbolKey becomes a glyph.

    It does not store generated symbols. Caching belongs to
    GeneratedSymbolFamily.
    """

    family_id: str
    symbol_type: type[SymT]
    prefix: str

    def __post_init__(self) -> None:
        if not isinstance(self.family_id, str):
            raise TypeError("family_id must be a string")
        if not self.family_id:
            raise ValueError("family_id may not be empty")

        if not isinstance(self.symbol_type, type):
            raise TypeError("symbol_type must be a class")
        if not issubclass(self.symbol_type, Symbol):
            raise TypeError("symbol_type must be Symbol or a Symbol subclass")

        if not isinstance(self.prefix, str):
            raise TypeError("prefix must be a string")
        # Empty prefix is allowed. SymbolKey("0") would render as "0".

    def coerce_key(self, key: SymbolKey | str | int) -> SymbolKey:
        """
        Accept a few convenient key forms and normalize them to SymbolKey.
        """
        if isinstance(key, SymbolKey):
            return key

        if isinstance(key, str):
            return SymbolKey(key)

        if type(key) is int:
            return SymbolKey.from_index(key)

        raise TypeError("key must be a SymbolKey, string, or integer")

    def key_from_index(self, index: int) -> SymbolKey:
        """
        Convert a generation index into this family's standard key.
        """
        return SymbolKey.from_index(index)

    def symbol_id_for(self, key: SymbolKey | str | int) -> SymbolId:
        """
        Build the canonical internal SymbolId for a key in this family.
        """
        key = self.coerce_key(key)
        return SymbolId(family_id=self.family_id, key=key)

    def glyph_for(self, key: SymbolKey | str | int) -> str:
        """
        Build the current glyph for a key in this family.

        The glyph is presentation-ish. The SymbolId is the canonical identity.
        """
        key = self.coerce_key(key)
        return f"{self.prefix}{key.value}"

    def make_symbol(self, key: SymbolKey | str | int) -> SymT:
        """
        Build a new symbol object for this key.

        This does not cache. GeneratedSymbolFamily handles caching.
        """
        key = self.coerce_key(key)
        symbol_id = self.symbol_id_for(key)
        glyph = self.glyph_for(key)
        return self.symbol_type(symbol_id=symbol_id, glyph=glyph)


# ======================================================================
# Generated symbol families
# ======================================================================

@dataclass(slots=True)
class GeneratedSymbolFamily(Generic[SymT]):
    """
    Stateful generated stock for one symbol family.

    The spec is the immutable recipe.
    This object only handles:
      - memoization;
      - fresh generation;
      - returning the same object for the same key.
    """

    spec: SymbolFamilySpec[SymT]

    _next_index: int = 0
    _cache: dict[SymbolKey, SymT] = field(default_factory=dict)

    def get(self, key: SymbolKey | str | int) -> SymT:
        """
        Return the symbol for key, creating and caching it if needed.

        Repeated calls with the same key return the same object.
        """
        key = self.spec.coerce_key(key)

        if key not in self._cache:
            self._cache[key] = self.spec.make_symbol(key)

        return self._cache[key]

    def fresh(self) -> SymT:
        """
        Generate a fresh symbol not already materialized by this family.
        """
        while True:
            key = self.spec.key_from_index(self._next_index)
            self._next_index += 1

            if key not in self._cache:
                return self.get(key)

    def generated_symbols(self) -> tuple[SymT, ...]:
        """
        Return the symbols already materialized by this family.

        This is not the whole infinite family.
        """
        return tuple(self._cache.values())

    def generated_keys(self) -> tuple[SymbolKey, ...]:
        """
        Return the keys already materialized by this family.
        """
        return tuple(self._cache.keys())

# ======================================================================
# Sorts
# ======================================================================

@dataclass(frozen=True, slots=True)
class Sort:
    name: str

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("name may not be empty")
        if not isinstance(self.name, str):
            raise ValueError("name must be a string")


# ======================================================================
# Profile words
# ======================================================================

@dataclass(frozen=True, slots=True)
class ProfileWord:
    """
    Finite input profile / arity word.

    Mathematically: w = (s_1, ..., s_n), a finite list of sorts.
    """

    sorts: tuple[Sort, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.sorts, tuple):
            raise TypeError("ProfileWord.sorts must be a tuple")

        if not all(isinstance(sort, Sort) for sort in self.sorts):
            raise TypeError("ProfileWord.sorts must contain only Sort instances")

    @classmethod
    def empty(cls) -> "ProfileWord":
        """
        The empty input profile ().
        """
        return cls(())

    @classmethod
    def from_sorts(cls, *sorts: Sort) -> "ProfileWord":
        """
        Convenience constructor.

        Example:
            ProfileWord.from_sorts(Number, Number)
        """
        return cls(tuple(sorts))

    @property
    def arity(self) -> int:
        """
        Number of input places.
        """
        return len(self.sorts)

    def __iter__(self):
        return iter(self.sorts)

    def __len__(self) -> int:
        return len(self.sorts)


# ======================================================================
# Profiles
# ======================================================================
# ======================================================================
# Operation profiles
# ======================================================================

@dataclass(frozen=True, slots=True)
class OperationProfile:
    """
    Profile of an operation symbol.

    Mathematically: f : w -> s.
    """

    input_profile: ProfileWord
    output_sort: Sort

    def __post_init__(self) -> None:
        if not isinstance(self.input_profile, ProfileWord):
            raise TypeError("input_profile must be a ProfileWord")

        if not isinstance(self.output_sort, Sort):
            raise TypeError("output_sort must be a Sort")

    @classmethod
    def nullary(cls, output_sort: Sort) -> "OperationProfile":
        """
        Profile of a constant symbol: () -> s.
        """
        return cls(
            input_profile=ProfileWord.empty(),
            output_sort=output_sort,
        )

    @property
    def input_sorts(self) -> tuple[Sort, ...]:
        """
        Tuple of input sorts.
        """
        return self.input_profile.sorts

    @property
    def arity(self) -> int:
        """
        Number of input places.
        """
        return self.input_profile.arity

    @property
    def is_nullary(self) -> bool:
        """
        Whether this profile represents a constant symbol.
        """
        return self.arity == 0


# ======================================================================
# Many-sorted carrier families and maps
# ======================================================================

@dataclass(frozen=True, slots=True)
class FunctionProfile:

    input_sorts: tuple[Sort, ...]
    output_sort: Sort
    
    t_sort: Sort

    def __post_init__(self) -> None:
        if not isinstance(self.input_sorts, tuple):
            raise TypeError("input_sorts must be a tuple")
        if not all(isinstance(s, Sort) for s in self.input_sorts):
            raise TypeError("input_sorts must all be Sorts")
        if not isinstance(self.output_sort, Sort):
            raise TypeError("output_sorts must be a Sort")

    @property
    def arity(self) -> int:
        """
        Return the number of input places.
        
        """
        return len(self.input_sorts)


@dataclass(frozen=True, slots=True)
class RelationProfile:
    """
    The input profile of a relation symbol.

    """
    input_sorts: tuple[Sort, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.input_sorts, tuple):
            raise TypeError("input_sorts must be a tuple")
        if not all(isinstance(s, Sort) for s in self.input_sorts):
            raise TypeError("input_sorts must all be Sorts")

    @property
    def arity(self) -> int:
        """
        Return the number of input places.

        """
        return len(self.input_sorts)

function_spec = SymbolFamilySpec(
    family_id="generated.functions",
    symbol_type=FunctionSymbol,
    prefix="f",
)

function_family = GeneratedSymbolFamily(function_spec)

f0 = function_family.fresh()
f1 = function_family.fresh()
f0_again = function_family.get(0)

print(f0)                 # f0
print(f1)                 # f1
print(f0 == f0_again)     # True
print(f0 is f0_again)     # True



