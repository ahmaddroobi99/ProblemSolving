# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)

        root.right = l
        root.left = r

        return root