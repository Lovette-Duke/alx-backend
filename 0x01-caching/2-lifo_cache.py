#!/usr/bin/env python3
"""task 2"""


from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """last in first out cache class."""
    def __init__(self):
        """initialize the class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds items to the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_in, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_in)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """returns items by their keys."""
        return self.cache_data.get(key, None)
