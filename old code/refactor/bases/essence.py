"""
    Base implementation of class Essence
"""

from refactor import abstract
from math import radians, acos, sin, cos


class BaseEssence(abstract.Essence):

    def __init__(self, name, longitude, latitude):
        self._name = name
        self._longitude = longitude
        self._latitude = latitude

    @property
    def longitude(self) -> float:
        return self.longitude

    @property
    def latitude(self) -> float:
        return self.latitude

    @property
    def name(self) -> str:
        return self._name

    def calc_distance(self, essence: "BaseEssence") -> float:
        """ Calculate distance between two essences in km """
        self_latitude_rad = radians(self._latitude)
        self_longitude_rad = radians(self._longitude)
        essence_latitude_rad = radians(essence._latitude)
        essence_longitude_rad = radians(essence._longitude)

        distance = acos(cos(self_latitude_rad) *
                        cos(essence_latitude_rad) *
                        cos(self_longitude_rad - essence_longitude_rad) +
                        sin(self_latitude_rad) *
                        sin(essence_latitude_rad))

        distance *= self._get_constant_radius()
        return distance

    @staticmethod
    def _get_constant_radius():
        earth_radius = 6_372.795
        return earth_radius
