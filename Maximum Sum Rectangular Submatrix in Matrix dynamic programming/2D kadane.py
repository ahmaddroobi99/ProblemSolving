from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])
        dp1 = [[matrix[i][j] for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp1[i][j] += dp1[i][j - 1]
                elif j == 0:
                    dp1[i][j] += dp1[i - 1][j]
                else:
                    dp1[i][j] += dp1[i - 1][j] + dp1[i][j - 1] - dp1[i - 1][j - 1]

        def get_sum(i, i2, j):
            return dp1[i2][j] - (dp1[i - 1][j] if i != 0 else 0)


        maxx = -10 ** 9
        for i in range(n):
            for i2 in range(i, n):
                sl = SortedList([0])

                for j in range(m):
                    summ = get_sum(i, i2, j)
                    ind = sl.bisect_left(summ - k)
                    if ind != len(sl):
                        maxx = max(maxx, summ - sl[ind])
                    sl.add(summ)
        return maxx