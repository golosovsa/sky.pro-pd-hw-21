"""
    Base class implementation Task
"""
import time

import abstract
from .essence import Essence
from .mobile_essence import MobileEssence


class Task(abstract.Task):

    _statuses: list[str] = ["wait_for_performer", "wait_for_delivery", "finished"]

    def __init__(self, where: Essence, dest: Essence, product: str, amount: int, performer: MobileEssence):
        self._where = where
        self._dest = dest
        self._product = product
        self._amount = amount
        self._performer = performer
        self._status_index: int = 0
        self._last_time: float = time.time()

    @property
    def where(self) -> Essence:
        return self._where

    @property
    def dest(self) -> Essence:
        return self._dest

    @property
    def product(self) -> str:
        return self._product

    @property
    def amount(self) -> int:
        return self.amount

    @property
    def performer(self) -> MobileEssence:
        return self._performer

    @property
    def status(self) -> str:
        return self._statuses[self._status_index]

    def update(self):
        status = self._statuses[self._status_index]
        if status == self._statuses[-1]:
            return

        method = getattr(self, f"_{status}")
        current_time = time.time()
        elapsed_time = current_time - self._last_time
        self._last_time = current_time
        method(elapsed_time)

    def __wait_for_essence(self, essence: Essence, elapsed_time: float):
        self._performer.update_position_to(essence, elapsed_time)
        if self._performer.is_in_position(essence):
            self._status_index += 1

    def _wait_for_performer(self, elapsed_time: float):
        self.__wait_for_essence(self._where, elapsed_time)

    def _wait_for_delivery(self, elapsed_time: float):
        self.__wait_for_essence(self._dest, elapsed_time)
