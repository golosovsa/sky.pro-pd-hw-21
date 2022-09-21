"""
    Base implementation of class Courier
"""

from refactor import abstract
from essence import BaseEssence


class BaseCourier(abstract.Courier):

    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self) -> float:
        return self._speed

    def calc_delivery_time(self, where: BaseEssence, dest: BaseEssence) -> float:
        distance = where.calc_distance(dest)
        time = distance / self._speed
        return time
