"""
    base class implement Repository
"""

import abstract


class Repository(abstract.Repository):

    def __init__(self, **kwargs):
        self._items: dict[str, int] = {}

    def add(self, key: str, count: int):
        assert type(key) == str, "key must be str"
        assert type(count) == int, "count must be int"
        if key in self._items:
            self._items[key] += count
        else:
            self._items[key] = count

    def remove(self, key: str, count: int):
        assert type(key) == str, "key must be str"
        assert type(count) == int, "count must be int"
        if key not in self._items:
            return
        self._items[key] -= count
        if self._items[key] <= 0:
            del self._items[key]

    def get_one(self, key: str):
        assert type(key) == str, "key must be str"
        return self._items.get(key, 0)

    def get_all(self) -> dict[str, int]:
        return self._items.copy()

    def __contains__(self, key: str) -> bool:
        assert type(key) == str, "key must be str"
        return key in self._items
