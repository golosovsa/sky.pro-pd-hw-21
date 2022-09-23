import pytest
from implement import Courier
from implement.base import Storage, MobileEssence


class TestCourier:

    def test_type(self):
        courier = Courier("name", (0, 0), 1, 20)
        assert courier.type == "Courier"
        assert issubclass(Courier, Storage)
        assert issubclass(Courier, MobileEssence)
