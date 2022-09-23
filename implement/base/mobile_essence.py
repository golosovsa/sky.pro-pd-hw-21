"""
    base class implement MobileEssence
"""

import abstract
from .essence import Essence


class MobileEssence(Essence, abstract.MobileEssence):

    _type: str = "Mobile Essence"
    __in_position_radius: float = 5

    def __init__(self, **kwargs):
        assert "speed" in kwargs, "Missing required parameter speed"
        assert type(kwargs["speed"]) in {float, int}, "Required parameter speed must be a float or an int"
        assert kwargs["speed"] > 0, "Required parameter speed must be greater than 0"
        super(MobileEssence, self).__init__(**kwargs)
        self._speed = kwargs["speed"]

    def calc_time(self, distance: float) -> float:
        return distance / self._speed

    def update_position_to(self, dest: Essence, time: float):
        if self.is_in_position(dest) or time == 0:
            return

        distance = self.calc_distance_to(dest)
        calc_time = self.calc_time(distance)
        if time >= calc_time:
            self._position = dest._position
            return

        diff_x_diff_t = (dest._position[0] - self._position[0]) / calc_time
        diff_y_diff_t = (dest._position[1] - self._position[1]) / calc_time
        new_x = self._position[0] + diff_x_diff_t * time
        new_y = self._position[1] + diff_y_diff_t * time
        self._position = new_x, new_y

    def is_in_position(self, dest: Essence) -> bool:
        return self.calc_distance_to(dest) <= self.__in_position_radius
