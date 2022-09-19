"""
    Base implementation of class City
"""

from refactor import abstract
from essence import BaseEssence


class BaseCity(abstract.City):
    def __init__(self):
        self._places: dict[str, BaseEssence] = {}
        self._couriers: dict[str, BaseEssence] = {}

    @property
    def places(self) -> dict[str, BaseEssence]:
        return self._places.copy()

    @property
    def couriers(self) -> dict[str, object]:
        return self._couriers.copy()

    def get_place(self, name) -> object:
        return self._places.get(name)

    def get_courier(self, place) -> object:
        pass

    def add_place(self, place):
        pass

    def add_courier(self, courier):
        pass