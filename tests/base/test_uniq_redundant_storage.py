import pytest
from implement.base import UniqRedundantStorage


class TestUniqRedundantStorage:

    def test_constructor(self):
        UniqRedundantStorage(capacity=20, uniq_capacity=50)

    def test_constructor_failed(self):
        with pytest.raises(TypeError):
            UniqRedundantStorage(20, 50)
        with pytest.raises(AssertionError):
            UniqRedundantStorage(capacity=20, some=50)
        with pytest.raises(AssertionError):
            UniqRedundantStorage(capacity=20, uniq_capacity="50")
        with pytest.raises(AssertionError):
            UniqRedundantStorage(capacity=20, uniq_capacity=-50)
        with pytest.raises(AssertionError):
            UniqRedundantStorage(capacity=20, uniq_capacity=0)

    def test_add(self):
        uniq_redundant_storage = UniqRedundantStorage(capacity=20, uniq_capacity=3)
        added = uniq_redundant_storage.add("key1", 5)
        assert added == 5
        assert "key1" in uniq_redundant_storage
        added = uniq_redundant_storage.add("key2", 5)
        assert added == 5
        assert "key2" in uniq_redundant_storage
        added = uniq_redundant_storage.add("key3", 5)
        assert added == 5
        assert "key2" in uniq_redundant_storage
        added = uniq_redundant_storage.add("key4", 5)
        assert added == 0
        assert "key4" not in uniq_redundant_storage
        reserved = uniq_redundant_storage.reserve("key4", 5)
        assert reserved == 0
        assert "key4" not in uniq_redundant_storage._redundant

    def test_get_free_space(self):
        uniq_redundant_storage = UniqRedundantStorage(capacity=20, uniq_capacity=3)
        uniq_redundant_storage.add("key1", 5)
        uniq_redundant_storage.add("key2", 5)
        assert uniq_redundant_storage.get_free_space() == 10
        uniq_redundant_storage.add("key3", 5)
        assert uniq_redundant_storage.get_free_space() == 0
        uniq_redundant_storage.remove("key3", 5)
        assert uniq_redundant_storage.get_free_space() == 10
        uniq_redundant_storage.reserve("key3", 5)
        assert uniq_redundant_storage.get_free_space() == 0



