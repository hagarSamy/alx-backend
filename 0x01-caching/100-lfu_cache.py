#!/usr/bin/python3
""" a class LFUCache that
inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''A class that inherit from BaseCaching
    and handles Least frequently used Cache
    '''
    def __init__(self):
        '''overloading __init__'''
        super().__init__()
        self.store = {}

    def put(self, key, item):
        ''' setting a value to the key of the cache dict'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                least_freq_k = min(self.store, key=self.store.get)
                del self.cache_data[least_freq_k]
                del self.store[least_freq_k]
                if key != least_freq_k:
                    print(f'DISCARD: {least_freq_k}')
            self.cache_data[key] = item
            self.store[key] = 0

    def get(self, key):
        '''retrieving a value by the key'''
        if key in self.store:
                self.store[key] +=1
        else:
            self.store[key] = 0
        return self.cache_data.get(key)
