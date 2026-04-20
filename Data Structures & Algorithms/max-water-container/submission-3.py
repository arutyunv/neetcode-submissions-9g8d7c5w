### Two-Pointer Solution ###

"""
We start with two pointers: one at the left end and one at the right end of the array. This gives the widest possible container.

At each step, we compute the area between the two lines. Then we move the pointer with the smaller height inward, because the smaller height is the limiting factor. 
By moving it, we may find a taller line that creates a larger area, even though the width becomes smaller.

We keep updating the maximum area seen so far, and we stop when the two pointers meet.
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # L starts at the left end
        L = 0
        
        # R starts at the right end (important!)
        R = len(heights) - 1
        
        # Store the maximum area found so far
        maxArea = 0 

        # Continue until pointers meet
        while L < R:
            
            # Compute current area BEFORE moving pointers
            width = R - L
            height = min(heights[L], heights[R])
            curArea = width * height
            
            # Update maximum area
            maxArea = max(maxArea, curArea)

            # Move the pointer with the smaller height
            # because it limits (bottlenecks) the area
            if heights[L] < heights[R]:
                L += 1   # move left pointer right
            else:
                R -= 1   # move right pointer left

        return maxArea