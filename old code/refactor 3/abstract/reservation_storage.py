"""
    Abstract class ReservationStorage
"""

from abc import ABC, abstractmethod
from .storage import Storage


class ReservationStorage(ABC):

    @abstractmethod
    def reserve(self, product: str, amount: int) -> int:
        pass

    @abstractmethod
    def apply_reservation(self, product: str, amount: int):
        pass
