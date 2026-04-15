### Approach with Sorting ### 

# Idea: If we sort the array, then any duplicate values will appear next to each other.
# Sorting groups identical elements together, so we can simply check adjacent positions to detect duplicates.
# This reduces the problem to a single linear scan after sorting, making it easy to identify if any value repeats.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # When we call .sort() built-in Python method/function
        # (it means it is part of Python’s standard library)
        # Array nums is sorted IN-PLACE
        nums.sort()

        # Start from index = 1 and till the end
        # Starting from 1 will help us to compare adjacent positions at index i=0 and index i=1
        # w/o causing an Index error 
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True 
        return False 
    