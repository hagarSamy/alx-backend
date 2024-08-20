#!/usr/bin/python3
""" a class LIFOCache that
inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''A class that inherit from BaseCaching
    and handles LIFO caching
    '''

    def __init__(self):
        '''overloading __init__'''
        super().__init__()

    def put(self, key, item):
        ''' setting a value to the key of the cache dict'''
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                last_key, val = self.cache_data.popitem()
                print(f'DISCARD: {last_key}')
            self.cache_data[key] = item

    def get(self, key):
        '''retrieving a value by the key'''
        try:
            result = self.cache_data[key]
        except KeyError:
            return None
        return result
