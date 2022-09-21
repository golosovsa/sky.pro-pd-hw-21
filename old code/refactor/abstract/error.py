"""
    Abstract class Error
"""

from abc import ABC, abstractmethod


class AbstractError(Exception, metaclass=ABC):
    @property
    @abstractmethod
    def message(self):
        pass
