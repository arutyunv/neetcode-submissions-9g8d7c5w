# Its like decision tree 

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(remaining_steps: int) -> int:
            if remaining_steps in memo:
                return memo[remaining_steps]
            if remaining_steps == 0:
                res = 1
            elif remaining_steps < 0:
                res = 0
            else:
                res = dfs(remaining_steps - 1) + dfs(remaining_steps - 2)
            memo[remaining_steps] = res
            return res

        return dfs(n)

        