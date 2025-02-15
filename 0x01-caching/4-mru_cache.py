#!/usr/bin/env python3
"""implimentation of MRU"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """impliments MRU caching policy"""
    def __init__(self):
        """initialisation method"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """assigns key value to cache dictionary"""
        if key is None or item is None:
            pass
        else:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > self.MAX_ITEMS:
                most_recent = self.keys.pop(-2)
                del self.cache_data[most_recent]
                print("DISCARD: {}".format(most_recent))

    def get(self, key):
        """gets the value of key"""
        if key:
            if key in self.keys:
                self.keys.remove(key)
                self.keys.append(key)

            try:
                return self.cache_data[key]
            except Exception as e:
                return None
        return None
