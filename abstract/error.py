"""
    Abstract class Error
"""

from abc import ABC, abstractmethod


class Error(Exception, ABC):
    @property
    @abstractmethod
    def message(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
