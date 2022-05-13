# Code design 
In this problem I decided to use `OrderedDict()` from the `collections` module and utilizing the `popitem(last=False)`, which removes and returns a (key,pair). The pairs are returned in FIFO order when `last=False` 
# Time Efficiency
Time Efficiency for operations `get()` and `set()` are `O(1)`
# Space Complexity
Space complexity of the LRU Cache is `O(n)`



