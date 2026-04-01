class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_so_far = 0
        curr_count = 0 

        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                best_so_far = max(curr_count, best_so_far)
                curr_count = 0 
        
        return max(curr_count, best_so_far)
