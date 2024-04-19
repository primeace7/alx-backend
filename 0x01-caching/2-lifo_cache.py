#!/usr/bin/env python3
'''Implement a LIFO cache
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''Cache with LIFO algorithm
    '''
    def __init__(self):
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        '''place an item in the cache
        '''
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) == self.MAX_ITEMS:
            print(f'DISCARD: {self.insertion_order[-1]}')
            del self.cache_data[self.insertion_order[-1]]
            del self.insertion_order[-1]

        self.insertion_order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieve an item from the cache
        '''
        if key is None or self.cache_data.get(key) is None:
            return None

        return self.cache_data.get(key)
