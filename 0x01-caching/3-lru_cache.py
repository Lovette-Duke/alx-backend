#!/usr/bin/env python3
"""task 3"""


from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """least recently used cache class."""
    def __init__(self):
        """initialize class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds items to the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """returns items by their key."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return key if self.cache_data.get(key) else None
