"""
    Abstract class Storage
"""
from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    """ Abstract class """

    @property
    @abstractmethod
    def type(self) -> str:
        """ Storage type """
        pass

    @property
    @abstractmethod
    def items(self) -> dict[str, int]:
        """ Storage items """
        pass

    @property
    @abstractmethod
    def capacity(self) -> int:
        """ Storage capacity """
        pass

    @abstractmethod
    def add(self, product: str, amount: int):
        """ Increases stock of items """
        pass

    @abstractmethod
    def remove(self, product: str, amount: int):
        """ Decreases stock of items """
        pass

    @abstractmethod
    def get_free_space(self):
        """ Amount of free space for items """
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        """ Returns the number of unique items """
        pass
