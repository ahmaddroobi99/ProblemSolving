# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        a = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)

        def build(l, r):
            if r < l:
                return None

            mid = (l + r) >> 1
            root = TreeNode(a[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        inorder(root)

        return build(0, len(a) - 1)

