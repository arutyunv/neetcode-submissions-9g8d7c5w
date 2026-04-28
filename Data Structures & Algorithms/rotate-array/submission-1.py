### Brute-Force Approach ###

"""
The simplest way to rotate an array by k positions is to perform k single rotations. 
In each rotation, we save the last element, shift every element one position to the right, 
and place the saved element at the front. This mimics the physical act of rotating items in a line. While straightforward, 
this approach is slow because we repeat the entire shift process k times.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Compute k such that it handles cases where k is larger than the array length 
        n = len(nums)
        k = k % n 

        # Repeat k single rotations 
        while k:
            # Store the last element in temp variable 
            temp = nums[n-1]
            # Shift all elements one position to the right.
            for i in range(n-1, 0, -1):
                nums[i] = nums[i - 1]
            
            # Place the saved element at index 0 
            nums[0] = temp 

            # Decrement k by 1 since we just completed a single rotation 
            k-=1

        
        
        