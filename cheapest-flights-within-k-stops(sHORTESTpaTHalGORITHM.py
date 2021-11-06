import collections
from cmath import inf
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # graph problem
        # find the minimum weight path
        # use breadth-first search and downcount k until negative
        keys = [float(inf)] * n
        keys[src] = 0
        f = collections.defaultdict(list)

        for u, v, p in flights:
            f[u].append((v, p))
        # BFS
        q = deque([(0, src)])
        while k >= 0:
            for _ in range(len(q)):
                w, node = q.popleft()
                for neighbor, price in f[node]:
                    if w + price < keys[neighbor]:  # decrease key
                        keys[neighbor] = w + price
                        q.append((keys[neighbor], neighbor))
            k -= 1

        return keys[dst] if keys[dst] != float('inf') else -1