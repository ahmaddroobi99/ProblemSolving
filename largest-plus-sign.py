class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        left, right = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
        up, down = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
        m = set(tuple(l) for l in mines)
        for r in range(n):
            for c in range(n):
                if (r, c) in m:
                    left[r][c] = 0
                    up[r][c] = 0
                elif r == 0 or c == 0:
                    left[r][c] = 1
                    up[r][c] = 1

                else:
                    left[r][c] += left[r][c - 1] + 1
                    up[r][c] += up[r - 1][c] + 1

                nr, nc = n - r - 1, n - c - 1

                if (nr, nc) in m:
                    right[nr][nc] = 0
                    down[nr][nc] = 0
                elif nr == (n - 1) or nc == (n - 1):
                    right[nr][nc] = 1
                    down[nr][nc] = 1
                else:
                    right[nr][nc] += right[nr][nc + 1] + 1
                    down[nr][nc] += down[nr + 1][nc] + 1

        out = 0
        for r in range(n):
            for c in range(n):
                out = max(out, min(right[r][c], left[r][c], up[r][c], down[r][c]))
        return out




