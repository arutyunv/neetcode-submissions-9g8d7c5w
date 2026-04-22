### Not Optimal Solution - Hash Set Approach ###

"""
We know, while walking, if we visit the same node again - there must be a cycle, so we can initialize 
the HashSet to keep track of the nodes visisted while walking and as soon as we check HashSet in O(1) and find out that there is this node, we can
conclude there is a cycle. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize the empty HashSet
        visited = set()

        # while we have node to trace 
        while head is not None:
            if head in visited: # seen this node before -> cycle 
                return True 
            visited.add(head) # remember this node 
            # Move to next node 
            head = head.next 
        
        return False 


        