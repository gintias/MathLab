try:
    from .FiniteSet import FiniteSet
    from .FiniteTuple import FiniteTuple
except ImportError:
    from FiniteSet import FiniteSet
    from FiniteTuple import FiniteTuple


def product_set(*sets):

    for S in sets:
        if not isinstance(S, FiniteSet):
            raise TypeError("product_set expects FiniteSet arguments.")

    if len(sets) == 0:
        return FiniteSet([FiniteTuple()])
    first = sets[0]
    rest = sets[1:]
    rest_product = product_set(*rest)

    result = []
    for a in first:
        for t in rest_product:
            result.append(t.prepend(a))

    return FiniteSet(result)





empty = FiniteSet([])
atom_set = FiniteSet([1])
pure_set = FiniteSet([empty])
mixed_set = FiniteSet([1, empty])

print(1)
print(1 in atom_set, empty in pure_set, pure_set.union(mixed_set) == FiniteSet([empty, 1]))
