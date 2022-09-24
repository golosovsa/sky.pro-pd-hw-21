"""
    Implementation of Request
"""

import re
import abstract
from .task import Task
from .warehouse import Warehouse
from .shop import Shop
from .courier import Courier


class Request(abstract.Request):

    def __init__(self, where: Warehouse | Shop, dest: Warehouse | Shop, product: str, amount: int):
        self._where = where
        self._dest = dest
        self._product = product
        self._amount = amount
        self._delivered: int = 0
        self._tasks: list[Task] = []

    @staticmethod
    def create(world: abstract.World, query):
        re_pattern = r"(?P<amount>\d+) (?P<product>\w+) (из|from) (?P<where>\w+) (в|to) (?P<dest>\w+)"
        match = re.search(re_pattern, query)
        assert match, "Query parsing error"
        result = match.groupdict()
        amount = int(result["amount"])
        product = result["product"]
        where = world.get_static_essence_by_name(result["where"])
        dest = world.get_static_essence_by_name(result["dest"])
        assert where, "Essence where not found"
        assert dest, "Essence dest not found"
        request = Request(where, dest, product, amount)
        return request

    @property
    def progress(self) -> float:
        return 100 * self._delivered / self._amount

    @property
    def is_done(self) -> bool:
        return self._delivered >= self._amount and len(self._tasks) == 0

    def _create_task(self, world: abstract.World):
        if self._delivered >= self._amount:
            return

        performer: Courier = world.get_the_nearest_free_courier(self._where)
        if performer is None:
            return

        performer_free = performer.get_free_space()
        where_count = self._where.get_one(self._product)
        deliver_count = self._amount - self._delivered
        amount = min(deliver_count, performer_free, where_count)
        if amount <= 0:
            return

        reserved = self._dest.reserve(self._product, amount)
        if reserved <= 0:
            return

        world.mark_as_busy(performer)

        self._where.remove(self._product, reserved)
        performer.add(self._product, reserved)
        task = Task(self._where, self._dest, performer)
        self._tasks.append(task)
        self._delivered += reserved

    def _task_completed(self, world, task):
        amount = task.performer.get_one(self._product)
        task.performer.remove(self._product, amount)
        self._dest.apply_reservation(self._product, amount)

        world.mark_as_free(task.performer)

    def update(self, world):
        self._create_task(world)
        tasks: list[Task] = []
        for task in self._tasks:
            task.update()
            if task.status == "completed":
                self._task_completed(world, task)
                continue
            tasks.append(task)
        self._tasks = tasks


