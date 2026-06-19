class FiniteSet:

    def __init__(self, elements, name=None):
        self.name = name
        self._elements = frozenset(elements)

    # ------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------

    def _require_finite_set(self, other):
        if not isinstance(other, FiniteSet):
            raise TypeError("Expected a FiniteSet.")

    # ------------------------------------------------------------
    # Basic Python protocols
    # ------------------------------------------------------------

    def __contains__(self, x):
        return x in self._elements

    def __iter__(self):
        return iter(self._elements)

    def __len__(self) -> int:
        return len(self._elements)

    def __repr__(self) -> str:
        return f"FiniteSet({{{', '.join(map(repr, self._elements))}}})"

    def __str__(self):
        if self.is_empty():
            return "∅"
        return "{" + ", ".join(str(x) for x in self._elements) + "}"

    def __eq__(self, other):
        return isinstance(other, FiniteSet) and self._elements == other._elements

    def __hash__(self):
        return hash(self._elements)

    # ------------------------------------------------------------
    # Basic set facts
    # ------------------------------------------------------------

    @property
    def elements(self):
        return self._elements

    def cardinality(self):
        return len(self._elements)

    def is_empty(self):
        return len(self._elements) == 0

    def is_singleton(self):
        return len(self._elements) == 1

    # ------------------------------------------------------------
    # Subset relations
    # ------------------------------------------------------------

    def is_subset_of(self, other):
        self._require_finite_set(other)
        return self._elements <= other._elements

    def is_proper_subset_of(self, other):
        self._require_finite_set(other)
        return self._elements < other._elements

    def is_superset_of(self, other):
        self._require_finite_set(other)
        return self._elements >= other._elements

    def is_disjoint_from(self, other):
        self._require_finite_set(other)
        return self._elements.isdisjoint(other._elements)

    # ------------------------------------------------------------
    # Set operations
    # ------------------------------------------------------------

    def union(self, other, name=None):
        self._require_finite_set(other)
        return FiniteSet(self._elements | other._elements, name=name)

    def intersection(self, other, name=None):
        self._require_finite_set(other)
        return FiniteSet(self._elements & other._elements, name=name)

    def difference(self, other, name=None):
        self._require_finite_set(other)
        return FiniteSet(self._elements - other._elements, name=name)

    def symmetric_difference(self, other, name=None):
        self._require_finite_set(other)
        return FiniteSet(self._elements ^ other._elements, name=name)

    # ------------------------------------------------------------
    # Derived finite sets
    # ------------------------------------------------------------

    def powerset(self, name=None):
        elems = list(self._elements)
        subsets = []

        for mask in range(2 ** len(elems)):
            subset = [elems[i] for i in range(len(elems)) if mask & (1 << i)]
            subsets.append(FiniteSet(subset))

        return FiniteSet(subsets, name=name)