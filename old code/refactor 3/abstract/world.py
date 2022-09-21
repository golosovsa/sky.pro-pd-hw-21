"""
    Abstract class World
"""

from abc import ABC, abstractmethod
from .essence import Essence


class World(ABC):

    @abstractmethod
    def add_essence(self, essence: Essence):
        pass

    @abstractmethod
    def add_essences_from_json(self, json):
        pass

    @abstractmethod
    def add_request(self, query: str):
        pass

    @abstractmethod
    def add_requests_from_json(self, json):
        pass

    @abstractmethod
    def get_essence(self):
        pass

    @abstractmethod
    def get_nearest_mobile_essence(self):
        pass

    @abstractmethod
    def register_task(self, task, parent):
        pass

    @abstractmethod
    async def run(self):
        pass
