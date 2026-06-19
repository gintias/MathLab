



class FiniteTuple:

    def __init__(self, *entries):
        self._entries = tuple(entries)

    @property
    def entries(self):
        return self._entries

    @property
    def arity(self):
        return len(self._entries)

    def is_singleton(self):
        return self.arity == 1
    
    def unbox_if_singleton(self):
        """
        Display/helper convention only.

        Do not use this for internal equality or hashing.
        """
        if self.arity == 1:
            return self._entries[0]
        return self

    def is_pair(self):
        return self.arity == 2

    def __getitem__(self, index):
        return self._entries[index]
    
    def __contains__(self, x):
        return x in self._entries

    def __iter__(self):
        return iter(self._entries)

    def __len__(self):
        return len(self._entries)

    def __eq__(self, other):
        return isinstance(other, FiniteTuple) and self._entries == other._entries

    def __hash__(self):
        return hash(self._entries)

    def __repr__(self):
        return f"FiniteTuple{self._entries!r}"

    def __str__(self):
        return "(" + ", ".join(str(x) for x in self._entries) + ")"

    @property
    def entries(self):
        return self._entries

    @property
    def arity(self):
        return len(self._entries)
    
    def is_pair(self):
        return isinstance(self, FiniteTuple) and self.arity == 2

    def prepend(self, x):
      return FiniteTuple(x, *self._entries)

    def append(self, x):
      return FiniteTuple(*self._entries,x)
    
    def concat(self, other):
        if not isinstance(other, FiniteTuple):
            raise TypeError("concat expects another FiniteTuple.")
        return FiniteTuple(*self._entries, *other._entries)
    
