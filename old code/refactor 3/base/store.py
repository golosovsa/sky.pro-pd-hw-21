"""
    Base class implementation Storage
"""

from implementation import ReservationStorage, Essence


class Store(ReservationStorage, Essence):
    def __init__(self, capacity, name, position):
        super(Store, self).__init__(capacity=capacity, name=name, position=position)



