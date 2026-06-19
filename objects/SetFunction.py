try:
    from .FiniteSet import FiniteSet
    from .Relation import Relation
except ImportError:
    from FiniteSet import FiniteSet
    from Relation import Relation


class SetFunction(Relation):
    """A total function between two finite sets, represented by its graph."""

    def __init__(self, domain, codomain, pairs):
        if not isinstance(domain, FiniteSet):
            raise TypeError("domain must be a FiniteSet.")
        if not isinstance(codomain, FiniteSet):
            raise TypeError("codomain must be a FiniteSet.")

        super().__init__(pairs)

        graph_domain = super().domain()
        if len(graph_domain) != len(self):
            raise ValueError("Each domain element must have exactly one output.")
        if graph_domain != domain:
            raise ValueError("The function must be defined on exactly its domain.")
        if not self.range().is_subset_of(codomain):
            raise ValueError("Every output must belong to the codomain.")

        self._domain = domain
        self._codomain = codomain
        self._lookup = {pair[0]: pair[1] for pair in self}

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def __call__(self, x):
        if x not in self._domain:
            raise ValueError(f"{x!r} is not in the function's domain.")
        return self._lookup[x]
