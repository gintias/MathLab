from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Mapping

@dataclass(frozen=True)
class Symbol(ABC):
    text: str
    sort: str
    arity: int | None = None

class SymbolFamily(ABC):
    sort: str
    infinite: bool
    cache: dict[Any, Symbol]

    def __init__(self, sort: str, infinite: bool):
        self.sort = sort
        self.infinite = infinite
        self.cache = {}

    @abstractmethod
    def build_symbol(self, key: Any) -> Symbol:
        pass

    def get(self, key: Any) -> Symbol:
        if key in self.cache:
            return self.cache[key]
        if not self.infinite and not self.allowed_key(key):
            raise ValueError(...)
        symbol = self.build_symbol(key)
        self.cache[key] = symbol
        return symbol

    @abstractmethod
    def allowed_key(self, key: Any) -> bool:
        pass

class InfiniteSymbolFamily(SymbolFamily):
    def __init__(self, sort: str, label: Callable[[Any], str]):
        super().__init__(sort, infinite=True)
        self.label = label

    def build_symbol(self, key: Any) -> Symbol:
        text = self.label(key)
        return Symbol(text=text, sort=self.sort)

    def allowed_key(self, key: Any) -> bool:
        return isinstance(key, int)

class ExplicitSymbolFamily(SymbolFamily):
    def __init__(self, sort: str, mapping: Mapping[Any, str], arities: Mapping[Any, int] = None):
        super().__init__(sort, infinite=False)
        self.mapping = mapping
        self.arities = arities or {}

    def build_symbol(self, key: Any) -> Symbol:
        text = self.mapping[key]
        return Symbol(text=text, sort=self.sort, arity=self.arities.get(key))

    def allowed_key(self, key: Any) -> bool:
        return key in self.mapping

class RegistryWrap:
    def __init__(self, family: SymbolFamily):
        self.family = family

    def get(self, key: Any) -> Symbol:
        return self.family.get(key)

    def register(self, symbol: Symbol) -> Symbol:
        if symbol.sort != self.family.sort:
            raise ValueError(...)
        if self.family.contains(symbol):
            return symbol
        self.family.cache[self.family.key_of(symbol)] = symbol
        return symbol

class Language:
    def __init__(self, families: Mapping[str, SymbolFamily], logical_symbols: list[Symbol] = None):
        self.registries = {name: RegistryWrap(fam) for name, fam in families.items()}
        self.logical_symbols = {sym.text: sym for sym in (logical_symbols or [])}

    def get(self, sort: str, key: Any) -> Symbol:
        return self.registries[sort].get(key)

    def variable(self, index: int) -> Symbol:
        return self.get("variable", index)