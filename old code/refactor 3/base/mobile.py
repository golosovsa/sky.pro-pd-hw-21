"""
    Base class implement Mobile
"""

from .storage import Storage
from .mobile_essence import MobileEssence


class Mobile(Storage, MobileEssence):
    _type = "mobile"
