"""
    Abstract class MobileEssence
"""

from abc import ABC, abstractmethod
from .essence import Essence


class MobileEssence(Essence, ABC):

    @property
    @abstractmethod
    def speed(self) -> float:
        pass

    @abstractmethod
    def calc_time(self, distance: float) -> float:
        pass

    @abstractmethod
    def update_position_to(self, essence_to: Essence, time):
        pass

    @abstractmethod
    def is_in_position(self, essence_dest) -> bool:
        pass
