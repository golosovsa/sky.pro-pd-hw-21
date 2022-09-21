"""
    class implementation Request
"""
import re

import abstract
from implementation import ReservationStorage
from .errors import RequestError
from .task import Task


class Request(abstract.Request):

    def __init__(self, where: ReservationStorage, dest: ReservationStorage, product: str, amount: int):
        if not isinstance(where, ReservationStorage):
            raise RequestError("Request init error. Wrong 'where' type.")
        if not isinstance(dest, ReservationStorage):
            raise RequestError("Request init error. Wrong 'dest' type.")
        if not isinstance(product, str) or product == "":
            raise RequestError("Request init error. Wrong 'product' detected.")
        if not isinstance(amount, int) or amount <= 0:
            raise RequestError("Request init error. Wrong 'amount' detected.")

        self._where = where
        self._dest = dest
        self._product = product
        self._amount = amount
        self._was_sent = 0

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
        if self.is_done:
            return

        mobile = world.get_nearest_mobile_essence()
        if mobile is None:
            return

        amount = min(self._amount - self._was_sent, mobile.get_free_space())
        reserve = self._dest.reserve(self._product, amount)
        taken = self._where.remove(self._product, reserve)
        mobile.add(self._product, taken)
        task = Task(self._where, self._dest, mobile)
        self._was_sent += taken
        world.register_task(task, self)

    def task_completed(self, task: Task):
        cargo = task.performer.get_items()
        if self._product not in cargo:
            raise RequestError("Request callback error. Wrong product")
        amount = cargo[self._product]
        taken = task.performer.remove(self._product, amount)
        task.dest.apply_reservation(self._product, taken)

    @property
    def progress(self) -> float:
        return 100 * self._was_sent / self._amount

    @property
    def is_done(self) -> bool:
        return self._was_sent >= self._amount
