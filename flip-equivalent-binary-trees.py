# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def sol(root1, root2):
            if not root1 and not root2:
                return True
            if not (root1 and root2):
                return False
            if root1.val != root2.val:
                return False
            if (root1.left and root2.right) and (root1.left.val == root2.right.val):
                temp = root1.left
                root1.left = root1.right
                root1.right = temp
            if (root1.right and root2.left) and (root1.right.val == root2.left.val):
                temp = root1.left
                root1.left = root1.right
                root1.right = temp

            return sol(root1.left, root2.left) and sol(root1.right, root2.right)

        return sol(root1, root2)