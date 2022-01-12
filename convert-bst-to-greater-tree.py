# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        def reverseIorder(node, sum_):
            if not node:
                return sum_
            node.val += reverseIorder(node.right,sum_)
            return reverseIorder(node.left,node.val)
        reverseIorder(root,0)
        return root


# class Solution:
# 	def dfs(self, root: TreeNode, s) -> int:
# 		if root.right:
# 			s = self.dfs(root.right, s)
# 		root.val += s
# 		s = root.val
# 		if root.left:
# 			s = self.dfs(root.left, s)
# 		return s

# 	def convertBST(self, root: TreeNode) -> TreeNode:
# 		if root:
# 			self.dfs(root, 0)
# 		return root