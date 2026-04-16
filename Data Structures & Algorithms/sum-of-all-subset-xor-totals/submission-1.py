### Recursive DFS Approach ###

"""
A cleaner recursive approach avoids explicitly building subsets. 
For each element, we make a binary choice (create a binary decision tree): include it in the XOR or skip it. 

We pass the running XOR total down the recursion tree. 

When we reach the end of the array, we return the accumulated XOR value. 
The sum of all returned values gives us the total.
"""


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int: 
        # Get the length of the nums array
        n = len(nums)

        # Define recursive (DFS) helper function 
        def dfs(i, current_xor):
            # Base case, when we went over all elements, we return current xor
            if i >= n:
                return current_xor
            
            # If not, we make two dfs calls: The first call includes nums[i] in the 
            # Second call excludes nums[i]
            # We sum XORs up 
            return dfs(i + 1, current_xor ^ nums[i]) + dfs(i + 1, current_xor)

        # Call the helper function on index = 0 and XOR sum of 0 to get the full tree traversal 
        return dfs(0, 0)
            
            
