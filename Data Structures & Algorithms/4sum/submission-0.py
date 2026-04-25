### Two-Pointer Algorithm ###

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array first
        # Why?
        # 1. Makes it easier to skip duplicates
        # 2. Lets us use the two-pointer technique
        nums.sort()

        # Store the length of the array
        n = len(nums)

        # This will store all valid quadruplets
        res = []

        # First loop: choose the first number
        for i in range(n):

            # Skip duplicate values for the first number
            # If nums[i] is same as previous, we already used it
            # as the first number in a previous quadruplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Second loop: choose the second number
            for j in range(i + 1, n):

                # Skip duplicate values for the second number
                # Same idea: if nums[j] is same as previous j,
                # we would generate duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Now use two pointers to find the last two numbers
                # left starts just after j
                # right starts at the end
                L, R = j + 1, n - 1

                # Keep searching while pointers do not cross
                while L < R:

                    # Compute the sum of the 4 chosen numbers
                    total = nums[i] + nums[j] + nums[L] + nums[R]

                    # If we found a valid quadruplet
                    if total == target:

                        # Add it to the result list
                        res.append([nums[i], nums[j], nums[L], nums[R]])

                        # Move both pointers inward
                        # because we already used this pair
                        L += 1
                        R -= 1

                        # Skip duplicate values on the left
                        # Prevents adding the same quadruplet again
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1

                        # Skip duplicate values on the right
                        # Prevents adding the same quadruplet again
                        while L < R and nums[R] == nums[R + 1]:
                            R -= 1

                    # If sum is too small,
                    # move left pointer right to increase sum
                    elif total < target:
                        L += 1

                    # If sum is too large,
                    # move right pointer left to decrease sum
                    else:
                        R -= 1

        # Return all unique quadruplets
        return res