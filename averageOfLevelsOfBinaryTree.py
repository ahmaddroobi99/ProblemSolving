# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root.left and not root.right:
            return [float(root.val)]

        res, curr, nxt = [], [root], []
        while curr:
            s = 0
            for i in curr:
                if i.left:
                    nxt.append(i.left)
                if i.right:
                    nxt.append(i.right)
                s += i.val
            res.append(s / len(curr))
            curr = nxt
            nxt = []
        return (res)