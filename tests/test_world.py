import pytest
from implement import World, Warehouse, Shop, Courier, Request, CreateRequestError


class TestWorld:

    def test_add_essence(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        courier = Courier("courier", (0, 0))
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier)

        assert len(world._static_essences) == 2
        assert len(world._dynamic_essences) == 1
        assert "warehouse" in world._static_essences
        assert id(warehouse) == id(world._static_essences["warehouse"])
        assert "shop" in world._static_essences
        assert id(shop) == id(world._static_essences["shop"])
        assert "courier" in world._dynamic_essences
        assert id(courier) == id(world._dynamic_essences["courier"])

    def test_fill_essence(self):
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        items = [
            {
                "product": "product1",
                "amount": 5
            },
            {
                "product": "product2",
                "amount": 3
            }
        ]
        World._fill_essence(warehouse, items)
        World._fill_essence(shop, items)

        assert warehouse.get_all() == {"product1": 5, "product2": 3}
        assert shop.get_all() == {"product1": 5, "product2": 3}

    def test_fill_essence_failed(self):
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        items = [
            {
                "product": "",
                "amount": "5"
            },
            {
                "product": 123,
                "amount": -30
            }
        ]
        with pytest.raises(AssertionError):
            World._fill_essence(warehouse, items)
            World._fill_essence(shop, items)

    def test_append_request(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        courier = Courier("courier", (0, 0))
        items = [
            {
                "product": "product1",
                "amount": 5
            },
            {
                "product": "product2",
                "amount": 3
            }
        ]
        World._fill_essence(warehouse, items)
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier)

        world._append_request("text 3 product1 from warehouse to shop")

        assert len(world._requests) == 1
        assert type(world._requests[0]) == Request

    def test_append_request_failed(self):
        world = World()
        with pytest.raises(CreateRequestError):
            world._append_request("text 3 product1 from warehouse to shop")
            world._append_request("bla-bla-bla")
            world._append_request(100500)

    def test_get_static_essence_by_name(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 0))
        shop = Shop("shop", (0, 0))
        courier1 = Courier("courier1", (0, 100))
        courier2 = Courier("courier2", (50, 0))
        courier3 = Courier("courier3", (10, 10))
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier1)
        world._add_essence(courier2)
        world._add_essence(courier3)

        assert id(world.get_static_essence_by_name("warehouse")) == id(warehouse)
        assert id(world.get_static_essence_by_name("shop")) == id(shop)

    def test_get_the_nearest_free_courier(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 0))
        shop = Shop("shop", (0, 0))
        courier1 = Courier("courier1", (0, 100))
        courier2 = Courier("courier2", (50, 0))
        courier3 = Courier("courier3", (10, 10))
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier1)
        world._add_essence(courier2)
        world._add_essence(courier3)

        assert id(courier3) == id(world.get_the_nearest_free_courier(warehouse))
        world.mark_as_busy(courier3)
        assert id(courier2) == id(world.get_the_nearest_free_courier(warehouse))

    def test_mark_as_busy_and_mark_as_free(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 0))
        shop = Shop("shop", (0, 0))
        courier1 = Courier("courier1", (0, 100))
        courier2 = Courier("courier2", (50, 0))
        courier3 = Courier("courier3", (10, 10))
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier1)
        world._add_essence(courier2)
        world._add_essence(courier3)

        world.mark_as_busy(courier2)
        world.mark_as_busy(courier3)
        assert courier1.name not in world._busy_essences
        assert courier2.name in world._busy_essences
        assert courier3.name in world._busy_essences
        world.mark_as_free(courier2)
        world.mark_as_free(courier3)
        assert courier1.name not in world._busy_essences
        assert courier2.name not in world._busy_essences
        assert courier3.name not in world._busy_essences
