"""
    Abstract class Essence
"""

from abc import ABC, abstractmethod


class Essence(ABC):

    @classmethod
    @property
    @abstractmethod
    def _type(cls) -> str:
        pass

    @property
    @abstractmethod
    def _name(self) -> str:
        pass

    @property
    @abstractmethod
    def _position(self) -> tuple[float, float]:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        return self._type

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

    @staticmethod
    @abstractmethod
    def create(**kwargs):
        pass

