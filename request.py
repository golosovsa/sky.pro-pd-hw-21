"""
    class Request
"""

import re

from consts import REQUEST_RE_PATTERN
from storage import Storage
from store import Store
from shop import Shop


class Request:

    def __init__(self, where: Storage, dest: Storage, amount: int, product: str):
        self.where = where
        self.dest = dest
        self.amount = amount
        self.product = product

    @classmethod
    def init(cls, storages: dict[str, Storage], query: str) -> "Request":

        inverse_storage =

        matches = re.search(REQUEST_RE_PATTERN, query.lower())
        if matches is None:
            raise ValueError(f"Invalid query parameter (query={query}).")

        result = matches.groupdict()

        amount = int(result.get("amount"))
        product = result.get("product")
        where = result.get("where")
        dest = inverse_storage.get(where)

        print(where, dest)

        return Request(storages[where], storages[dest], amount, product)

    def execute(self) -> tuple[int, int, int]:
        took = self.where.remove(product=self.product, amount=self.amount)
        delivered = self.dest.add(product=self.product, amount=took)
        returned = took - delivered
        self.where.add(product=self.product, amount=returned)
        return took, delivered, returned

