"""
    Implementation of Warehouse
"""

import abstract
from .base import RedundantStorage, Essence


class Warehouse(RedundantStorage, Essence, abstract.Warehouse):
    _type = "Warehouse"

    def __init__(self, name, position, capacity=100):
        RedundantStorage.__init__(self, capacity=capacity)
        Essence.__init__(self, name=name, position=position)

    def __del__(self):
        Essence.__del__(self)
