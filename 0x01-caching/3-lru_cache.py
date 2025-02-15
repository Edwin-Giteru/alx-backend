#!/usr/bin/env python3
"""
a class LRUCache that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key is None and item is None:
            return 

        self.cache_data[key]=item
        self.order.append(key)

        if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            if lru_key in self.cache_data:
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))

    def get(self, key):
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
