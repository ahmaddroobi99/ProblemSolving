class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        R, C = len(grid), len(grid[0])

        @lru_cache(None)
        def recurse(r, c):
            if r >= R:
                return c  # return the c you are in.

            if grid[r][c] == -1:
                next_col = grid[r][c - 1] if c - 1 >= 0 else 0
                if next_col == grid[r][c]:
                    return recurse(r + 1, c - 1)
            else:
                next_col = grid[r][c + 1] if c + 1 < C else 0
                if next_col == grid[r][c]:
                    return recurse(r + 1, c + 1)

            return -1

        res = []
        for c in range(C):
            res.append(recurse(0, c))

        return res