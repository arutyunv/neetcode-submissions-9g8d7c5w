#### BRUTE FORCE SOLUTION ###


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Step 1. initialize empty array that will be returned
        ans = [0] * len(arr)

        # Step 2. Loop over every element in arr
        for i in range(len(arr)): 
            # Initialize max to -1 (value that means there is no neighbor to the right)
            max_val = -1
            # Loop over values to the right to find max on the right 
            for j in range(i + 1, len(arr)):
                if arr[j] > max_val:
                    max_val = arr[j]
            # Put the value to return array at the index i 
            # to mimic replacement of the original array w/ max element to the right 
            ans[i] = max_val
        
        return ans
