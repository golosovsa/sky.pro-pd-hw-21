"""
    Abstract class Storage
"""

from abc import ABC, abstractmethod
from .protected_repository import ProtectedRepository
from .essence import Essence


class Storage(ProtectedRepository, ABC):

    @classmethod
    @abstractmethod
    def type(cls) -> str:
        pass

    @property
    @abstractmethod
    def capacity(self) -> int:
        pass

    @abstractmethod
    def add(self, product, amount) -> int:
        pass

    @abstractmethod
    def remove(self, product, amount) -> int:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
