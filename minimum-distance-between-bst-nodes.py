# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l=[]
        def makelist(root,l):
            if root:
                l.append(root.val)
                if root.left:
                    makelist(root.left,l)
                if root.right:
                    makelist(root.right,l)
            return l
        a=sorted(makelist(root,l))
        b=[]
        for i in range(len(a)-1):
            b.append(abs(a[i]-a[i+1]))
        return min(b)