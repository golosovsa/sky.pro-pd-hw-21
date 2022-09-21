"""
    Abstract class UniqRedundantStorage
"""

from abc import ABC, abstractmethod

from .redundant_storage import RedundantStorage


class UniqRedundantStorage(RedundantStorage, ABC):

    @property
    @abstractmethod
    def _uniq_capacity(self) -> int:
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
