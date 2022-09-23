"""
    base class implement Storage
"""

import abstract
from .repository import Repository


class Storage(Repository, abstract.Storage):

    def __init__(self, **kwargs):
        assert "capacity" in kwargs, "Missing required parameter capacity"
        assert type(kwargs["capacity"]) == int, "Required parameter capacity must be an int"
        assert kwargs["capacity"] > 0, "Required parameter capacity must be greater than 0"
        self._capacity = kwargs["capacity"]
        super(Storage, self).__init__(**kwargs)

    @property
    def capacity(self) -> int:
        return self._capacity

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> dict[str, int]:
        return self.get_all()

    def get_unique_items_count(self) -> int:
        return len(self._items)

    def add(self, product, amount) -> int:
        """ Returns how much was added """
        amount = min(self.get_free_space(), amount)
        if amount <= 0:
            return 0
        super(Storage, self).add(product, amount)
        return amount

    def remove(self, product, amount) -> int:
        """ Returns how much was removed """
        amount = min(self.get_one(product), amount)
        if amount <= 0:
            return 0
        super(Storage, self).remove(product, amount)
        return amount
