# 146. LRU Cache
# Medium

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4


# Constraints:


# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        if self.next:
            return f"Key: {self.key}, Val: {self.val} -> {self.next}"
        return str(self.val)


class LRUCache:

    # Time: O(1)
    # Space: O(n)
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum capacity of the cache
        self.cache = {}  # Dictionary to store key-node pairs
        self.head = Node(0, 0)  # Dummy head of the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail of the doubly linked list
        self.head.next = self.tail  # Initialize the list as empty
        self.tail.prev = self.head

    # Time: O(1)
    # Space: O(n)
    def insert(self, node):
        # Insert the node right after the head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # Time: O(1)
    # Space: O(n)
    def remove(self, node):
        # Remove the node from the doubly linked list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    # Time: O(1)
    # Space: O(n)
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Move the accessed node to the front
            self.insert(node)
            return node.val  # Return the value of the node
        return -1  # Return -1 if the key is not found

    # Time: O(1)
    # Space: O(n)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # Remove the old node
        node = Node(key, value)
        self.cache[key] = node  # Insert the new node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev  # Identify the least recently used node
            self.remove(lru)  # Remove the least recently used node
            del self.cache[lru.key]  # Delete the node from the cache

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    def main(self):
        print("Command: LRUCache(2)")
        lru_cache = LRUCache(2)
        print("Command: put(1, 1)")
        lru_cache.put(1, 1)
        print("Command: put(2, 2)")
        lru_cache.put(2, 2)
        print("Command: get(1)")
        print(f"Output: {lru_cache.get(1)}")
        print("Command: put(3, 3)")
        lru_cache.put(3, 3)
        print("Command: get(2)")
        print(f"Output: {lru_cache.get(2)}")
        print("Command: put(4, 4)")
        lru_cache.put(4, 4)
        print("Command: get(1)")
        print(f"Output: {lru_cache.get(1)}")
        print("Command: get(3)")
        print(f"Output: {lru_cache.get(3)}")
        print("Command: get(4)")
        print(f"Output: {lru_cache.get(4)}")


if __name__ == "__main__":
    LRUCache(0).main()
