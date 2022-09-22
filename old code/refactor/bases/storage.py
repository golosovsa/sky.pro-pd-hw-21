"""
    Base implement of class Storage
"""

from refactor import abstract


class BaseStorage(abstract.Storage):

    _type = "Base"

    def __init__(self, capacity):
        self.__items: dict[str, int] = {}
        self.__reserved: dict[str, int] = {}
        self.__capacity = capacity

    @property
    def type(self) -> str:
        return self._type

    @property
    def items(self) -> dict[str, int]:
        return self.__items.copy()

    @property
    def capacity(self) -> int:
        return self.__capacity

    def add(self, product: str, amount: int):
        amount = min(amount, self.get_free_space())
        if amount <= 0:
            return 0

        self.__items[product] = amount
        return amount

    def remove(self, product: str, amount: int):
        if product not in self.__items:
            return 0

        amount = min(self.__items[product], amount)
        self.__items[product] = amount
        if amount <= 0:
            del self.__items[product]

        return amount

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_unique_items_count(self) -> int:
        return len(self.__items)
