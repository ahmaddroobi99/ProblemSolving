from typing import List


class TreeNode:
    def TreeNode(self,val=0,left=None,right=None):
        self.val= val
        self.left=left
        self.right=right




class Solution :
    def boundaryOfBinaryTree (self,root:TreeNode)->List[int]:

        def dfs_leftmost (node):
            if not node.right and not node.left:
                return
            result.append(node.val)
            if node.left:
                dfs_leftmost(node.left)

            elif  node.right :
                dfs_rightmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)


            if node!=root and not node.left and not node.right:
                result.append(node.val)

            dfs_leaves(node.right)



        def dfs_rightmost(node):
            if not node.right and not node.left:
                return
            if node.right :
                dfs_rightmost(node.right)
            elif node.left :
                dfs_leftmost(node.left)

            result.append(node.val)


        result = [root.val]

        if root.left:
            dfs_leftmost(root.left)
        if root.right :
            dfs_rightmost(root.right)

        return result





