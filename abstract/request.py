"""
    Abstract class Request
"""

from abc import ABC, abstractmethod


class Request(ABC):

    @staticmethod
    @abstractmethod
    def create(world, query: str) -> "Request":
        pass

    @abstractmethod
    def update(self, world):
        pass

    @property
    @abstractmethod
    def progress(self) -> float:
        pass
