"""
    abstract init package
"""

# repository
#   |---> storage
#           |---> courier <---
#           |---> redundant_storage
#                   |---> warehouse <---
#                   |---> uniq_redundant_storage
#                           |---> shop <---

from .repository import Repository
from .storage import Storage
from .redundant_storage import RedundantStorage
from .uniq_redundant_storage import UniqRedundantStorage

# essence
#   |---> warehouse <---
#   |---> shop <---
#   |---> mobile_essence
#           |---> courier <---

from .essence import Essence
from .mobile_essence import MobileEssence

# ---> warehouse <---
# ---> shop <---
# ---> Courier <---

from .warehouse import Warehouse
from .shop import Shop
from .courier import Courier

##############################
# request generates tasks
# the task has several stages
# the world asynchronously processes requests and performs tasks

# request
from .request import Request

# task
from .task import Task

# world
from .world import World
