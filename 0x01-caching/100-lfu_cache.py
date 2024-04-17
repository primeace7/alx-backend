#!/usr/bin/env python3
'''Implement an LFU cache algorithm
'''


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


class LFUCache(BaseCaching):
    '''Cache with LFU algorithm
    '''
    def __init__(self):
        super().__init__()
        self.keys = []
        self.frequency = []

    def put(self, key, item):
        '''place an item in the cache
        '''
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) == self.MAX_ITEMS:
            min_frequency = min(self.frequency)
            lfu = self.keys[self.frequency.index(min_frequency)]
            print(f'DISCARD: {lfu}')
            del self.cache_data[lfu]
            del self.keys[self.keys.index(lfu)]
            del self.frequency[self.frequency.index(min_frequency)]

        self.keys.append(key)
        self.frequency.append(0)
        self.cache_data[key] = item

    def get(self, key):
        '''Retrieve an item from the cache
        '''
        if key is None or self.cache_data.get(key) is None:
            return None

        idx = self.keys.index(key)

        self.frequency[idx] += 1

        return self.cache_data.get(key)
