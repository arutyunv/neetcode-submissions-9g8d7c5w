### Backtracking Approach ###

"""
We want all subsets, but the array may contain duplicates.
If we blindly generate all subsets, we will produce repeated ones.
So we must avoid picking the same value in the same decision level more than once.

Key idea:

At each index i, we make two choices:
    * Include nums[i]
    * Exclude nums[i]
But when excluding, if the next number is the same (nums[i] == nums[i+1]), then skipping it now and skipping it later produce the same subset.
So after exploring the "exclude" branch, we skip over all duplicate values to avoid generating duplicate subsets.

We also sort the array first, so duplicates become consecutive and easy to skip.

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # First, we sort the array to have duplicate elements together 
        nums.sort()

        # Initialize result list of lists and curSet (a list)
        subsets = [] 
        curSet = [] 

        # Backtracking recursive function to generate subsets of an array
        def helper(i, nums, curSet, subsets):
            # Base case when we hit the end of the array 
            if i == len(nums):
                subsets.append(curSet.copy())
                return 

            
            # Case when we make a decision tp include nums[i]
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subsets)
            curSet.pop()

            # Case when we make decision NOT to include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, nums, curSet, subsets)

        # Call the recursive helper function on the whole array 
        helper(0, nums, curSet, subsets)

        # Helper function modified subsets and we just return it
        return subsets

        