### Top-Down DP Approach ### 

class Solution:
    def tribonacci(self, n: int) -> int:
        # Initialize cache that will store the results of previously computed Fibonacci numbers
        cache = {}

        def tribonacci_recursive(n: int) -> int:
            # Base cases: T0 = 1, T1 = 1, T2 = 1
            if n <= 2:
                return 1 if n != 0 else 0

            # If already computed current Fib number, return cached value
            if n in cache:
                return cache[n]

            # Compute and store result
            cache[n] = (
                tribonacci_recursive(n - 1)
                + tribonacci_recursive(n - 2)
                + tribonacci_recursive(n - 3))
            
            return cache[n]

        return tribonacci_recursive(n)