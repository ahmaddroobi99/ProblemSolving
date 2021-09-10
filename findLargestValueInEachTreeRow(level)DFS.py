# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node=root, level=0):
            if not node:
                return
            if len(res)-1 < level:
                res.append(node.val)
            else:
                res[level] = max(node.val, res[level])
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs()
        return res