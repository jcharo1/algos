

import collections


class LRU_Cache(object):

    def __init__(self, capacity=None):
        # Initialize class variables
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity == 0 or self.capacity is None:
            print("Capacity of our cache is zero or null!")
            return -1

        try:
            self.cache.pop(key)
        
        except KeyError:
            
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        
        
        self.cache[key] = value 
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # return -1


print("-----------Test Case 1-------")
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1,5)
print(our_cache.get(1)) #returns 5 since 5 is last recently used 




print("-----------Test Case 2-------")

our_cache1 = LRU_Cache(0)

print(our_cache1.set(2, 2)) #returns -1 and prints error message



print("-----------Test Case 3-------")

our_cache2 = LRU_Cache()


print(our_cache2.set(2,2)) #returns -1 and prints error message