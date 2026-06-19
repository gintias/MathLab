from typing import Optional

class Registry:
    """
    Internal canonical-key and equality-class manager.
    """

    def __init__(self):
        # Maps canonical key -> record_id
        self.key_to_record_id: dict[tuple, int] = {}
        self.parent: dict[int, int] = {}

    def register_record(self, key: tuple, record_id: int) -> None:
        """
        Register a record by its canonical key.

        """
        self.key_to_record_id[key] = record_id
        self.make_record_node(record_id)

    def has_key(self, key: tuple) -> bool:
        """
        Check if we have seen this canonical key before.

        """
        return key in self.key_to_record_id
    
    def lookup_key(self, key: tuple) -> Optional[int]:
        """
        Retreive the record_id associated with a canonical_key.

        """
        return self.key_to_record_id.get(key)
    
    def make_record_node(self, record_id: int) -> None:
        """
        Initialize union-find node for a record.

        """
        if record_id not in self.parent:
            self.parent[record_id] = record_id

    def canonical_id(self, record_id: int) -> int:
        """
        Union-find find operation with path compression.
        Returns the canonical representative of record_id.

        """
        if self.parent[record_id] != record_id:
            self.parent[record_id] = self.canonical_id(self.parent[record_id])
        return self.parent[record_id]

    def union_equal(self, left_id: int, right_id: int) -> None:
        """
        Record that two records are known equal.
        Union them in the union-find structure.

        """
        left_canon = self.canonical_id(left_id)
        right_canon = self.canonical_id(right_id)
        
        if left_canon != right_canon:
            # Make left the parent of right
            self.parent[right_canon] = left_canon

    def known_equal(self, left_id: int, right_id: int) -> bool:
        """
        Check if two records are in the same equality class.

        """
        return self.canonical_id(left_id) == self.canonical_id(right_id)