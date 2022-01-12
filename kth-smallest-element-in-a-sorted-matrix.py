class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        res = [0] * m * n

        for i in range(m):
            for j in range(n):
                pos = i * n + j
                res[pos] = matrix[i][j]

        res.sort()
        result = res[k - 1]
        return result
