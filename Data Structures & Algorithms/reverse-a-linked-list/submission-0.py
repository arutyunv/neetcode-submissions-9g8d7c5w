## ITERATIVE APPROACH ##


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head is the first node of the linked list
        prev = None
        curr = head

        # Loop stops when curr point to None/null
        while curr:
            temp = curr.next      # point to next node in the original (not reversed) list
            curr.next = prev      # reverse 
            prev = curr           # move prev to current node 
            curr = temp           # move curr further 

        # prev is the new head of the reversed list.
        return prev