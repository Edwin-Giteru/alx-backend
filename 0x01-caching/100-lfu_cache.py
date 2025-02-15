#!/usr/bin/env python3
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFU Caching System """
    
    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.freq_count = {}

    def put(self, key, item):
        """ Add an item to the cache using LFU policy """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.freq_count[key] += 1 
        else:
            self.cache_data[key] = item
            self.freq_count[key] = 1
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_key = min(self.freq_count, key=self.freq_count.get) 
            if lfu_key in self.cache_data:
                del self.cache_data[lfu_key]
                del self.freq_count[lfu_key]
                print(f"DISCARD: {lfu_key}")
    
    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        
        self.freq_count[key] += 1  # Increase frequency count
        return self.cache_data[key]

