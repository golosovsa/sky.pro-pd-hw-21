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
        return cls._type

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name

    @property
    @abstractmethod
    def position(self) -> tuple[float, float]:
        return self._position

    @staticmethod
    @abstractmethod
    def calc_distance(where, dest) -> float:
        pass

    @abstractmethod
    def calc_distance_to(self, dest) -> float:
        pass
