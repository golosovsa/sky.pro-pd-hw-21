"""
    Implementation of Warehouse
"""

import json
import pathlib
import abstract
from .warehouse import Warehouse
from .shop import Shop
from .courier import Courier
from .request import Request
from .errors import CreateEssenceError, CreateRequestError


class World(abstract.World):

    __essences_types = {
        Warehouse.type: Warehouse,
        Shop.type: Shop,
        Courier.type: Courier
    }

    def __init__(self):
        self._static_essences: dict[str, Warehouse | Shop] = {}
        self._dynamic_essences: dict[str, Courier] = {}
        self._busy_essences: list[str] = []
        self._requests: list[Request] = []

    def _add_essence(self, essence: Warehouse | Shop | Courier | None):
        if essence is None:
            return
        match essence.type:
            case Warehouse.type | Shop.type:
                self._static_essences[essence.name] = essence
            case Courier.type:
                self._dynamic_essences[essence.name] = essence

    @staticmethod
    def _fill_essence(essence, items):
        for item in items:
            assert type(item) == dict, "Wrong type of item in contains items"
            assert "product" in item, "Missing required parameter product in contains items"
            assert "amount" in item, "Missing required parameter amount in contains items"
            assert type(item["product"]) == str, "Wrong type of required parameter product in contains items"
            assert type(item["amount"]) == int, "Wrong type of required parameter amount in contains items"
            assert item["product"] != "", "Wrong value of required parameter product in contains items"
            assert item["amount"] > 0, "Wrong value of required parameter amount in contains items"
            essence.add(item["product"], item["amount"])

    def _append_essence(self, **kwargs):
        try:
            assert "type" in kwargs, "Missing required parameter type"
            assert type(kwargs["type"]) == str, "Wrong type of required parameter type"
            essence_type = kwargs["type"]
            assert essence_type in self.__essences_types, "Unknown essence type"
            assert "settings" in kwargs, "Missing required parameter settings"
            assert type(kwargs["settings"]) == dict, "Wrong type of required parameter settings"

            essence = self.__essences_types[essence_type](**kwargs["settings"])
            if "contains" in kwargs:
                assert type(kwargs["contains"]) == list, "Wrong type of parameter contains"
                self._fill_essence(essence, kwargs["contains"])

            self._add_essence(essence)

        except (AssertionError, TypeError) as error:
            raise CreateEssenceError(str(error))

    def _append_request(self, query: str):
        try:
            assert type(query) == str, "Wrong type of parameter queries"
            request = Request.create(self, query)
            self._requests.append(request)
        except (AssertionError, TypeError) as error:
            raise CreateRequestError(str(error))

    @staticmethod
    def _print_error(error, obj):
        print("=" * 20, "ERROR", "=" * 20)
        print(str(error), end="\n\n")
        print(str(obj))
        print("=" * 47, end="\n\n")

    @staticmethod
    def create_from_dict(data) -> "World" or None:
        try:
            assert type(data) == dict, "Wrong type of data"
            assert "essences" in data, "Missing required parameter essences"
            assert type(data["essences"]) == list, "Wrong type of parameter essences"
            assert "requests" in data, "Missing required parameter requests"
            assert type(data["requests"]) == list, "Wrong type of parameter requests"

            world = World()

            for essence in data["essences"]:
                try:
                    world._append_essence(**essence)
                except CreateEssenceError as error:
                    World._print_error(error, essence)

            for query in data["requests"]:
                try:
                    world._append_request(query)
                except CreateRequestError as error:
                    World._print_error(error, query)

            essences_in_data = len(data["essences"])
            essences_has_appended = len(world._static_essences) + len(world._dynamic_essences)
            requests_in_data = len(data["requests"])
            requests_has_appended = len(world._requests)

            print("=" * 12, "The world was created", "=" * 12)
            print(f"Appended successfully {essences_has_appended} from {essences_in_data} essences")
            print(f"Appended successfully {requests_has_appended} from {requests_in_data} requests")
            print("=" * 47)
            return world

        except AssertionError as error:
            World._print_error(error, data)
            print("=" * 11, "The world wasn't created", "=" * 10)
            return None

    @staticmethod
    def create_from_json_file(filename):
        path = pathlib.Path(filename)
        with path.open("rt", encoding="utf-8") as fin:
            json_object = json.load(fin)
        return World.create_from_dict(json_object)

    def get_static_essence_by_name(self, name):
        return self._static_essences.get(name, None)

    def get_the_nearest_free_courier(self, essence: Warehouse | Shop):
        free_couriers = list(filter(
            lambda ess: ess.name not in self._busy_essences,
            self._dynamic_essences.values()
        ))
        if not free_couriers:
            return None
        courier = min(
            free_couriers,
            key=lambda ess: essence.calc_distance_to(ess)
        )
        return courier

    def mark_as_busy(self, essence: Courier):
        if essence.name not in self._busy_essences:
            self._busy_essences.append(essence.name)

    def mark_as_free(self, essence: Courier):
        if essence.name in self._busy_essences:
            self._busy_essences.remove(essence.name)
