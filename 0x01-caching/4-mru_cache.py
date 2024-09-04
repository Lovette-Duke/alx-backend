#!/usr/bin/env python3
"""task 4"""


from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """most recently used cache class."""
    def __init__(self):
        """initializes class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds items to the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """returns items by key."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return key if self.cache_data.get(key) else None
