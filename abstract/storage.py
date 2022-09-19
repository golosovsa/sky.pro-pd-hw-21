"""
    Abstract class Storage
"""

from abc import ABC, abstractmethod


class Storage(ABC):

    _type: str = "Abstract"

    @property
    def type(self):
        return self._type

    @abstractmethod
    def add(self, product, amount):
        pass

    @abstractmethod
    def remove(self, product, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
