from typing import List


class Solution:
    def construct2DArray(self, arr: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if len(arr) != m * n: return []
        k = 0
        for i in range(m):
            temp = [0] * n
            for j in range(n):
                temp[j] = arr[k]
                k += 1
            res.append(temp)

        return res