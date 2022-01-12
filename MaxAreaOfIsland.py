from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def recur(i, j):
            grid[i][j] = 2

            area = 1
            if i - 1 >= 0 and grid[i - 1][j] == 1: area += recur(i - 1, j)
            if i + 1 < len(grid) and grid[i + 1][j] == 1: area += recur(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == 1: area += recur(i, j - 1)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1: area += recur(i, j + 1)

            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, recur(i, j))
        return max_area