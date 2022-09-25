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

    def __str__(self):
        return f"Transport {self._amount} {self._product} from {self._where.name} to {self._dest.name}"

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
        world.log("Search nearest free courier...")
        performer: Courier = world.get_the_nearest_free_courier(self._where)
        if performer is None:
            world.log("Courier not found")
            return

        world.log(f"Founded courier with name {performer.name}")
        performer_free = performer.get_free_space()
        where_count = self._where.get_one(self._product)
        deliver_count = self._amount - self._delivered
        amount = min(deliver_count, performer_free, where_count)

        world.log(f"{performer.name} can take {performer_free} of {self._product}")
        world.log(f"{self._where.name} contains {where_count} of {self._product}")
        world.log(f"Left to deliver {deliver_count} of {self._product}")

        if amount <= 0:
            world.log("Delivery is not possible")
            return

        reserved = self._dest.reserve(self._product, amount)

        world.log(f"{self._dest.name} can reserve {reserved} of {self._product}")

        if reserved <= 0:
            world.log("Delivery is not possible")
            return

        world.mark_as_busy(performer)

        self._where.remove(self._product, reserved)
        performer.add(self._product, reserved)
        task = Task(self._where, self._dest, performer)
        self._tasks.append(task)
        self._delivered += reserved

        world.log("A new task has been created")

    def _task_completed(self, world, task):
        amount = task.performer.get_one(self._product)
        task.performer.remove(self._product, amount)
        self._dest.apply_reservation(self._product, amount)

        world.mark_as_free(task.performer)

    def update(self, world):
        world.log(f"Request '{self.__str__()}' updating...")
        self._create_task(world)
        tasks: list[Task] = []
        for task in self._tasks:
            task.update()
            world.log(str(task))
            if task.status == "completed":
                self._task_completed(world, task)
                continue
            tasks.append(task)
        self._tasks = tasks
        world.log(f"The request '{self.__str__()}' was completed by {self.progress:.2f}%")


