from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        dict = defaultdict(list)

        for i in range(m):
            for j in range(n):
                dict[i - j].append(mat[i][j])

        for k in dict:
            dict[k].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = dict[i - j].pop()

        return mat
