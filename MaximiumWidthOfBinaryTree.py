# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #         if root==None :
        #             return 0
        #         q=[(root,0)]
        #         width =1
        #         while len(q) != 0 :
        #             if len(q)> 1 :
        #                 width =max(width, q[-1][1]-q[0][1]+1)
        #                 temp_q=[]
        #                 while len(q)!=0 :
        #                     node ,position = q.pop(0)
        #                     if node.left !=None :
        #                         temp_q.append((node.left,position*2))

        #                     if node.right !=None :
        #                         temp_q.append((node.right,position*2 + 1))

        #                 q= temp_q
        #         return width
        if not root: return 0
        q = [[root, 1]]
        maxWidth = 0
        while q:
            maxWidth = max(maxWidth, q[-1][1] - q[0][1] + 1)  # find the difference for upcomming queue
            for _ in range(len(q)):
                curr, idx = q.pop(0)
                if curr.left: q.append((curr.left, idx * 2))
                if curr.right: q.append((curr.right, idx * 2 + 1))
        return maxWidth