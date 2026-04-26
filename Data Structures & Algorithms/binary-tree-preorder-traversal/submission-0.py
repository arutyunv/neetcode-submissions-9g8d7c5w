### Iterative Depth First Search Approach ###


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val          # Value stored in the node
#         self.left = left        # Pointer to left child
#         self.right = right      # Pointer to right child

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Preorder = Root -> Left -> Right
        # We will simulate recursive DFS using our own stack.

        curr = root
        # 'curr' is the current node we are exploring
        # Start at the root of the tree

        stack = []
        # Stack stores right children we need to visit later
        # This simulates the recursive call stack

        res = []
        # Result list to store preorder traversal

        # Continue while:
        # 1. we still have a current node to explore
        # OR
        # 2. we have saved right children in the stack
        while curr or stack:

            # If current node exists, process it
            if curr:
                res.append(curr.val)
                # Preorder visits Root first
                # So record current node's value immediately

                stack.append(curr.right)
                # Save the right child for later
                # We do this because preorder explores Left first,
                # so Right must wait on the stack

                curr = curr.left
                # Move left first
                # This follows preorder: Root -> Left -> Right

            else:
                curr = stack.pop()
                # If no current node, we finished going left
                # Backtrack by popping a saved right child
                # This resumes traversal on the right side

        return res
        # Return preorder traversal result

        