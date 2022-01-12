# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if arr:
                v = max(arr)
                idx = arr.index(v)
                node = TreeNode(v)
                node.left = helper(arr[:idx])
                node.right = helper(arr[idx + 1:])

                return node

        return helper(nums)