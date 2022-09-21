"""
    Abstract class Courier
"""

from abc import ABC, abstractmethod


class AbstractCourier(ABC):

    @property
    @abstractmethod
    def speed(self) -> float:
        pass

    @abstractmethod
    def calc_delivery_time(self, where, dest) -> float:
        pass
