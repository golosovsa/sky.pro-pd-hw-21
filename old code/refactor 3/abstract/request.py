"""
    Abstract class Request
"""

from abc import ABC, abstractmethod
from .task import Task
from .world import World


class Request(ABC):

    @staticmethod
    @abstractmethod
    def create(world, query: str) -> "Request":
        pass

    @abstractmethod
    def update(self, world: World):
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
    def task_completed(self, task: Task):
        pass
