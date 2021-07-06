# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
# dfs

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def rootLeafPath(root: TreeNode, path: str):
            path += str(root.val)
            if root.left:
                rootLeafPath(root.left, path + '->')
            if root.right:
                rootLeafPath(root.right, path + '->')
            if not root.left and not root.right:
                result.append(path)

        result = []
        rootLeafPath(root, '')
        return result
