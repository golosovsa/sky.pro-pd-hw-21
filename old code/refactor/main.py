"""
    Main
"""

from store import Store
from shop import Shop
from request import Request

if __name__ == "__main__":
    print("=" * 80)
    store = Store()
    shop = Shop()

    Request.init([store, shop], "Доставить 3 печеньки из склад в магазин")
