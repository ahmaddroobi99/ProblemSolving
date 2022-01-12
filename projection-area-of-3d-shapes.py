class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        p = len(grid)
        x, y, c = [], [0]*p, 0
        for i in range(p):
            x.append(0)
            for j in range(p):
                n = grid[i][j]
                if n > 0:
                    c += 1
                if x[i] < n:
                    x[i] = n
                if y[j] < n:
                    y[j] = n

        return (sum(x)+sum(y)+c)