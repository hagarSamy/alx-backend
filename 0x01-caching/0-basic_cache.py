#!/usr/bin/python3
"""  a class BasicCache that
inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    A class BaseCaching -- a caching system
    '''
    def put(self, key, item):
        '''setting a value to the key of the cache dict'''
        self.cache_data[key] = item

    def get(self, key):
        '''
        retrieving a value by the key
        '''
        if key is not None:
            try:
                result = self.cache_data[key]
            except KeyError:
                return None
            return result
