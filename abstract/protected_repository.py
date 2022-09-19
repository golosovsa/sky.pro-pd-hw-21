"""
    Abstract class ProtectedRepository
"""

from abc import ABC, abstractmethod


class ProtectedRepository(ABC):

    @abstractmethod
    def _add(self, key: str, count: int):
        pass

    @abstractmethod
    def _remove(self, key: str, count: int):
        pass

    @abstractmethod
    def _get_one(self, key: str):
        pass

    @abstractmethod
    def _get_all(self):
        pass

    @abstractmethod
    def __contains__(self, key: str):
        pass
