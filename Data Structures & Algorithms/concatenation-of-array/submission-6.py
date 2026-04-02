#### ONE PASS (SMARTER APPROACH) SOLUTION #### 

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Step 1. Get length of initial array 
        n = len(nums)
        # Step 2. Create/initialize array ans of size 2n that will be returned 
        ans = [0] * (2 * n)

        # Step 3. Loop over all elements in nums 
        for i in range(n):
            # Index mapping i... populating first half of the array of size n 
            ans[i] = nums[i]

            # index mapping i+n... populating the second half of the array of size n
            ans[i+n] = nums[i]

        return ans 