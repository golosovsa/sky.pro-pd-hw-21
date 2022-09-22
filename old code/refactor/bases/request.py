"""
    Base implement of class Request
"""

from refactor import abstract
import re
from city import BaseCity
from storage import BaseStorage


class BaseRequest(abstract.Request):

    def __int__(self, where: BaseStorage, dest: BaseStorage, product: str, amount: int):
        self._where = where
        self._dest = dest
        self._product = product
        self._amount = amount

    @property
    def where(self) -> str:
        return str(self._where)

    @property
    def dest(self) -> str:
        return str(self._dest)

    @property
    def product(self) -> str:
        return self.product

    @property
    def amount(self) -> int:
        return self.amount

    @classmethod
    def create(cls, city: BaseCity, query: str) -> "BaseRequest":
        re_pattern = r"^.+(:?P<amount>\d+) (:?P<product>\w+) из (:?P<where>\w+) в (:?P<dest>\w+)"
        matches = re.search(re_pattern, query)
        if matches is None:
            return None
        where = city.get_place(matches.group("where"))
        dest = city.get_place(matches.group("dest"))
        product = str(matches.group("product"))
        amount = int(matches.group("amount"))
        return BaseRequest(where, dest, product, amount)

    def execute(self):
        pass
