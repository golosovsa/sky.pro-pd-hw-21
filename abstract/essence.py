"""
    Abstract class Essence
"""

from abc import ABC, abstractmethod


class Essence(ABC):

    _type: str = NotImplemented
    _name: str = NotImplemented
    _position: tuple[float, float] = NotImplemented

    @classmethod
    @property
    @abstractmethod
    def type(cls) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def position(self) -> tuple[float, float]:
        pass

    @staticmethod
    @abstractmethod
    def calc_distance(where, dest) -> float:
        pass

    @abstractmethod
    def calc_distance_to(self, dest) -> float:
        pass
