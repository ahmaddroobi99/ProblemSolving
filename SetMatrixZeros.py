class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero, colZero, M, N = 1, 1, len(matrix), len(matrix[0])
        for i in range(M):
            if matrix[i][0] == 0:
                rowZero = 0
                break
        for i in range(N):
            if matrix[0][i] == 0:
                colZero = 0
                break
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, M):
            if matrix[i][0] == 0:
                for j in range(1, N):
                    matrix[i][j] = 0
        for j in range(1, N):
            if matrix[0][j] == 0:
                for i in range(1, M):
                    matrix[i][j] = 0
        if rowZero == 0:
            for i in range(M):
                matrix[i][0] = 0
        if colZero == 0:
            for j in range(N):
                matrix[0][j] = 0