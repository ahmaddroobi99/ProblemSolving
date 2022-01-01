# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:

#         def helper(n: TreeNode = root):
#             if not n or n.val == val:
#                 return n
#             return helper(n.right) if val > n.val else helper(n.left)

#         return helper()
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        ptr = root
        while ptr:
            if ptr.val == val:
                return ptr
            ptr = ptr.right if val > ptr.val else ptr.left