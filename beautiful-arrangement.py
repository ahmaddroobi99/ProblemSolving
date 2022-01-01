class Solution:
    def countArrangement(self, n: int) -> int:
        graph = defaultdict(set)
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                graph[i].add(j)
                graph[j].add(i)

        def dfs(m):
            res = 0
            stack = [{m}]
            while stack:
                visited = stack.pop()

                if visited and len(visited) == n:
                    res += 1
                target = len(visited) + 1
                for i in range(1, n + 1):  # 1<=i<=n
                    if i not in visited:
                        if i % target == 0 or target % i == 0:
                            stack.append(visited | {i})
            return res

        r = 0
        for i in range(1, n + 1):
            r += dfs(i)
        return r