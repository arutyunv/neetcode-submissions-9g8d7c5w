### Prefix Sum Solution ###

"""
Step 1: Build a prefix sum array
    prefix[i] = sum of nums[0] through nums[i].
    This lets us know the total sum to any index from the left.
Step 2: Build a postfix sum array
    postfix[i] = sum of nums[i] through nums[n-1].
    This lets us know the total sum from any index to the right.
Step 3: Find the pivot
    For each index i from 0 to n-1:
    left_sum = prefix[i-1] if i > 0, otherwise 0.
    right_sum = postfix[i+1] if i+1 < n, otherwise 0.
    If left_sum equals right_sum, return i (this is the leftmost pivot due to scanning from left to right).
Step 4: If no index satisfies the condition, return -1.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Build prefix sums: prefix[i] = sum(nums[0..i])
        prefix = []
        total = 0
        for x in nums:
            total += x
            prefix.append(total)
        
        # Build postfix sums: postfix[i] = sum(nums[i..n-1])
        postfix = [0] * n
        total = 0
        for i in range(n - 1, -1, -1):
            total += nums[i]
            postfix[i] = total

        # Check each index: left sum vs right sum
        for i in range(n):
            left_sum = prefix[i - 1] if i > 0 else 0
            right_sum = postfix[i + 1] if i + 1 < n else 0
            if left_sum == right_sum:
                return i

        return -1


        