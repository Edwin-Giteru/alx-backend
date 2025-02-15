#!/usr/bin/env python3
"""
a class that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        self.cache_data[key] = item
    
    def get(self, key):
        for key, value in self.cache_data.items():
            return value
        return None
