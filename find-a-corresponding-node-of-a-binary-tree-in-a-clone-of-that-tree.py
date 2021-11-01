
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        row = {(original, cloned)}
        while row:
            next_row = set()
            for node_o, node_c in row:
                if node_o == target:
                    return node_c
                if node_o.left:
                    next_row.add((node_o.left, node_c.left))
                if node_o.right:
                    next_row.add((node_o.right, node_c.right))
            row = next_row
        return cloned    # this should not be reached