import pytest
from implement.base import RedundantStorage


class TestRedundantStorage:

    def test_constructor(self):
        RedundantStorage(capacity=20)

    def test_constructor_failed(self):
        with pytest.raises(TypeError):
            RedundantStorage(20)
        with pytest.raises(AssertionError):
            RedundantStorage(some_param=20)
        with pytest.raises(AssertionError):
            RedundantStorage(capacity=0)
        with pytest.raises(AssertionError):
            RedundantStorage(capacity=-500)

    def test_reserve(self):
        redundant_storage = RedundantStorage(capacity=20)
        redundant_storage.add("key1", 5)
        redundant_storage.add("key2", 5)
        reserved = redundant_storage.reserve("key3", 20)
        assert reserved == 10
        assert redundant_storage.get_free_space() == 0
        added = redundant_storage.add("key4", 1)
        assert added == 0
        assert "key4" not in redundant_storage

    def test_apply_reservation(self):
        redundant_storage = RedundantStorage(capacity=20)
        redundant_storage.add("key1", 5)
        redundant_storage.add("key3", 5)
        reserved = redundant_storage.reserve("key3", 20)
        assert reserved == 10
        assert redundant_storage.get_free_space() == 0
        added = redundant_storage.add("key4", 1)
        assert added == 0
        assert "key4" not in redundant_storage
        applied = redundant_storage.apply_reservation("key3", 10)
        assert applied == 10
        assert "key3" in redundant_storage
        assert redundant_storage.get_one("key3") == 15

    def test_get_free_space(self):
        redundant_storage = RedundantStorage(capacity=20)
        redundant_storage.add("key1", 5)
        redundant_storage.reserve("key2", 5)
        redundant_storage.reserve("key3", 5)
        assert redundant_storage.get_free_space() == 5

