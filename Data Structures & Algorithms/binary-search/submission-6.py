class Solution:
    def search(self, nums, target):
        # Recursive helper function
        # Searches for target between indices left and right
        def search_recursive(left, right):

            # Base case:
            # If the search space becomes invalid,
            # target does not exist in the array
            if left > right:
                return -1

            # Find middle index of current search range
            mid = (left + right) // 2

            # If middle element equals target,
            # we found the answer
            if nums[mid] == target:
                return mid

            # If target is smaller than middle element,
            # search the LEFT half
            if target < nums[mid]:
                return search_recursive(left, mid - 1)

            # Otherwise search the RIGHT half
            return search_recursive(mid + 1, right)

        # Start searching across the entire array
        return search_recursive(0, len(nums) - 1)