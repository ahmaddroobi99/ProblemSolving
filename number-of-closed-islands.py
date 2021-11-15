from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        queue = []
        m = len(grid)
        n = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    grid[i][j] = 1
                    isClosed = True

                    while queue:
                        cur_i, cur_j = queue.pop()

                        if cur_i in (0, m - 1) or cur_j in (0, n - 1):
                            isClosed = False

                        for d in directions:
                            new_i = cur_i + d[0]
                            new_j = cur_j + d[1]

                            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0:
                                queue.append((new_i, new_j))
                                grid[new_i][new_j] = 1

                    if isClosed:
                        ans += 1
        return ans




