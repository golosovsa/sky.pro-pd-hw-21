"""
    Abstract class Storage
"""

from abc import ABC, abstractmethod
from .warehouse import Warehouse
from .shop import Shop
from .courier import Courier


class Task(ABC):

    _steps: list[str] = NotImplemented

    _where: Warehouse | Shop = NotImplemented
    _dest: Warehouse | Shop = NotImplemented
    _performer: Courier = NotImplemented
    _step_index: int = NotImplemented
    _time: float = NotImplemented

    @property
    @abstractmethod
    def status(self) -> str:
        pass

    @property
    @abstractmethod
    def performer(self) -> Courier:
        pass

    @abstractmethod
    def update(self):
        pass
