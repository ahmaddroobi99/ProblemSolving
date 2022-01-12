# IDEA :
# We have to read question litle carefully. After reading first some of us can think this problem as of graph problem.

# But If we read and see that we have to count number of computers which all are not alone in their row and columns.
# So we can directly go through whole grid and can store the number of computers in the specific row and column by making two arrays as rows and cols.
# After counting this we can go again and check for the number of single computer in the specific rows and cols.
# Finally return total - cnts.
# '''

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    total += 1

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    cnt += 1

        return total - cnt