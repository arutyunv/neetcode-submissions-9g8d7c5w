### Brute Force Solution ###

"""
The most straightforward approach is to check every possible subarray. 
For each starting index, we expand the subarray until the sum reaches or exceeds the target, then record the length. 
Since all numbers are positive, once we hit the target we can stop expanding from that starting point.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        all_length = []
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # Calculate sum of subarray nums[i] to nums[j]
                current_sum = sum(nums[i:j+1])
                
                if current_sum >= target:
                    # Store the length, not the sum
                    all_length.append(j - i + 1)
                    break  # Break early since we found a valid subarray starting at i
        
        # Return the minimum length if found, otherwise 0
        return min(all_length) if all_length else 0

        
        