"""
    Implementation of Shop
"""

import abstract
from implement.base import UniqRedundantStorage, Essence


class Shop(UniqRedundantStorage, Essence, abstract.Shop):
    _type = "Shop"

    def __init__(self, name, position, capacity=20, uniq_capacity=5):
        super(Shop, self).__init__(name=name, position=position, capacity=capacity, uniq_capacity=uniq_capacity)
