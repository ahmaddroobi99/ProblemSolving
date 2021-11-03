from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rw = len(mat)
        cl = len(mat[0])
        old = rw * cl
        new = r * c

        if old != new:
            return mat

        old = [ i for e in mat for i in e]
        new = []

        a = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(old[a])
                a += 1
            new.append(temp)
            temp = []

        return new