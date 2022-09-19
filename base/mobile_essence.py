"""
    Base class implementation MobileEssence
"""
import math
import abstract
from .essence import Essence


class MobileEssence(abstract.MobileEssence, Essence):

    _type: str = "Base Mobile"
    _in_position_radius: float = 5.0

    def __init__(self, name: str, position: tuple[float, float], speed: float):
        super(Essence, self).__init__(name, position)
        self._speed = speed

    @property
    def speed(self) -> float:
        return self._speed

    def calc_time(self, distance: float) -> float:
        return distance / self._speed

    def update_position_to(self, essence_to: Essence, time):

        if self.is_in_position(essence_to) or time == 0:
            return

        distance = self.calc_distance_to(essence_to)
        calc_time = self.calc_time(distance)

        if time >= calc_time:
            self._position = essence_to._position
            return

        diff_x_diff_t = (essence_to._position[0] - self._position[0]) / calc_time
        diff_y_diff_t = (essence_to._position[1] - self._position[1]) / calc_time
        new_x = self._position[0] + diff_x_diff_t * time
        new_y = self._position[1] + diff_y_diff_t * time
        self._position = new_x, new_y

    def is_in_position(self, essence_dest) -> bool:
        return self.calc_distance_to(essence_dest) <= self._in_position_radius
