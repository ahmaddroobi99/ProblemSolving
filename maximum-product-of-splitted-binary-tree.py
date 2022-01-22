class Solution:
    def __init__(self):
        self.total = 0
        self.res = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def totalsum(node):
            if node:
                self.total += node.val
            if node.left:
                totalsum(node.left)
            if node.right:
                totalsum(node.right)

        def postorder(node, curr_sum):
            a, b = 0, 0
            if node.left:
                a = postorder(node.left, curr_sum)
            if node.right:
                b = postorder(node.right, curr_sum)
            curr_sum += node.val + a + b
            self.res = max(curr_sum * (self.total - curr_sum), self.res)
            return curr_sum

        totalsum(root)
        postorder(root, 0)
        return self.res % ((10 ** 9) + 7)
    