"""
    Abstract class Essence
"""

from abc import ABC, abstractmethod


class Request(ABC):
    @staticmethod
    @abstractmethod
    def create(world, query):
        pass

    @property
    @abstractmethod
    def progress(self) -> float:
        pass

    @property
    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def task_completed(self, task):
        pass

    @abstractmethod
    async def update(self):
        pass
