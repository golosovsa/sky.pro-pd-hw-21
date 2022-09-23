import pytest
from implement.base import Essence, MobileEssence


class TestMobileEssence:

    def test_constructor(self):
        MobileEssence(name="name", position=(0.5, 10), speed=1)

    def test_constructor_failed(self):
        with pytest.raises(AssertionError):
            MobileEssence(name="name", position=(0.5, 10), some_param=1)
        with pytest.raises(AssertionError):
            MobileEssence(name="name", position=(0.5, 10), speed="1")
        with pytest.raises(AssertionError):
            MobileEssence(name="name", position=(0.5, 10), speed=-0.5)

    def test_calc_time(self):
        mobile = MobileEssence(name="mobile", position=(0, 0), speed=5)
        assert abs(mobile.calc_time(10) - 2) < 0.001

    def test_update_position_to(self):
        mobile = MobileEssence(name="mobile", position=(0, 0), speed=5)
        static = Essence(name="static", position=(50, 50))
        distance = mobile.calc_distance_to(static)
        full_time = mobile.calc_time(distance)
        mobile.update_position_to(static, full_time / 2)
        assert abs(mobile.position[0] - 25) < 0.001
        assert abs(mobile.position[1] - 25) < 0.001

    def test_is_in_position(self):
        mobile = MobileEssence(name="mobile", position=(0, 0), speed=5)
        static1 = Essence(name="static1", position=(0, 4))
        static2 = Essence(name="static2", position=(0, 6))

        assert mobile.is_in_position(static1)
        assert not mobile.is_in_position(static2)

    def test_type(self):
        mobile = MobileEssence(name="mobile", position=(0, 0), speed=5)
        assert mobile.type == "Mobile Essence"

