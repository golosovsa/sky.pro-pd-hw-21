"""
    Abstract class Essence
"""

from abc import ABC, abstractmethod


class Essence(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def position(self) -> tuple[float, float]:
        pass

    @abstractmethod
    def calc_distance_to(self, essence: "Essence") -> float:
        pass
