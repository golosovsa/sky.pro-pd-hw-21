"""
    Implementation of Task
"""

from time import time

import abstract
from . import Warehouse, Shop, Courier


class Task(abstract.Task):

    _steps = ["wait_for_performer", "wait_for_delivery", "completed"]

    def __init__(self, where: Warehouse | Shop, dest: Warehouse | Shop, performer: Courier):
        self._where = where
        self._dest = dest
        self._performer = performer
        self._step_index = 0
        self._time = time()

    @property
    def performer(self) -> Courier:
        return self._performer

    @property
    def status(self) -> str:
        return self._steps[self._step_index]

    def __wait_for_essence(self, essence: Warehouse | Shop | Courier, elapsed_time: float):
        self._performer.update_position_to(essence, elapsed_time)
        if self._performer.is_in_position(essence):
            self._step_index += 1

    def _wait_for_performer(self, elapsed_time):
        self.__wait_for_essence(self._where, elapsed_time)

    def _wait_for_delivery(self, elapsed_time):
        self.__wait_for_essence(self._dest, elapsed_time)

    def update(self):
        if self._step_index == len(self._steps) - 1:
            return

        method = getattr(self, f"_{self._steps[self._step_index]}")
        current_time = time()
        elapsed_time = current_time - self._time
        self._time = current_time
        method(elapsed_time)

    def __str__(self):
        match self.status:
            case "wait_for_performer":
                distance = self._performer.calc_distance_to(self._where) + \
                           self._where.calc_distance_to(self._dest)
                estimated_time = self._performer.calc_time(distance)
                return f"Task for the {self._performer.name} " \
                       f"is in progress 'Wait for performer' " \
                       f"and will be completed in {estimated_time:.2f} seconds'"
            case "wait_for_delivery":
                distance = self._performer.calc_distance_to(self._dest)
                estimated_time = self._performer.calc_time(distance)
                return f"Task for the {self._performer.name} " \
                       f"is in progress 'Wait for delivery' " \
                       f"and will be completed in {estimated_time:.2f} seconds'"
            case "completed":
                return f"Task for the {self._performer.name} completed"
