"""
    Abstract class Essence
"""

from abc import ABC, abstractmethod


class World(ABC):

    @property
    @abstractmethod
    def __essence_types(self) -> dict[str, type]:
        pass

    @abstractmethod
    def register_essence_type(self, essence_type):
        pass

    @property
    @abstractmethod
    def _essences(self) -> dict[str, dict[str, object]]:
        pass

    @abstractmethod
    def add_essence(self, essence):
        pass

    @abstractmethod
    def _get_essence(self, type_of, name):
        pass

    @abstractmethod
    def get_storage(self, name):
        pass

    @abstractmethod
    def get_courier(self, name):
        pass

    @abstractmethod
    def get_nearest_free_courier(self, where):
        pass

    @property
    @abstractmethod
    def __tasks(self) -> list:
        pass

    @abstractmethod
    def add_task(self, task):
        pass

    @property
    @abstractmethod
    def __requests(self) -> list:
        pass

    @abstractmethod
    def add_request(self, query):
        pass

    @staticmethod
    @abstractmethod
    def create_from_json(data):
        pass

    @abstractmethod
    async def run(self):
        pass
