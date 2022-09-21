"""
    Abstract class Storage
"""

from abc import ABC, abstractmethod


class Task(ABC):

    @property
    @abstractmethod
    def _where(self):
        pass

    @property
    @abstractmethod
    def _dest(self):
        pass

    @property
    @abstractmethod
    def _performer(self):
        pass

    @property
    @abstractmethod
    def status(self) -> str:
        pass

    @classmethod
    @property
    @abstractmethod
    def _steps(cls) -> str:
        pass

    @property
    @abstractmethod
    def _step_index(cls) -> str:
        pass

    @abstractmethod
    async def update(self):
        pass
