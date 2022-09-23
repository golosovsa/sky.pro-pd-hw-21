import pytest
from implement.base import Storage


class TestStorage:

    def test_constructor(self):
        assert Storage(capacity=10)

    def test_constructor_failed(self):
        with pytest.raises(AssertionError):
            Storage()
        with pytest.raises(AssertionError):
            Storage(some_param=20)
        with pytest.raises(AssertionError):
            Storage(capacity="20")
        with pytest.raises(AssertionError):
            Storage(capacity=-10)
        with pytest.raises(AssertionError):
            Storage(capacity=0)

        with pytest.raises(TypeError):
            Storage(20)
        with pytest.raises(TypeError):
            Storage("20")

    def test_capacity(self):
        storage = Storage(capacity=20)
        assert type(storage.capacity) == int
        assert storage.capacity == 20

    def test_get_free_space(self):
        storage = Storage(capacity=20)
        assert type(storage.get_free_space()) == int
        assert storage.get_free_space() == 20
        storage.add("p1", 3)
        storage.add("p2", 3)
        storage.add("p3", 3)
        assert storage.get_free_space() == 20 - 3 - 3 - 3

    def test_get_items(self):
        storage = Storage(capacity=20)
        storage.add("p1", 3)
        storage.add("p2", 3)
        storage.add("p3", 3)
        assert storage.get_items() == {"p1": 3, "p2": 3, "p3": 3}

    def test_get_unique_items_count(self):
        storage = Storage(capacity=20)
        storage.add("p1", 5)
        storage.add("p2", 5)
        storage.add("p3", 5)
        assert storage.get_unique_items_count() == 3

    def test_add(self):
        storage = Storage(capacity=20)
        added = storage.add("p1", 5)
        assert added == 5
        assert "p1" in storage
        assert storage.get_one("p1") == 5
        added = storage.add("p1", 25)
        assert added == 15
        assert storage.get_one("p1") == 20
        assert storage.get_free_space() == 0
        added = storage.add("p2", 1)
        assert added == 0
        assert "p2" not in storage

    def test_remove(self):
        storage = Storage(capacity=20)
        storage.add("p1", 5)
        storage.add("p2", 5)
        storage.add("p3", 5)
        removed = storage.remove("p1", 4)
        assert removed == 4
        assert "p1" in storage
        assert storage.get_one("p1") == 1
        removed = storage.remove("p1", 100)
        assert removed == 1
        assert "p1" not in storage
        assert storage.get_free_space() == 10
