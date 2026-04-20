### Two Pointer Approach ###

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at the ends of the array
        L = 0
        R = len(numbers) - 1

        # Move pointers based on the current sum
        while L < R:
            current_sum = numbers[L] + numbers[R]

            # If the sum is too large, move the right pointer left
            if current_sum > target:
                R -= 1
            # If the sum is too small, move the left pointer right
            elif current_sum < target:
                L += 1
            # Found the two numbers that sum to target
            else:
                # Return 1-indexed positions
                return [L + 1, R + 1]