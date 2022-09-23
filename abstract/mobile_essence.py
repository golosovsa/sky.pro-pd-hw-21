"""
    Abstract class MobileEssence
"""

from abc import ABC, abstractmethod
from .essence import Essence


class MobileEssence(Essence, ABC):

    _speed: float = NotImplemented

    @abstractmethod
    def calc_time(self, distance: float) -> float:
        pass

    @abstractmethod
    def update_position_to(self, dest, time):
        pass

    @abstractmethod
    def is_in_position(self, dest) -> bool:
        pass
