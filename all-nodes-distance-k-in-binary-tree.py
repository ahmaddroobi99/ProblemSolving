# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque, defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)
        # create undirected graph
        stack = [root]
        while stack:
            node = stack.pop()
            if node == target:
                targetVal = node.val
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)

        # start BFS
        q = deque([(targetVal, 0)])  # startNode distance=0
        seen = set()
        seen.add(targetVal)
        res = []
        while q:
            node, depth = q.popleft()
            if depth == k:
                res.append(node)
            if depth > k: break  # no need to continue

            for neigh in graph[node]:
                if neigh not in seen:
                    q.append((neigh, depth + 1))
                    seen.add(neigh)
        return res