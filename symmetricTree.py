class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is not None:
            return self.util(root.left, root.right)

    def util(self, left, right):
        if left is not None and right is not None:
            if left.val == right.val:
                return self.util(left.right, right.left) and self.util(left.left, right.right)

            else:
                return False

        if left is None and right is None:
            return True

        return False