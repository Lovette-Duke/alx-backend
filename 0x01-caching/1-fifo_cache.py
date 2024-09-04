#!/usr/bin/env python3
"""task 1"""


from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """first in first out cache class."""
    def __init__(self):
        """Initializes class variables."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds an items to the cache."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_out, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_out)

    def get(self, key):
        """returns items by key."""
        return self.cache_data.get(key, None)
