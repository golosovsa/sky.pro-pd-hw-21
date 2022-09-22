"""
    Base class implement Essence
"""
import math
import abstract


class Essence(abstract.Essence):

    def __init__(self, **kwargs):
        self._name = kwargs["name"]
        self._position = kwargs["position"]

    @property
    def name(self) -> str:
        return self._name

    @property
    def position(self) -> tuple[float, float]:
        return self._position[0], self._position[1]

    def calc_distance_to(self, essence: "Essence") -> float:
        return math.sqrt(
            math.pow(self._position[0] - essence._position[0], 2) +
            math.pow(self._position[1] - essence._position[1], 2)
        )
