### Dynamic Programming (Top-Down): Recursion + memoization ###

"""
The brute force solution recomputes the same subproblems many times.
We can optimize it by remembering results once we compute them.

For each step i, the minimum cost to reach the top is: cost[i] + minimum cost from step i+1 or i+2
By storing this result, we avoid repeated work.

"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}  # cache: stores results for each index i

        # dfs(i) = minimum cost to reach the top starting from step i
        def dfs(i):
            # If we have already computed this state, reuse it
            if i in memo:
                return memo[i]
            
            # Base case:
            # If we go past the last step, we are at the "top"
            # → no cost needed
            if i >= len(cost):
                return 0
            
            # Recursive case:
            # From step i, we can:
            # 1. Move to i + 1
            # 2. Move to i + 2
            # We take the cheaper option
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            
            return memo[i]

        # We can start from step 0 or step 1
        return min(dfs(0), dfs(1))


        