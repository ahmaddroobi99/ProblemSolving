# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.maxLvl=0
        self.leftVal=None
        def DFS(node,lvl):
            if node:
                if lvl>self.maxLvl:
                    self.leftVal=node.val
                    self.maxLvl=lvl
                DFS(node.left,lvl+1)
                DFS(node.right,lvl+1)
        DFS(root,1)
        return self.leftVal