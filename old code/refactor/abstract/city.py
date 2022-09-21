"""
    Abstract class City
"""

from abc import ABC, abstractmethod


class AbstractCity(ABC):

    @property
    @abstractmethod
    def places(self) -> dict[str, object]:
        pass

    @property
    @abstractmethod
    def couriers(self) -> dict[str, object]:
        pass

    @abstractmethod
    def get_place(self, name) -> object:
        pass

    @abstractmethod
    def get_courier(self, place) -> object:
        pass

    @abstractmethod
    def add_place(self, place):
        pass

    @abstractmethod
    def add_courier(self, courier):
        pass
