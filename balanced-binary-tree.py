# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if node == None:
                return (0, True)

            l_h, l_b = helper(node.left)
            r_h, r_b = helper(node.right)

            return (max(l_h, r_h) + 1, l_b and r_b and abs(l_h - r_h) <= 1)

        return helper(root)[1]











