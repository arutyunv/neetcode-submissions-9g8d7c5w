### Brute-Force Solution ### 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            value = nums[i]
            for k in range(i+1, len(nums)):
                if value == nums[k]:
                    return True

        return False
