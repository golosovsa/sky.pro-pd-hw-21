"""
    Base class implement ProtectedRepository
"""

import abstract


class ProtectedRepository(abstract.ProtectedRepository):
    """ Base implement """

    def __init__(self):
        self._data: dict[str, int] = {}

    def __contains__(self, key: str):
        return key in self._data

    def _add(self, key, count):
        if count == 0:
            return

        if key in self._data:
            self._data[key] += count
        else:
            self._data[key] = count

    def _remove(self, key, count):
        if key not in self._data or count == 0:
            return

        self._data[key] -= count
        if self._data[key] <= 0:
            del self._data[key]

    def _get_one(self, key):
        return self._data.get(key, 0)

    def _get_all(self):
        return self._data.copy()
