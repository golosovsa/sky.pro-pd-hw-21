"""
    Abstract class Courier
"""

from abc import ABC, abstractmethod
from .storage import Storage
from .mobile_essence import MobileEssence


class Courier(Storage, MobileEssence, ABC):
    _type = "courier"

