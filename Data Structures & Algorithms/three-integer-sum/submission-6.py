### Brute Force Approach ###

"""
The brute-force approach simply tries every possible triplet.
Since we check all combinations (i, j, k) with i < j < k, we are guaranteed to find all sets of three numbers that sum to zero.
Sorting helps keep the triplets in order and makes it easier to avoid duplicates by storing them in a set.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array to make handling duplicates easier
        nums.sort()

        # create an empty set result to store unique triples 
        result = set()

        # Loop over i 
        for i in range(len(nums)):
            # Loop over j 
            for j in range(i+1, len(nums)):
                # Loop over k 
                for k in range(j+1, len(nums)):
                    # Check equality condition 
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        # Add to set as a tuple, because this way we can check for duplicates 
                        result.add(tuple(temp))   
        
        # Convert the set of tuples back into a list of lists and return 
        return [list(i) for i in result]