from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        srow = [0] * rows
        scols = [0] * cols

        for x in range(rows):
            for y in range(cols):
                if mat[x][y]:
                    srow[x] += 1
                    scols[y] += 1

        count = 0
        for x in range(rows):
            for y in range(cols):
                if mat[x][y] == 1 and srow[x] == 1 and scols[y] == 1:
                    count += 1

        return count
