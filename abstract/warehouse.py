"""
    Abstract class Warehouse
"""

from abc import ABC, abstractmethod
from .redundant_storage import RedundantStorage
from .essence import Essence


class Warehouse(RedundantStorage, Essence, ABC):
    _type = "warehouse"
