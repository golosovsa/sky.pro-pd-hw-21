"""
    Abstract class Essence
"""

from abc import ABC, abstractmethod


class AbstractEssence(ABC):

    @property
    @abstractmethod
    def longitude(self) -> float:
        pass

    @property
    @abstractmethod
    def latitude(self) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def calc_distance(self, essence) -> float:
        pass
