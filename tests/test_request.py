import pytest
from time import sleep
from implement import World, Request, Warehouse, Shop, Courier, CreateRequestError


class TestRequest:

    def test_create(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        courier = Courier("courier", (0, 0))
        items = {
            "product1": 5,
            "product2":  3
        }
        World._fill_essence(warehouse, items)
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier)

        request = Request.create(world, "text 3 product1 from warehouse to shop")
        assert request

    def test_create_failed(self):
        world = World()
        with pytest.raises(AssertionError):
            Request.create(world, "text 3 product1 from warehouse to shop")
            Request.create(world, "abra ka dabra")

    def test_progress(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        courier = Courier("courier", (0, 0), 10)
        items = {
            "product1": 5,
            "product2": 3
        }
        World._fill_essence(warehouse, items)
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier)
        request = Request.create(world, "text 3 product1 from warehouse to shop")
        request.update(world)
        sleep(1)
        request.update(world)
        sleep(1)
        request.update(world)
        assert abs(request.progress - 66.667) < 0.001

    def test_is_done(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        courier = Courier("courier", (0, 0), 10, 10)
        items = {
            "product1": 5,
            "product2": 3
        }
        World._fill_essence(warehouse, items)
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier)
        request = Request.create(world, "text 5 product1 from warehouse to shop")
        assert not request.is_done
        request.update(world)
        sleep(1)
        assert not request.is_done
        request.update(world)
        sleep(1)
        assert request.is_done

    def test_create_task(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        courier = Courier("courier", (0, 0), 10, 10)
        items = {
            "product1": 5,
            "product2": 3
        }
        World._fill_essence(warehouse, items)
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier)
        request = Request.create(world, "text 5 product1 from warehouse to shop")
        request.update(world)

        assert len(request._tasks) == 1
        assert request._tasks[0]._where == warehouse
        assert request._tasks[0]._dest == shop
        assert request._tasks[0].performer == courier
        assert courier.get_all() == {"product1": 5}

    def test_task_completed(self):
        world = World()
        warehouse = Warehouse("warehouse", (0, 1))
        shop = Shop("shop", (0, 2))
        courier = Courier("courier", (0, 0), 10, 10)
        items = {
            "product1": 5,
            "product2": 3
        }
        World._fill_essence(warehouse, items)
        world._add_essence(warehouse)
        world._add_essence(shop)
        world._add_essence(courier)
        request = Request.create(world, "text 5 product1 from warehouse to shop")
        assert not request.is_done
        request.update(world)
        assert request._tasks
        task = request._tasks[0]
        request._task_completed(world, task)
        assert task.performer.name not in world._busy_essences

