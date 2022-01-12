from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        N, M = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        lives = [[-1 for j in range(M)] for i in range(N)]
        q = deque()
        q.append([0, 0, k, 0])
        # visited =set()

        while len(q) > 0:
            cr, cc, clives, cdist = q.popleft()
            if cr == N - 1 and cc == M - 1:
                return cdist
            if grid[cr][cc] == 1:
                # continue
                clives -= 1
            for direction in directions:
                nr, nc = cr + direction[0], cc + direction[1]
                if 0 <= nr < N and 0 <= nc < M and lives[nr][nc] < clives:
                    q.append([nr, nc, clives, cdist + 1])
                    # visited.add((nr,nc))
                    lives[nr][nc] = clives

        return -1
