"""
    Implementation of Courier
"""

import abstract
from implement.base import Storage, MobileEssence


class Courier(Storage, MobileEssence, abstract.Courier):
    _type = "Courier"

    def __init__(self, name, position, speed, capacity):
        super(Courier, self).__init__(name=name, position=position, speed=speed, capacity=capacity)
