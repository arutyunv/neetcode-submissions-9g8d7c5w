### Sliding Window Approach ###

"""
We maintain a running sum of the current window. 
When the window slides, we add the new element entering from the right and remove the element leaving from the left. 
This gives constant-time updates per window instead of recalculating from scratch.
"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        
        # sum of first k elements (first window)
        window_sum = sum(arr[:k])
        
        # check first window
        if window_sum / k >= threshold:
            count += 1
        
        # slide the window
        for i in range(k, len(arr)):
            # add next element and remove the leftmost one
            window_sum += arr[i] - arr[i - k]
            
            # check condition
            if window_sum / k >= threshold:
                count += 1
        
        return count