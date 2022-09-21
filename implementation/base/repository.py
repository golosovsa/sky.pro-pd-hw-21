"""
    base class implementation Repository
"""

import abstract


class Repository(abstract.Repository):

    def __init__(self, **kwargs):
        self._items: dict[str, int] = {}


    def add(self, key: str, count: int):
        pass

    def remove(self, key: str, count: int):
        pass

    def get_one(self, key: str):
        pass

    def get_all(self):
        pass

    def __contains__(self, key: str):
        pass
