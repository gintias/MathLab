class FiniteSet:
    """
    A finite mathematical set.

    Responsibility:
        - store a finite collection of distinct elements
        - provide membership, iteration, cardinality
        - provide standard finite set operations
        - expose basic facts about itself
        - serve as a carrier for later structures
    """

    # ------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------

    def __init__(self, elements, *, name=None):
        """
        Create a finite set from an iterable/presentation of elements.

        Expected behavior:
            - validate input
            - remove duplicates according to equality
            - store canonical internal representation
            - record basic facts
        """
        ...

    @classmethod
    def empty(cls, *, name=None):
        """
        Construct the empty finite set.
        """
        ...

    @classmethod
    def singleton(cls, x, *, name=None):
        """
        Construct {x}.
        """
        ...

    @classmethod
    def from_iterable(cls, iterable, *, name=None):
        """
        Construct a finite set from an iterable.
        """
        ...

    @classmethod
    def from_predicate(cls, universe, predicate, *, name=None):
        """
        Construct {x in universe : predicate(x)}.

        Here universe should itself be finite/enumerable.
        """
        ...

    # ------------------------------------------------------------
    # Validation / normalization
    # ------------------------------------------------------------

    def _validate_elements(self, elements):
        """
        Check that the proposed element presentation is acceptable.

        Possible checks:
            - is it iterable?
            - can it be exhausted finitely?
            - are elements comparable by equality?
            - are elements hashable, if using frozenset internally?
        """
        ...

    def _normalize_elements(self, elements):
        """
        Convert the input presentation into the canonical internal form.

        Possible internal form:
            - frozenset
            - tuple with duplicate removal
            - ordered tuple plus equality logic

        For now, probably frozenset.
        """
        ...

    def _record_basic_facts(self):
        """
        Store basic facts:
            - finite
            - cardinality
            - empty/nonempty
            - singleton/non-singleton
        """
        ...

    # ------------------------------------------------------------
    # Basic access
    # ------------------------------------------------------------

    def elements(self):
        """
        Return the elements as a stable collection.
        """
        ...

    def cardinality(self):
        """
        Return |A|.
        """
        ...

    def is_empty(self):
        """
        Return True iff A = empty set.
        """
        ...

    def is_singleton(self):
        """
        Return True iff |A| = 1.
        """
        ...

    def contains(self, x):
        """
        Return True iff x in A.
        """
        ...

    def __contains__(self, x):
        """
        Python membership syntax: x in A.
        """
        ...

    def __iter__(self):
        """
        Iterate over elements of A.
        """
        ...

    def __len__(self):
        """
        Return |A|.
        """
        ...

    # ------------------------------------------------------------
    # Equality / representation
    # ------------------------------------------------------------

    def equals(self, other):
        """
        Mathematical equality of finite sets:
            A = B iff they have the same elements.
        """
        ...

    def __eq__(self, other):
        """
        Python equality.
        """
        ...

    def __repr__(self):
        """
        Developer-facing representation.
        """
        ...

    def display(self):
        """
        Human/math-facing display.
        """
        ...

    # ------------------------------------------------------------
    # Subset relations
    # ------------------------------------------------------------

    def is_subset_of(self, other):
        """
        Return True iff self ⊆ other.
        """
        ...

    def is_proper_subset_of(self, other):
        """
        Return True iff self ⊂ other.
        """
        ...

    def is_superset_of(self, other):
        """
        Return True iff self ⊇ other.
        """
        ...

    def is_disjoint_from(self, other):
        """
        Return True iff self ∩ other = empty set.
        """
        ...

    # ------------------------------------------------------------
    # Set operations
    # ------------------------------------------------------------

    def union(self, other, *, name=None):
        """
        Return self ∪ other.
        """
        ...

    def intersection(self, other, *, name=None):
        """
        Return self ∩ other.
        """
        ...

    def difference(self, other, *, name=None):
        """
        Return self \\ other.
        """
        ...

    def symmetric_difference(self, other, *, name=None):
        """
        Return (self \\ other) ∪ (other \\ self).
        """
        ...

    # ------------------------------------------------------------
    # Products and powersets
    # ------------------------------------------------------------

    def cartesian_product(self, other, *, name=None):
        """
        Return self × other as a finite set of ordered pairs.

        Later this may return a FiniteProductSet instead of plain FiniteSet.
        """
        ...

    def power_set(self, *, name=None):
        """
        Return P(self), the finite set of all subsets of self.

        Elements should probably be FiniteSet objects or frozen representations.
        """
        ...

    def tuples(self, arity, *, name=None):
        """
        Return A^arity.

        Useful later for relations of arity n.
        """
        ...

    # ------------------------------------------------------------
    # Images / preimages, later useful for functions
    # ------------------------------------------------------------

    def image_under(self, function, *, name=None):
        """
        Return f[self].

        This should probably wait until Function exists.
        Placeholder for now.
        """
        ...

    def filter(self, predicate, *, name=None):
        """
        Return {x in self : predicate(x)}.
        """
        ...

    # ------------------------------------------------------------
    # Facts / metadata
    # ------------------------------------------------------------

    def facts(self):
        """
        Return basic known facts about this finite set.

        Example:
            finite
            cardinality = n
            empty/nonempty
            singleton/non-singleton
        """
        ...

    def explain(self):
        """
        Return a human-readable explanation of how this set was constructed
        and what basic facts are known.
        """
        ...