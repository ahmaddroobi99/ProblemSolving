class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        visited = [cols * [False] for _ in range(rows)]
        found = False

        def Go(x, y, px, py):
            visited[x][y] = True

            nonlocal found
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y] and not (nx == px and ny == py):
                    if visited[nx][ny]:
                        found = True
                    else:
                        Go(nx, ny, x, y)

        for x in range(rows):
            for y in range(cols):
                if not visited[x][y] and not found:
                    Go(x, y, -1, -1)
        return found
