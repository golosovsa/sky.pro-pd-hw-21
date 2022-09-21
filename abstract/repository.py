"""
    Abstract class Repository
"""

from abc import ABC, abstractmethod


class Repository(ABC):

    @property
    @abstractmethod
    def _items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def add(self, key: str, count: int):
        pass

    @abstractmethod
    def remove(self, key: str, count: int):
        pass

    @abstractmethod
    def get_one(self, key: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def __contains__(self, key: str):
        pass
