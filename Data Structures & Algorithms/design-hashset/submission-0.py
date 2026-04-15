"""

A little refresh of what HashSet is: 

A HashSet is a collection of unique values where we can:
1. Add fast 
2. Check existence fast 
3. Remove fast 

We don’t store elements randomly — we use a hash function to decide where to store them. 

Core Idea: Hashing. We use a function like: index = key % size. 
This maps any key to a position in an array. Example:
   * key = 1, so index = 1 % 1000 = 1
   * key = 1001 → index = 1001 % 1000 = 1
Problem: collisions (different keys - same index)

How to handle collisions? We use chaining: Each index stores a list (bucket)
So instead of: array[index] = key

We do: array[index] = [list of keys]
""" 


class MyHashSet:

    def __init__(self):
        self.size = 1000001 # number of buckets
        self.data = [[] for _ in range(self.size)]  # array of lists

    def hash(self, key):
        return key % self.size # map key → index

    def add(self, key: int) -> None:
        index = self.hash(key) # find bucket
        bucket = self.data[index]

        # avoid duplicates
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        index = self.hash(key)
        bucket = self.data[index]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        bucket = self.data[index]

        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)