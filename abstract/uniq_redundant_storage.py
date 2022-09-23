"""
    Abstract class UniqRedundantStorage
"""

from abc import ABC, abstractmethod

from .redundant_storage import RedundantStorage


class UniqRedundantStorage(RedundantStorage, ABC):

    _uniq_capacity: int = NotImplemented

    @abstractmethod
    def get_free_space(self) -> int:
        pass
