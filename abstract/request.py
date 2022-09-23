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
    def _create_task(self, world):
        pass

    @abstractmethod
    def _task_completed(self, world, task):
        pass

    @abstractmethod
    def update(self, world):
        pass
