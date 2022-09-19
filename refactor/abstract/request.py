"""
    Abstract class Request
"""
from abc import ABC, abstractmethod
from storage import AbstractStorage


class AbstractRequest(ABC):
    """ Abstract class """

    @property
    @abstractmethod
    def where(self) -> str:
        pass

    @property
    @abstractmethod
    def dest(self) -> str:
        pass

    @property
    @abstractmethod
    def product(self) -> str:
        pass

    @property
    @abstractmethod
    def amount(self) -> int:
        pass

    @classmethod
    @abstractmethod
    def create(cls, city, query: str) -> "AbstractRequest":
        pass

    @abstractmethod
    def execute(self):
        pass
