from collections import defaultdict


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        output = 0
        graph = defaultdict(list)
        for s, t, w in edges:
            graph[s].append((t, w + 1))
            graph[t].append((s, w + 1))

        dist = [float('inf')] * n
        dist[0] = 0
        h = [(0, 0)]

        while h:
            node, sofar = heappop(h)
            for nx, steps in graph[node]:
                totalsteps = steps + sofar
                totalsteps = steps + sofar
                if totalsteps <= dist[nx]:
                    dist[nx] = totalsteps
                    heappush(h, (nx, totalsteps))

        for s, t, w in edges:
            w1, w2 = maxMoves - dist[s], maxMoves - dist[t]
            output += max(0, w2) + max(0, w1)
            if w1 >= 0 and w2 >= 0:
                output -= max(0, w1 + w2 - w)
        output += sum([1 for d in dist if d <= maxMoves])
        return output
