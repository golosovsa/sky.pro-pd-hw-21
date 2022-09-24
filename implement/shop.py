"""
    Implementation of Shop
"""

import abstract
from implement.base import UniqRedundantStorage, Essence


class Shop(UniqRedundantStorage, Essence, abstract.Shop):
    _type = "Shop"

    def __init__(self, name, position, capacity=20, uniq_capacity=5):
        UniqRedundantStorage.__init__(self, capacity=capacity, uniq_capacity=uniq_capacity)
        Essence.__init__(self, name=name, position=position)

    def __del__(self):
        Essence.__del__(self)
