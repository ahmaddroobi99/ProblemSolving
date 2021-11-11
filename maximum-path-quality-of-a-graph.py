from collections import defaultdict


class Solution:
    def maximalPathQuality(self, values, E, maxTime):
        G = defaultdict(list)
        for x, y, w in E:
            G[x].append((y, w))
            G[y].append((x, w))

        def dfs(node, visited, gain, cost):
            if node == 0: self.ans = max(self.ans, gain)
            for neib, w in G[node]:
                if w <= cost:
                    dfs(neib, visited | set([neib]), gain + (neib not in visited) * values[neib], cost - w)

        self.ans = 0
        dfs(0, set([0]), values[0], maxTime)
        return self.ans