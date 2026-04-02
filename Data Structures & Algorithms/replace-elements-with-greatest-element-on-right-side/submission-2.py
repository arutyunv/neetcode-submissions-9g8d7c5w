#### BRUTE FORCE SOLUTION ###


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Step 1. initialize empty array that will be returned
        ans = [0] * len(arr)

        # Step 2. Loop over every element in arr
        for i in range(len(arr)): 
            max_val = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > max_val:
                    max_val = arr[j]
            ans[i] = max_val
        
        return ans
