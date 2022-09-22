"""
    Abstract class Shop
"""

from abc import ABC, abstractmethod
from .uniq_redundant_storage import UniqRedundantStorage
from .essence import Essence


class Shop(UniqRedundantStorage, Essence, ABC):
    _type = "shop"
