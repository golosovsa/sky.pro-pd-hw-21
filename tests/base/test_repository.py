import pytest
from implement.base import Repository


bad_values = [1.25, 1 - 3j, "str", (1, 2, 3), [1, 2, 3], {1: 2, 3: 4}, object]
bad_keys = [1, 1.25, 1 - 3j, (1, 2, 3), [1, 2, 3], {1: 2, 3: 4}, object]


class TestRepository:

    def test_constructor(self):
        assert Repository()
        assert Repository(number=123, string="123")

    def test_constructor_failed(self):
        with pytest.raises(TypeError):
            assert Repository(123)
        with pytest.raises(TypeError):
            assert Repository(123, "123")
        with pytest.raises(TypeError):
            assert Repository(123, string="123")

    def test_add(self):
        rep = Repository()
        rep.add("key1", 1)
        rep.add("key2", 2)
        assert "key1" in rep._items
        assert "key2" in rep._items
        assert rep._items["key1"] == 1
        assert rep._items["key2"] == 2

    @pytest.mark.parametrize("key", bad_keys)
    @pytest.mark.parametrize("value", bad_values)
    def test_add_failed(self, key, value):
        rep = Repository()
        with pytest.raises(AssertionError):
            rep.add(key, value)

    def test_remove(self):
        rep = Repository()
        rep.add("key", 100)
        rep.remove("key", 50)
        assert "key" in rep._items
        assert rep._items["key"] == 50
        rep.remove("key", 100)
        assert "key" not in rep._items
        rep.remove("key", 50)

    @pytest.mark.parametrize("key", bad_keys)
    @pytest.mark.parametrize("value", bad_values)
    def test_remove_failed(self, key, value):
        rep = Repository()
        with pytest.raises(AssertionError):
            rep.add(key, value)

    def test_get_one(self):
        rep = Repository()