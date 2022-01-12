class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [[root.val]] if root.val == targetSum else []

        left = self.pathSum(root.left, targetSum - root.val)
        right = self.pathSum(root.right, targetSum - root.val)
        res = []

        for path in left:
            res.append([root.val] + path)

        for path in right:
            res.append([root.val] + path)

        return res