### Brute Force Solution ###

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # Initialize counter that will be keeping track of sub-arrays 
        counter = 0 
        # Optimization: calculate target sum once to avoid division and floating point logic
        target_sum = k * threshold

        # Left (L) pointer (that goes over every elements in the array)
        for L in range(len(arr) - k + 1):
            # Keep the subarray itself 
            subarray = [] 

            # Right (R) pointer
            for R in range(L, L + k):
                subarray.append(arr[R])
            
            # Take the average of the current subarray
            current_sum = sum(subarray)

            # Check if the subarray average is greater than or equal to threshold
            if current_sum >= target_sum:
                counter+=1
    
        return counter
