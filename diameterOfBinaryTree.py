class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = []

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            ans.append(l + r)
            return 1 + max(l, r)

        dfs(root)
        return max(ans)