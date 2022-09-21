"""
    Abstract class Task
"""

from abc import ABC, abstractmethod

from .mobile_essence import MobileEssence
from .essence import Essence


class Task(ABC):

    @property
    @abstractmethod
    def where(self) -> Essence:
        pass

    @property
    @abstractmethod
    def dest(self) -> Essence:
        pass

    @property
    @abstractmethod
    def performer(self) -> MobileEssence:
        pass

    @property
    @abstractmethod
    def status(self) -> str:
        pass

    @abstractmethod
    def update(self):
        pass

