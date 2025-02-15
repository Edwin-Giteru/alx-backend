#!/usr/bin/env python3
"""
a class LIFOCache that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):        
        if key is None and item is None:
            return
        self.cache_data[key] = item
        self.stack.append(key)
        
        if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        for value in self.cache_data.values():
            return value
        return None
