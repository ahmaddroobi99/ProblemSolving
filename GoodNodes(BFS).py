# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, MaxVal):
            if not root:
                return 0

            res = 1 if (root.val >= MaxVal) else 0
            MaxVal = max(MaxVal, root.val)
            res += dfs(root.left, MaxVal)
            res += dfs(root.right, MaxVal)
            return res

        return dfs(root, root.val)
