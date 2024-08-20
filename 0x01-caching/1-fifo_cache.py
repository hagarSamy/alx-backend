#!/usr/bin/python3
""" a class FIFOCache that
inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class that inherit from BaseCaching
    and handles FIFO caching
    '''

    def __init__(self):
        '''overloading __init__'''
        super().__init__()

    def put(self, key, item):
        ''' setting a value to the key of the cache dict'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f'DISCARD: {first_key}')
            self.cache_data[key] = item

    def get(self, key):
        '''retrieving a value by the key'''
        try:
            result = self.cache_data[key]
        except KeyError:
            return None
        return result
