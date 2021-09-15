# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        l1 = []
        l2 = []

        # Recursive helper function to help get our leaf values.
        def helper(node, vals):
            if not node:
                return
            # If we are at a leaf, append the value.
            if not node.left and not node.right:
                vals.append(node.val)
                return
            helper(node.left, vals)
            helper(node.right, vals)

        # Traverse trees.
        helper(root1, l1)
        helper(root2, l2)
        # Check the leaf vals in t1 and t2 are ==.
        return l1 == l2