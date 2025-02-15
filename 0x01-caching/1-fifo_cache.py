#!/usr/bin/env python3
"""
a class FIFOCache that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        self.cache_data[key] = item

        if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print("DISCARD: {}\n".format(first_key))
    
    def get(self, key):
        for key, value in self.cache_data.items():
            return value
        return None

