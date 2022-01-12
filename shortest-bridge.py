import collections


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.indexes_1 = set()

        for i in range(len(grid)):
            flag = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    flag = 1
                    break
            if flag:
                break

        start_queue = collections.deque([(i, j, 0) for i, j in self.indexes_1])
        min_path = self.bfs(grid, start_queue)

        return min_path

    def bfs(self, grid, start_queue) -> int:
        visited = set()
        queue = start_queue

        while queue:
            i, j, path = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            current = grid[i][j]
            if current == 1:
                return path-1

            if i < len(grid) - 1:
                queue.append((i + 1, j, path + 1))

            if i > 0:
                queue.append((i - 1, j, path + 1))

            if j < len(grid[0]) - 1:
                queue.append((i, j + 1, path + 1))

            if j > 0:
                queue.append((i, j - 1, path + 1))

        return -1

    def dfs(self, grid, i, j):
        if i > len(grid) - 1 or i < 0 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] in {0, 2}:
            return

        grid[i][j] = 2
        self.indexes_1.add((i, j))
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)