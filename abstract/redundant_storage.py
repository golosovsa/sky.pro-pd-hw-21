"""
    Abstract class RedundantStorage
"""

from abc import ABC, abstractmethod

from .storage import Storage


class RedundantStorage(Storage, ABC):

    _redundant: Storage = NotImplemented

    @abstractmethod
    def reserve(self, product: str, amount: int) -> int:
        pass

    @abstractmethod
    def apply_reservation(self, product: str, amount: int):
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass
