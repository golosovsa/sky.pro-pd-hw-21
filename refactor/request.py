"""
    class Request
"""

from refactor.abstract import Storage

class Request:

    def __init__(self, where: Storage, dest: Storage, amount: int, product: str):
        self.where = where
        self.dest = dest
        self.amount = amount
        self.product = product

    @classmethod
    def init(cls, storages: dict[str, Storage], query: str) -> "Request":
        pass

    def execute(self) -> tuple[int, int, int]:
        took = self.where.remove(product=self.product, amount=self.amount)
        delivered = self.dest.add(product=self.product, amount=took)
        returned = took - delivered
        self.where.add(product=self.product, amount=returned)
        return took, delivered, returned
