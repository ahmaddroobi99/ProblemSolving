# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinrayTreePath import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def depth(root):
            ans = 0
            while root:
                root = root.left
                ans += 1
            return ans

        def count(root, left_level):
            if not root:
                return 0
            right_level = depth(root.right)
            if right_level == left_level:
                return count(root.right, right_level - 1) + (1 << left_level)
            else:
                return count(root.left, left_level - 1) + (1 << right_level)

        return count(root, depth(root) - 1)

# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         stack = []
#         height = 0
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             height += 1
#             root = root.right
#         return (height)