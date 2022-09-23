import pytest
from implement import Warehouse
from implement.base import RedundantStorage, Essence


class TestWarehouse:

    def test_type(self):
        warehouse = Warehouse("name", (5, 5), 20)
        assert warehouse.type == "Warehouse"
        assert issubclass(Warehouse, RedundantStorage)
        assert issubclass(Warehouse, Essence)
