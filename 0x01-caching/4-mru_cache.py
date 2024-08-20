#!/usr/bin/python3
""" a class MRUCache that
inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''A class that inherit from BaseCaching
    and handles most recently used Cache
    '''

    def __init__(self):
        '''overloading __init__'''
        super().__init__()

    def put(self, key, item):
        ''' setting a value to the key of the cache dict'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                mru_key, value = self.cache_data.popitem()
                del self.cache_data[mru_key]
                print(f'DISCARD: {mru_key}')
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
