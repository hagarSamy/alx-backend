#!/usr/bin/python3
""" a class LRUCache that
inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''A class that inherit from BaseCaching
    and handles Least recently used Cache
    '''

    def __init__(self):
        '''overloading __init__'''
        super().__init__()

    def put(self, key, item):
        ''' setting a value to the key of the cache dict'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                lru_key = next(iter(self.cache_data))
                del self.cache_data[lru_key]
                print(f'DISCARD: {lru_key}')
            self.cache_data[key] = item

    def get(self, key):
        '''retrieving a value by the key'''
        try:
            result = self.cache_data[key]
        except KeyError:
            return None
        # reorder the dict
        k_v = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = k_v
        return result
