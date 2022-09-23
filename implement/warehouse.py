"""
    Implementation of Warehouse
"""

import abstract
from .base import RedundantStorage, Essence


class Warehouse(RedundantStorage, Essence, abstract.Warehouse):
    _type = "Warehouse"

    def __init__(self, name, position, capacity=100):
        super(Warehouse, self).__init__(name=name, position=position, capacity=capacity)

