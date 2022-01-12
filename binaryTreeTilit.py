# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def preorder(node):
            if node is None:
                return 0
            leftSum = preorder(node.left)
            rightSum = preorder(node.right)
            preorder.tilt += abs(leftSum - rightSum)

            return node.val + leftSum + rightSum

        preorder.tilt = 0
        preorder(root)
        return preorder.tilt