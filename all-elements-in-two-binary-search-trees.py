# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, temp):
        if root:
            self.dfs(root.left, temp)
            temp.append(root.val)
            self.dfs(root.right, temp)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        temp1 = []
        temp2 = []
        self.dfs(root1, temp1)
        self.dfs(root2, temp2)
        i = 0
        temp1.extend(temp2)
        temp1.sort()
        return temp1