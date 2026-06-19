try:
    from .FiniteSet import FiniteSet
    from .FiniteTuple import FiniteTuple
except ImportError:
    from FiniteSet import FiniteSet
    from FiniteTuple import FiniteTuple


class RelationEntry:
    """
    An ordered pair of tuple-blocks.

    Internally:
        ((x_1,...,x_m), (y_1,...,y_n))

    The left and right components are always FiniteTuple objects.
    """

    def __init__(self, left, right):
        self._left = self._coerce_block(left)
        self._right = self._coerce_block(right)

    def _coerce_block(self, block):
        """
        Coerce input into a FiniteTuple block.

        Examples:
            a                  -> FiniteTuple(a)
            (a, b)              -> FiniteTuple(a, b)
            FiniteTuple(a, b)   -> FiniteTuple(a, b)
        """
        if isinstance(block, FiniteTuple):
            return block

        if isinstance(block, tuple):
            return FiniteTuple(*block)

        return FiniteTuple(block)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def input_arity(self):
        return self._left.arity

    @property
    def output_arity(self):
        return self._right.arity

    @property
    def total_arity(self):
        return self.input_arity + self.output_arity

    def inverse(self):
        return RelationEntry(self._right, self._left)

    def __getitem__(self, index):
        if index == 0:
            return self._left
        if index == 1:
            return self._right
        raise IndexError("RelationEntry has only two components: left and right.")

    def __iter__(self):
        return iter((self._left, self._right))

    def __eq__(self, other):
        return (
            isinstance(other, RelationEntry)
            and self._left == other._left
            and self._right == other._right
        )

    def __hash__(self):
        return hash((self._left, self._right))

    def _display_block(self, block):
        """
        Display convention:
            FiniteTuple(a) displays as a.
            FiniteTuple(a,b) displays as (a,b).

        Internal structure is not changed.
        """
        if block.arity == 1:
            return str(block[0])
        return str(block)

    def __repr__(self):
        return f"RelationEntry({repr(self._left)}, {repr(self._right)})"

    def __str__(self):
        left = self._display_block(self._left)
        right = self._display_block(self._right)
        return f"({left}, {right})"


class Relation(FiniteSet):
    """
    A finite relation.
    Every entry is an ordered pair of tuple-blocks:
        ((x_1,...,x_m), (y_1,...,y_n))
    So every relation is binary at the top level, but the left and right
    sides may have arbitrary finite arity.
    The relation has an arity profile:
        (input_arity, output_arity)
    and total arity:
        input_arity + output_arity.
    """

    def __init__(self, entries, input_arity=None, output_arity=None, name=None):
        self.name = name

        normalized_entries = [self._coerce_entry(entry) for entry in entries]

        self._input_arity, self._output_arity = self._resolve_arity_profile(
            normalized_entries,
            input_arity,
            output_arity,
        )

        super().__init__(normalized_entries)

    # ------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------

    def _coerce_entry(self, entry):
        """
        Coerce acceptable presentations into RelationEntry objects.

        Accepted:
            RelationEntry(left, right)
            (left, right)

        Important:
            A raw flat tuple like (a,b,c) is rejected.
        """
        if isinstance(entry, RelationEntry):
            return entry

        if isinstance(entry, tuple) and len(entry) == 2:
            left, right = entry
            return RelationEntry(left, right)

        raise TypeError(
            "Relation entries must be RelationEntry objects or pairs (left_block, right_block). "
            "Flat tuples like (a,b,c) are not allowed."
        )

    def _resolve_arity_profile(self, entries, declared_input_arity, declared_output_arity):
        """
        Resolve the common input/output arities of all relation entries.

        Empty relations require both input_arity and output_arity.
        Nonempty relations must have uniform arity profile.
        """
        for value, label in [
            (declared_input_arity, "input_arity"),
            (declared_output_arity, "output_arity"),
        ]:
            if value is not None:
                if not isinstance(value, int):
                    raise TypeError(f"{label} must be an integer.")
                if value < 0:
                    raise ValueError(f"{label} must be nonnegative.")

        if len(entries) == 0:
            if declared_input_arity is None or declared_output_arity is None:
                raise ValueError(
                    "Cannot infer arity profile of an empty relation. "
                    "Declare input_arity and output_arity."
                )
            return declared_input_arity, declared_output_arity

        profiles = {
            (entry.input_arity, entry.output_arity)
            for entry in entries
        }

        if len(profiles) != 1:
            raise ValueError("All relation entries must have the same arity profile.")

        inferred_input_arity, inferred_output_arity = next(iter(profiles))

        if (
            declared_input_arity is not None
            and declared_input_arity != inferred_input_arity
        ):
            raise ValueError("Declared input_arity does not match entries.")

        if (
            declared_output_arity is not None
            and declared_output_arity != inferred_output_arity
        ):
            raise ValueError("Declared output_arity does not match entries.")

        return inferred_input_arity, inferred_output_arity

    # ------------------------------------------------------------
    # Arity data
    # ------------------------------------------------------------

    @property
    def input_arity(self):
        return self._input_arity

    @property
    def output_arity(self):
        return self._output_arity

    @property
    def arity_profile(self):
        return (self._input_arity, self._output_arity)

    @property
    def total_arity(self):
        return self._input_arity + self._output_arity

    def is_plain_binary(self):
        """
        True iff entries have shape ((a),(b)).

        Display-wise these look like ordinary pairs (a,b).
        """
        return self.arity_profile == (1, 1)

    # ------------------------------------------------------------
    # Domain/range
    # ------------------------------------------------------------

    def domain(self):
        """
        Domain of the relation: set of left blocks.
        """
        return FiniteSet(entry.left for entry in self)

    def range(self):
        """
        Range of the relation: set of right blocks.
        """
        return FiniteSet(entry.right for entry in self)

    def field(self):
        """
        Field of the relation.

        For now this returns the union of the domain and range as block-objects.

        If R has profile (1,1), this is the usual field except elements are
        singleton FiniteTuple blocks internally.
        """
        return self.domain().union(self.range())

    # ------------------------------------------------------------
    # Relation operations
    # ------------------------------------------------------------

    def inverse(self):
        return Relation(
            (entry.inverse() for entry in self),
            input_arity=self.output_arity,
            output_arity=self.input_arity,
        )

    def image(self, S):
        """
        Image of a set S of left blocks:

            R[S] = { right : exists left in S with (left,right) in R }.

        S should contain FiniteTuple blocks, not raw elements.
        """
        return FiniteSet(entry.right for entry in self if entry.left in S)

    def preimage(self, T):
        """
        Preimage of a set T of right blocks:

            R^{-1}[T] = { left : exists right in T with (left,right) in R }.
        """
        return FiniteSet(entry.left for entry in self if entry.right in T)

    def restriction(self, S):
        """
        Domain restriction:

            R|S = { (left,right) in R : left in S }.
        """
        return Relation(
            (entry for entry in self if entry.left in S),
            input_arity=self.input_arity,
            output_arity=self.output_arity,
        )

    # ------------------------------------------------------------
    # Display
    # ------------------------------------------------------------

    def __repr__(self):
        return (
            f"Relation({{{', '.join(map(repr, self))}}}, "
            f"input_arity={self.input_arity}, "
            f"output_arity={self.output_arity})"
        )

    def __str__(self):
        if self.is_empty():
            return f"∅_profile_{self.arity_profile}"

        return "{" + ", ".join(str(entry) for entry in self) + "}"
    