# Explanation
# Below implementation is based on the hint section
# Time complexity: O(M*N) since each value is visited only constant number of times (3 times: add to list, rotate, update)
# Please read the comments below for more detail
# Implementation
from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        i, j, r, c = 0, 0, m, n
        while i < r and j < c:
            values = []  # add current layer to a list for easier rotation
            for jj in range(j, c - 1):
                values.append(grid[i][jj])
            for ii in range(i, r - 1):
                values.append(grid[ii][c - 1])
            for jj in range(c - 1, j, -1):
                values.append(grid[r - 1][jj])
            for ii in range(r - 1, i, -1):
                values.append(grid[ii][j])

            kk = k % len(values)  # avoid redundant rotation
            values = values[kk:] + values[:kk]  # rotate

            idx = 0  # overwrite matrix
            for jj in range(j, c - 1):
                grid[i][jj] = values[idx]
                idx += 1
            for ii in range(i, r - 1):
                grid[ii][c - 1] = values[idx]
                idx += 1
            for jj in range(c - 1, j, -1):
                grid[r - 1][jj] = values[idx]
                idx += 1
            for ii in range(r - 1, i, -1):
                grid[ii][j] = values[idx]
                idx += 1
            i, j, r, c = i + 1, j + 1, r - 1, c - 1
        return grid