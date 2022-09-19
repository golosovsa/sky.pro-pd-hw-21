"""
    Abstract class Request
"""

from abc import ABC, abstractmethod


class Request(ABC):

    @staticmethod
    @abstractmethod
    def create(world, query):
        pass

    @abstractmethod
    def get_progress(self):
        pass

    @abstractmethod
    def execute(self):
        pass
