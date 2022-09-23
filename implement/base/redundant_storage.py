"""
    base class implement RedundantStorage
"""

import abstract
from .storage import Storage


class RedundantStorage(Storage, abstract.RedundantStorage):

    def __init__(self, **kwargs):
        super(RedundantStorage, self).__init__(**kwargs)
        self._redundant = Storage(capacity=self._capacity)

    def reserve(self, product: str, amount: int) -> int:
        amount = min(self.get_free_space(), amount)
        if amount <= 0:
            return 0
        return self._redundant.add(product, amount)

    def apply_reservation(self, product: str, amount: int):
        amount = min(self._redundant.get_one(product), amount)
        if amount <= 0:
            return 0
        removed_from_redundant = self._redundant.remove(product, amount)
        added_to_self = self.add(product, removed_from_redundant)
        return added_to_self

    def get_free_space(self) -> int:
        free = super(RedundantStorage, self).get_free_space()
        redundant = sum(self._redundant.get_all().values())
        return free - redundant
