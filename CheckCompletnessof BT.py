# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        prev = root
        while q:
            node = q.pop(0)
            if node:
                if not prev:
                    return False
                q.append(node.left)
                q.append(node.right)
            prev = node
        return True