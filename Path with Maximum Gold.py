class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        if len(grid) == 0 or grid is None:
            return 0

        r, c = len(grid), len(grid[0])
        max_gold = 0
        current_gold = 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    current_gold = find_gold(grid, i, j, r, c, visited)
                    max_gold = max(current_gold, max_gold)

        return max_gold


def find_gold(grid, i, j, r, c, visited):
    if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] == 0 or visited[i][j]:
        return 0
    visited[i][j] = True
    up = find_gold(grid, i - 1, j, r, c, visited)
    down = find_gold(grid, i + 1, j, r, c, visited)
    left = find_gold(grid, i, j - 1, r, c, visited)
    right = find_gold(grid, i, j + 1, r, c, visited)
    visited[i][j] = False

    return max(up, max(down, max(left, right))) + grid[i][j]