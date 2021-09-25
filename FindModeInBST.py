# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def find_hash(root, hash):
            if not root:
                return

            if root.val in hash:
                hash[root.val] += 1

            else:
                hash[root.val] = 1

            find_hash(root.left, hash)
            find_hash(root.right, hash)

        if not root:
            return []

        hash = {}
        res = []
        find_hash(root, hash)

        max_val = max(hash.values())

        for key in hash.keys():
            if hash[key] == max_val:
                res.append(key)

        return res




