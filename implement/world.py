"""
    Implementation of Warehouse
"""

import abstract
from . import Warehouse, Shop, Courier, Request


class World(abstract.World):

    __essences_types = {
        Warehouse.type: Warehouse,
        Shop.type: Shop,
        Courier.type: Courier
    }

    def __init__(self):
        self._static_essences: dict[str, Warehouse | Shop] = {}
        self._dynamic_essences: dict[str, Courier] = {}
        self._busy_essences: list[str] = []
        self._requests: list[Request] = []

    def _add_essence(self, essence: Warehouse | Shop | Courier | None):
        if essence is None:
            return
        match essence.type:
            case Warehouse.type | Shop.type:
                self._static_essences[essence.name] = essence
            case Courier.type:
                self._dynamic_essences[essence.name] = essence

    def _create_essence(self, data):

