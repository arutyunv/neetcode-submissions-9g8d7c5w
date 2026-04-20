### Brute Force Solution ###

"""
Brute force ignores the ordering and simply checks every possible pair.
For each index i, we look at every index j > i and check whether their sum equals the target.
This approach is easy to understand but inefficient because it tries all combinations without using the sorted property.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Loop through the array using index i from 0 to n-1
        for i in range(len(numbers)):

            # For each i, loop through index j from i+1 to n-1
            for j in range(i+1, len(numbers)): 

                # If numbers[i] + numbers[j] equals the target:
                if numbers[i] + numbers[j] == target:

                    # Return [i + 1, j + 1] (1-indexed as required by the problem)
                    return [i+1, j+1]      

        # if no such pair exists, return an empty list 
        return []   
                    