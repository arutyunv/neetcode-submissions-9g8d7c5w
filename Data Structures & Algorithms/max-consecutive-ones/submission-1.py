class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # n is the number of elements in array 
        n = len(nums)
        # initiaize resulted count to be 0 
        final_count = 0 

        # loop over each index 
        for i in range(n):
            counter = 0 
            # for each index, count how many consecutive 1 start from that position
            for j in range (i, n): 
                if nums[j] == 1:
                    counter += 1 
                else: break
            # take the maximum between current count and best count so far 
            final_count = max(final_count, counter)

        return final_count