# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xl = []
        yl = []
        depth = 0
        parent = None
        if root is None:
            return False

        self.dfs(root, x, y, 0, None, xl, yl)
        return xl[0][0] == yl[0][0] and xl[0][1] != yl[0][1]

    def dfs(self, root, x, y, depth, parent, xl, yl):
        if root is None:
            return False

        if root.val == x:
            xl.append((depth, parent))

        if root.val == y:
            yl.append((depth, parent))

        self.dfs(root.left, x, y, depth + 1, root, xl, yl)
        self.dfs(root.right, x, y, depth + 1, root, xl, yl)





