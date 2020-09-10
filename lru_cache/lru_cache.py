class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, capacity=10):
        # check if limit is valid
        if capacity < 1:
            print("LRUCache capacity must be > 0")
            return None
        self.capacity = capacity
        self.size = 0
        self.node_map = {}
        self.head = None
        self.tail = None
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.node_map:
            return self.node_map[key].value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key exist, use the corresponding node and update its value
        if key in self.node_map:
            self.node_map[key].value = value
        else:
            node = Node(key,value)
            self.node_map[key] = node

            if self.size == 0:
                self.head = node
                self.tail = node
            
            if self.size < self.capacity:
                self.size += 1

            # size at max capacity must remove the least recently used
            elif self.size == self.capacity:
                k = self.tail.key # preserve current tail key

                if self.size == 1:
                    # special case; replace only node left,
                    # so it becomes the head and the tail
                    self.head = node
                    self.tail = node
                else:
                    # normal case, just adjust the tail position
                    if self.tail:
                        if self.tail.prev:
                            self.tail = self.tail.prev
                            self.tail.next = None
        
                # delete old try:
                del self.node_map[k]
            