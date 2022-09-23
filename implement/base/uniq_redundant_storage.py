"""
    base class implement UniqRedundantStorage
"""

import abstract
from .redundant_storage import RedundantStorage


class UniqRedundantStorage(RedundantStorage, abstract.UniqRedundantStorage):

    def __init__(self, **kwargs):
        assert "uniq_capacity" in kwargs, "Missing required parameter uniq_capacity"
        assert type(kwargs["uniq_capacity"]) == int, "Required parameter uniq_capacity must be an int"
        assert kwargs["uniq_capacity"] > 0, "Required parameter uniq_capacity must greater than 0"
        super(UniqRedundantStorage, self).__init__(**kwargs)
        self._uniq_capacity = kwargs["uniq_capacity"]

    def get_free_space(self) -> int:
        self_products = self.get_items().keys()
        redundant_products = self._redundant.get_items().keys()
        uniq_products = {*self_products, *redundant_products}

        if len(uniq_products) < self._uniq_capacity:
            return super(UniqRedundantStorage, self).get_free_space()
        return 0
