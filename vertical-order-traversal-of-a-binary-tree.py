# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node, x, y):
            if node == None:
                return None
            d[x].append([y, x, node.val])
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)

            # --------main---------

        d = defaultdict(list)
        ans = []
        dfs(root, 0, 0)
        for i in sorted(d.keys()):
            ans.append([i[2] for i in sorted(d[i])])
        return ans