#!/usr/bin/env python3
'''implement a basic Cache with no optimization or limits
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Basic cache without any optimizations
    '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''place an item in the cache
        '''
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        '''Retrieve an item from the cache
        '''
        if key is None or self.cache_data.get(key) is None:
            return None

        return self.cache_data.get(key)
