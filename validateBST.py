class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        low, high = float('-inf'), float('inf')
        return self.helper(root, low, high)

    def helper(self, root, lower_bound, upper_bound):
        if not root:
            return True
        if lower_bound < root.val < upper_bound:
            return self.helper(root.left, lower_bound, root.val) and self.helper(root.right, root.val, upper_bound)
        return False




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right