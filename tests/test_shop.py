import pytest
from implement import Shop
from implement.base import UniqRedundantStorage, Essence


class TestShop:

    def test_type(self):
        shop = Shop("shop", (5, 5))
        assert shop.type == "Shop"
        assert issubclass(Shop, UniqRedundantStorage)
        assert issubclass(Shop, Essence)
