"""
    Abstract class Essence
"""

from abc import ABC, abstractmethod


class World(ABC):

    __essence_types: dict[str, type] = NotImplemented
    _static_essences: dict[str, object] = NotImplemented
    _dynamic_essences: dict[str, object] = NotImplemented
    _busy_essences: list[str] = NotImplemented
    _requests: list[object] = NotImplemented

    @abstractmethod
    def _add_essence(self, essence):
        pass

    @staticmethod
    @abstractmethod
    def _fill_essence(essence, items):
        pass

    @abstractmethod
    def _append_essence(self, **kwargs):
        pass

    @abstractmethod
    def append_request(self, query):
        pass

    @abstractmethod
    def get_static_essence_by_name(self, name):
        pass

    @staticmethod
    @abstractmethod
    def _print_error(error, obj):
        pass

    @staticmethod
    @abstractmethod
    def create_from_dict(data):
        pass

    @staticmethod
    @abstractmethod
    def create_from_json_file(filename):
        pass

    @abstractmethod
    def get_the_nearest_free_courier(self, essence):
        pass

    @abstractmethod
    def mark_as_busy(self, essence):
        pass

    @abstractmethod
    def mark_as_free(self, essence):
        pass

    @abstractmethod
    def compute_all_requests(self):
        pass

    @staticmethod
    @abstractmethod
    def log(*args, **kwargs):
        pass
