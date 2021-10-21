# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# sol 1

# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         def dfs (root):
#             if not root :
#                 return None

#             leftTail= dfs (root.left)
#             righTail = dfs(root.right)

#             if leftTail :
#                 leftTail.right = root.right
#                 root.right =root.left
#                 root.left= None


#             last=  righTail or leftTail or root
#             return last

#         dfs (root)


# sol 2


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        res = []
        self.get(root, res)
        for i in res[1:]:
            root.right = i
            root.left = None
            root = root.right

    def get(self, root, res):
        if root == None:
            return
        res.append(root)
        self.get(root.left, res)
        self.get(root.right, res)