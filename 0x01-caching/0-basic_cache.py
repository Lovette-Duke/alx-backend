#!/usr/bin/python3
"""caching task 0"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """completing the basic cache class."""

    def __init__(self):
        """initializing. """
        super().__init__()

    def put(self, key, item):
        """adding the put method."""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """adding the get method."""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
