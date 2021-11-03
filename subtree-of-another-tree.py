# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if cur.val == subRoot.val:
                if self.isSame(cur, subRoot):
                    return True

    def isSame(self, p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                return p.val == q.val and self.isSame(p.right, q.right) and self.isSame(p.left, q.left)