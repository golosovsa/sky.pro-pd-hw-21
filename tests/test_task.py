import pytest

from time import sleep
from implement import Task
from implement.base import Essence, MobileEssence


class TestTask:

    def test_logic(self):
        performer = MobileEssence(name="performer", position=(0, 0), speed=250)
        where = Essence(name="where", position=(500, 0))
        dest = Essence(name="dest", position=(500, 500))
        task = Task(where, dest, performer)
        assert task.status == "wait_for_performer"
        sleep(2.5)
        task.update()
        assert task.status == "wait_for_delivery"
        sleep(2.5)
        task.update()
        assert task.status == "completed"
