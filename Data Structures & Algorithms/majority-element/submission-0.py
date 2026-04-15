### Brute-force solution ### 

# Idea: since majority element appears more than n/2 times, 
# we can count how many times it appears in the array. If the count exceeds n/2, we have found the answer. 
# This straightforward approach checks every element against every other element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       # Get length of array nums
       n = len(nums) 

       # Loop over every element in nums
       for num in nums: 
        # Loop over nums again and count how many occurences we have of that element
        count = sum(1 for i in nums if i == num)
        # Check if count is more than n/2 times
        if count > n // 2:
            return num
        