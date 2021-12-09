# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startNode = None
        self.endNode = None

        def createParent(root, parent):
            if not root:
                return

            root.parent = parent
            createParent(root.left, root)
            createParent(root.right, root)

            if root.val == startValue:
                self.startNode = root
            if root.val == destValue:
                self.endNode = root

            return

        createParent(root, None)

        queue = [(self.startNode, "")]
        visited = set()
        visited.add(self.startNode.val)

        while queue:
            node, value = queue.pop(0)

            if node == self.endNode:
                return value

            if node.parent and node.parent.val not in visited:
                queue.append((node.parent, value + "U"))
                visited.add(node.parent.val)

            if node.right and node.right.val not in visited:
                queue.append((node.right, value + "R"))
                visited.add(node.right.val)

            if node.left and node.left.val not in visited:
                queue.append((node.left, value + "L"))
                visited.add(node.left.val)

        return ""