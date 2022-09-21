"""
    class implementation World
"""

import abstract
from implementation import Storage, ReservationStorage as Static
from .request import Request
from .task import Task
from .errors import WorldError


class World(abstract.World):

    def __init__(self):
        self._essences: dict[str, dict[str, Storage]] = {}
        self._requests: list[Request] = []
        self._tasks: list[Task] = []

    def add_essence(self, essence: Storage):
        essence_type = essence.type()
        if essence_type not in self._essences:
            self._essences[essence_type]: dict[str, Storage] = {}
        essence_name = essence.name
        if essence_name in self._essences[essence_type]:
            raise WorldError("Add essence error. Already exist.")
        self._essences[essence_type][essence_name] = essence

    def add_essences_from_json(self, json):
        for essence in json:
            essence = Static()

    def add_request(self, query: str):
        pass

    def add_requests_from_json(self, json):
        pass

    def get_essence(self):
        pass

    def get_nearest_mobile_essence(self):
        pass

    def register_task(self, task, parent):
        pass

    async def run(self):
        pass
