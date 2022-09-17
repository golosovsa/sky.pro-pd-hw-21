"""
    class Shop
    - no more than 5 unique items
    - capacity 20 by default
"""
from store import Store


class Shop(Store):

    _type: str = "магазин"

    def __init__(self, capacity: int = 20, unique_capacity: int = 5):
        super(Shop, self).__init__(capacity=capacity)
        self.__unique_capacity = unique_capacity

    @property
    def unique_capacity(self) -> int:
        return self.__unique_capacity

    def add(self, product: str, amount: int) -> int:
        if product not in self.items and self.get_unique_items_count() >= self.__unique_capacity:
            return 0
        return super(Shop, self).add(product=product, amount=amount)
