### Implementation w/ Array ###

"""
Since keys are constrained to the range [0, 1000000], we can use direct addressing.
We allocate an array where the index represents the key and the value at that index is the stored value. 
We use -1 to indicate that a key is not present. This gives O(1) time for all operations at the cost of fixed memory usage regardless of how many keys are actually stored.
"""


class MyHashMap:

    def __init__(self):
        # Create array w/ 1000000 elements (since we have that contraint on upper bound)
        # index would be the key and actual elements in the array would the value 
        self.map = [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        # Just index into the array and change the value 
        self.map[key] = value
        

    def get(self, key: int) -> int:
        # Get the value from the array 
        return self.map[key]

    def remove(self, key: int) -> None:
        # Removing the element means setting element to -1 
        self.map[key] = -1 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)