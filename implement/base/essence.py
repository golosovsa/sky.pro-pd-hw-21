"""
    base class implement Essence
"""
from math import sqrt, pow
import abstract


class Essence(abstract.Essence):

    _type: str = "Essence"
    __names: list[str] = []

    def __init__(self, **kwargs):
        assert "name" in kwargs, "Missing required parameter name"
        assert type(kwargs["name"]) == str, "Required parameter name must be a str"
        assert kwargs["name"] != "", "Required parameter name cannot be empty"
        assert kwargs["name"] not in Essence.__names, "Required parameter name cannot be repeated"
        assert "position" in kwargs, "Missing required parameter position"
        assert type(kwargs["position"]) in {tuple, list}, "Required parameter position must be a tuple or a list"
        assert len(kwargs["position"]) == 2, "Required parameter position must must consist of 2 elements"
        assert type(kwargs["position"][0]) in {float, int}, "First element of required parameter position " \
                                                            "must be a float or an int"
        assert type(kwargs["position"][1]) in {float, int}, "Second element of required parameter position " \
                                                            "must be a float or an int"
        self.__names.append(kwargs["name"])
        self._name = kwargs["name"]
        self._position = tuple(kwargs["position"])

    def __del__(self):
        if self._name in self.__names:
            self.__names.remove(self._name)

    @classmethod
    @property
    def type(cls) -> str:
        return cls._type

    @property
    def name(self) -> str:
        return self._name

    @property
    def position(self) -> tuple[float, float]:
        return self._position

    @staticmethod
    def calc_distance(where: "Essence", dest: "Essence") -> float:
        where_x, where_y = where.position
        dest_x, dest_y = dest.position
        return sqrt(
            pow(dest_x - where_x, 2) +
            pow(dest_y - where_y, 2)
        )

    def calc_distance_to(self, dest) -> float:
        return self.calc_distance(self, dest)
