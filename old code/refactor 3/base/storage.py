"""
    Base class implement Storage
"""

import abstract
from .protected_repository import ProtectedRepository


class Storage(abstract.Storage, ProtectedRepository):

    _type: str = "Base"

    def __init__(self, capacity: int):
        super().__init__()
        self._capacity = capacity

    @property
    def capacity(self) -> int:
        return self._capacity

    @classmethod
    def type(cls):
        return cls._type

    def add(self, product, amount) -> int:
        """ Returns how much was added """
        free = self.get_free_space()
        amount = min(amount, free)
        self._add(product, amount)
        return amount

    def remove(self, product, amount) -> int:
        """ Returns how much was removed """
        total = self._get_one(product)
        amount = min(amount, total)
        self._remove(product, amount)
        return amount

    def get_free_space(self) -> int:
        free = self._capacity - sum(self._data.values())
        return 0 if free < 0 else free

    def get_items(self) -> dict[str, int]:
        return self._get_all()

    def get_unique_items_count(self) -> int:
        return len(self._data)



