"""
    class implement Task
"""
import time

import abstract
from implement import ReservationStorage, Essence
from implement import Mobile


class Task(abstract.Task):

    _statuses: list[str] = ["wait_for_performer", "wait_for_delivery", "finished"]

    def __init__(self,
                 where: ReservationStorage,
                 dest: ReservationStorage,
                 performer: Mobile):
        self._where = where
        self._dest = dest
        self._performer = performer
        self._status_index: int = 0
        self._last_time: float = time.time()

    @property
    def where(self) -> ReservationStorage:
        return self._where

    @property
    def dest(self) -> ReservationStorage:
        return self._dest

    @property
    def performer(self) -> Mobile:
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

    def __wait_for_essence(self, essence: Essence | ReservationStorage, elapsed_time: float):
        self._performer.update_position_to(essence, elapsed_time)
        if self._performer.is_in_position(essence):
            self._status_index += 1

    def _wait_for_performer(self, elapsed_time: float):
        self.__wait_for_essence(self._where, elapsed_time)

    def _wait_for_delivery(self, elapsed_time: float):
        self.__wait_for_essence(self._dest, elapsed_time)
