from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            nonlocal time, children, visited
            visited.add(node)
            has_apple = hasApple[node]

            for child in children[node]:
                if child not in visited:
                    descendent_has_apple = dfs(child)
                    has_apple = has_apple or descendent_has_apple

            if has_apple and node != 0:
                time += 2
            return has_apple

        time = 0
        children = [[] for _ in range(n)]
        visited = set()
        for node, child in edges:
            children[node].append(child)
            children[child].append(node)

        dfs(0)
        return time

