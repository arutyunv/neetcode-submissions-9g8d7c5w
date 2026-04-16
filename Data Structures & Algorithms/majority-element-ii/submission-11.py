### Hash Map Approach ### 

"""
Idea: Use hash map that stores key->value pair as an element->its frequency.  
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Get the length of array
        n = len(nums)


        elements = set()
        frequency_map = {}

        for num in nums: 
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

            # Check if the current element showed up more than n/3 times? 
            if frequency_map[num] > n // 3:
                # If so, append to elements array 
                elements.add(num)
            
        return list(elements)

        