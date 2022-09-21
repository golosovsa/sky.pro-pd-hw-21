"""
    Base class implementation ReservationStorage
"""

import abstract
from .storage import Storage


class ReservationStorage(Storage, abstract.ReservationStorage):

    _type: str = "static"

    def __init__(self, **kwargs):
        capacity = kwargs["capacity"]
        super(ReservationStorage, self).__init__(capacity)
        self._reservation_storage: Storage = Storage(capacity)

    def reserve(self, product: str, amount: int) -> int:
        """ Returns how much was reserved """
        free = self.get_free_space()
        amount = min(amount, free)
        if amount <= 0:
            return 0
        amount = self._reservation_storage.add(product, amount)
        return amount

    def apply_reservation(self, product: str, amount: int):
        amount = self._reservation_storage.remove(product, amount)
        self.add(product, amount)

    def get_free_space(self):
        free = super(ReservationStorage, self).get_free_space()
        return free - (self._reservation_storage.capacity - self._reservation_storage.get_free_space())
