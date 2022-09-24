import pytest
from implement.base import Essence


class TestEssence:

    def test_constructor(self):
        Essence(name="name1", position=(5, 0.5))

    def test_constructor_failed(self):
        with pytest.raises(TypeError):
            Essence("name", (5, 0.5))
        with pytest.raises(TypeError):
            Essence("name", position=(5, 0.5))
        with pytest.raises(AssertionError):
            Essence(name=123, position=(5, 0.5))
        with pytest.raises(AssertionError):
            Essence(name="", position=(5, 0.5))
        with pytest.raises(AssertionError):
            essence1 = Essence(name="name", position=(5, 0.5))
            essence2 = Essence(name="name", position=(5, 0.5))
        with pytest.raises(AssertionError):
            Essence(name="name", position="(5, 0.5)")
        with pytest.raises(AssertionError):
            Essence(name="name", position=(5, ))
        with pytest.raises(AssertionError):
            Essence(name="name", position=(5, 0.5, 5.5))
        with pytest.raises(AssertionError):
            Essence(name="name", position=(5, True))

    def test_type(self):
        essence = Essence(name="name", position=(5, 0.5))
        assert essence.type == "Essence"

    def test_name(self):
        essence = Essence(name="name", position=(5, 0.5))
        assert essence.name == "name"
        with pytest.raises(AttributeError):
            essence.name = "new name"

    def test_position(self):
        essence = Essence(name="name", position=(5, 0.5))
        assert essence.position == (5, 0.5)
        with pytest.raises(AttributeError):
            essence.position = (0.5, 5)

    def test_calc_distance(self):
        essence1 = Essence(name="name1", position=(0, 0))
        essence2 = Essence(name="name2", position=(0, 5))
        essence3 = Essence(name="name3", position=(5, 0))

        assert abs(Essence.calc_distance(essence1, essence2)) - 5.0 < 0.001
        assert abs(Essence.calc_distance(essence1, essence3)) - 5.0 < 0.001
        assert abs(Essence.calc_distance(essence2, essence3)) - 7.071 < 0.01

    def test_calc_distance_to(self):
        essence1 = Essence(name="name1", position=(0, 0))
        essence2 = Essence(name="name2", position=(0, 5))
        essence3 = Essence(name="name3", position=(5, 0))

        assert abs(essence3.calc_distance_to(essence1) - 5.0) < 0.001
        assert abs(essence3.calc_distance_to(essence2) - 7.071) < 0.001
