class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {}

        def dfs(r, c):
            if (r, c) in visited:
                return visited[(r, c)]
            x = 1
            for i, j in dirs:
                new_r, new_c = r + i, c + j
                if 0 <= new_r < M and 0 <= new_c < N and matrix[r][c] < matrix[new_r][new_c]:
                    x = max(x, dfs(new_r, new_c) + 1)

            visited[(r, c)] = x
            return x

        output = 0
        for i in range(M):
            for j in range(N):
                output = max(output, dfs(i, j))

        return output
