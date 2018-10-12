"""
Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations:
get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it
should invalidate the least recently used item before inserting the new item.
The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number
of unique keys it can hold at a time.

Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least
recently used” item is the one with the oldest access time.

NOTE: If you are using any global variables, make sure to clear them in the constructor.
Example :

Input :
         capacity = 2
         set(1, 10)
         set(5, 12)
         get(5)        returns 12
         get(1)        returns 10
         get(10)       returns -1
         set(6, 14)    this pushes out key = 5 as LRU is full.
         get(5)        returns -1
"""


class LRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0  # for tracking use of the key ::: if capacity is full min time was removed
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.time
            self.time += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.time
        self.time += 1


# Solution 2 using ordered dict
class LRUCache:

    def __init__(self, capacity):
        from collections import OrderedDict
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                print(self.cache.popitem(last=False))
        self.cache[key] = value


lru = LRU(2)
print(lru.get(2))

lru.set(2, 6)
print(lru.get(1))

lru.set(1, 5)
lru.set(1, 2)
print(lru.get(1))
print(lru.get(2))
