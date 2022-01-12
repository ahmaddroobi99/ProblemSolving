# Water can only be trapped if the adjacent elements have height larger than the height of the current cell. To do this, we first look at the i = 0 , j = 0, i = n-1, j = m-1 rows, we marks these nodes as visited, and add then to a min heap. We then start popping elements from the min heap, the first element would be the boundary element with the least height, we then look at its all 4 adjacent neighbours, using (dx, dy), and (i, j), when we find a neighbour which has height less than the popped element's height, we add the difference between them into the resultant array, since this node has been visited, we add this as well to the heap as well, but when we do this, we add this with curH as max boundary avaiable, since that will be the boundary value that we will be looking at, otherwise, if the popped element is less than the current element, water cannot be trapped between them, we just add this element to the heap.
import heapq


class Solution(object):
    def trapRainWater(self, heightMap):

        if not heightMap:
            return 0

        n = len(heightMap)
        m = len(heightMap[0])

        h = []
        grid = [[0] * m for _ in range(n)]
        re = 0

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    grid[i][j] = 1
                    heapq.heappush(h, (heightMap[i][j], i, j))

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        while h:
            curh, i, j = heapq.heappop(h)
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or y < 0 or x >= n or y >= m:
                    continue
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    if curh > heightMap[x][y]:
                        re += curh - heightMap[x][y]
                        heapq.heappush(h, (curh, x, y))
                    else:
                        heapq.heappush(h, (heightMap[x][y], x, y))

        return re