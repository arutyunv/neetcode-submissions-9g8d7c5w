### Two-Pointer Approach ###

"""
Sort the array first. In each step, the heaviest person (end pointer) must take a boat. 
If they can also fit the lightest person (start pointer), move both pointers inward. 
If they can't, only the heaviest person goes, and you move the end pointer down. 
Increment your boat count in every iteration.
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the array 
        people.sort()

        # Get two pointers L and R 
        L = 0
        R = len(people) - 1

        # Boat count 
        boat_count = 0 

        while L <= R:
            # If light person + heavy person fit into boat, put them together 
            if people[R] + people[L] <= limit:
                boat_count+=1 
                L+=1
                R-=1 
            # Else put the heavy 
            else:
                boat_count+=1
                R-=1

        return boat_count
            
            



        