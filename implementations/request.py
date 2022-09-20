"""
    class implementation Request
"""
import re

import abstract
from base import Essence
from .errors import RequestError


class Request(abstract.Request):

    def __init__(self, where: Essence, dest: Essence, product: str, amount: int):
        self._where = where
        self._dest = dest
        self._product = product
        self._amount = amount
        self._was_sent = 0

        if product is None or product == "":
            raise RequestError("Request init error. Empty product detected.")
        if amount <= 0:
            raise RequestError("Request init error. Empty amount detected.")

    @staticmethod
    def create(world, query: str) -> "Request":
        re_pattern = r"(?P<amount>\d+) (?P<product>\w+) (from|из) (?P<where>\w+) (to|в) (?P<dest>\w+)"
        matches = re.search(re_pattern, query)
        if matches is None:
            raise RequestError("Request parsing error. Wrong query.")
        result = matches.groupdict()
        amount = int(result.get("amount"))
        product = result.get("product")
        where = world.get_essence(result.get("where"))
        dest = world.get_essence(result.get("dest"))
        if where is None:
            raise RequestError("Request parsing error. The essence 'from' does not exist in the world.")
        if dest is None:
            raise RequestError("Request parsing error. The essence 'to' does not exist in the world.")

        return Request(where, dest, product, amount)

    def update(self, world):
        pass

    @property
    def progress(self) -> float:
        pass
