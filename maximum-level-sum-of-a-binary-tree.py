# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue, level = collections.deque([root]), 0
        max_sum, max_level = float("-Inf"), 1

        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                curr_sum += curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            level += 1

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = level

        return max_level