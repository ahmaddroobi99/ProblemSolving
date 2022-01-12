class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        rowPreSum = []

        for i in range(m):
            rowpresum = {-1: 0}
            for j in range(n):
                rowpresum[j] = rowpresum[j - 1] + grid[i][j]
            rowPreSum.append(rowpresum)

        colPreSum = []
        for j in range(n):
            presum = {-1: 0}
            for i in range(m):
                presum[i] = presum[i - 1] + grid[i][j]

            colPreSum.append(presum)

        ans = 1
        for i in range(m):
            for j in range(n):
                for length in range(2, min(m - i, n - j) + 1):
                    ssum = rowPreSum[i][j + length - 1] - rowPreSum[i][j - 1]
                    diagonal = antidiagonal = 0
                    flag = True
                    for l in range(length):
                        row = rowPreSum[i + l][j + length - 1] - rowPreSum[i + l][j - 1]
                        if row != ssum:
                            flag = False
                            break
                        col = colPreSum[j + l][i + length - 1] - colPreSum[j + l][i - 1]
                        if col != ssum:
                            flage = False
                            break

                        diagonal += grid[i + l][j + l]
                        antidiagonal += grid[i + l][j + length - l - 1]

                    if flag and diagonal == antidiagonal == ssum:
                        ans = max(ans, length)

        return ans







