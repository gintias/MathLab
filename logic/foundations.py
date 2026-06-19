from dataclasses import dataclass
from typing import Iterable

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


@dataclass(frozen=True, slots=True)
class SortSet:
    sorts: frozenset[sort]

    def __init__(self, sorts: Iterable[Sort | str]) -> None:
        normalized = frozenset(s if isinstance(s, Sort) else Sort(s) for s in sorts)
        
        if not normalized:
            raise ValueError("SortSet must be nonempty")

        self.__setattr__(self, )
        

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