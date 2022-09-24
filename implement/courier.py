"""
    Implementation of Courier
"""

import abstract
from implement.base import Storage, MobileEssence


class Courier(Storage, MobileEssence, abstract.Courier):
    _type = "Courier"

    def __init__(self, name, position, speed=5, capacity=1):
        Storage.__init__(self, capacity=capacity)
        MobileEssence.__init__(self, name=name, position=position, speed=speed)

    def __del__(self):
        MobileEssence.__del__(self)
