# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        self.res = 0

        def dfs(root: TreeNode, target: int, prev_sum: int):
            if not root:
                return

            prev_sum += root.val
            self.res += prefix[prev_sum - target]
            prefix[prev_sum] += 1

            dfs(root.left, target, prev_sum)
            dfs(root.right, target, prev_sum)

            prefix[prev_sum] -= 1

        dfs(root, sum, 0)
        return self.res