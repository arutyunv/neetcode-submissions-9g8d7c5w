### Reverse the Second half of Linked list Approach ###

"""
To avoid extra space from converting to an array, we can modify the list itself. 
Using the slow and fast pointer technique, we find the middle of the list. 
Then we reverse the second half in place. Now the first half and the reversed second half can be traversed simultaneously, 
allowing us to compute twin sums directly without extra stora
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1. Use slow and fast pointers to find the start of the second half. 
        # When fast reaches the end, slow is at the midpoint.
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2. Reverse the second half of the list starting from slow.
        prev, cur = None, slow
        # Note: After reversing the second half, R points to the head of the reversed second half. That half contains exactly n/2 nodes (since the list length is even).
        # You want to process each node of the second half exactly once, pairing it with the corresponding node in the first half. When you reach the end of the reversed second half, R becomes None.
        # note 2: the reversed first half has n/2 nodes and its tail points to None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # Step 3. Initialize L at the head and R at the head of the reversed second half.
        # Step 4. While R is not null:
        # Compute L.val + R.val and update maxSum if larger
        # Advance both L and R

        maxSum = 0
        L, R = head, prev
        while R:
            maxSum = max(maxSum, L.val + R.val)
            L, R = L.next, R.next

        return maxSum
        