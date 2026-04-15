### Approach w/ Hash Set ###

### Idea: Use hash set to keep track of the values we already encounter.
# As we interate thru the array, we check whether the current value is already presented in the set.
# If it is, that means we've seen this value before, so a duplicate exists.
#Using a hash set allows constant-time lookups, making this approach much more efficient than comparing every pair.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty hash set to store seen values 
        seen = set()

        # Iterate through each number in the array
        for num in nums:
            # Check if it is already in the set, return true because a duplicate has been found
            if num in seen:
                return True 
            # Otherwise, add it to the set
            seen.add(num)

        # If the loop finishes w/o finding any duplicates, return False 
        return False 