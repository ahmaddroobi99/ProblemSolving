from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        mat = [[float('inf')] * cols for _ in range(rows)]  # stores min abs value of the path
        mat[0][0] = 0  # for start position it will be 0

        visited = [[False] * cols for _ in range(rows)]  # mark positions which have been processed
        minHeap = [(0, 0, 0)]  # heap to store minimum absolute value of path to reach i,j (minPathAbsVal, i, j)
        heapify(minHeap)

        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # for traversing L,R,U,D nodes of a node.

        while len(minHeap):  # process till there are elements in heap
            absVal, i, j = heappop(minHeap)  # get the node in heap with minimum abs path value
            if visited[i][j]: continue  # if node is visited, continue
            visited[i][j] = True  # mark node as visited
            for x, y in moves:  # process neighboring nodes
                r, c = i + y, j + x
                if (0 <= r < rows and 0 <= c < cols) and not visited[r][c]:
                    curAbsVal = abs(heights[i][j] - heights[i + y][j + x])  # get current absolute value of node
                    pathMaxAbsVal = max(curAbsVal, mat[i][j])  # get the max absolute value for the path
                    if pathMaxAbsVal < mat[r][
                        c]:  # check if it is less than current minimum abs path value of another path
                        mat[r][c] = pathMaxAbsVal  # if yes, update the value to current value
                        heappush(minHeap, (pathMaxAbsVal, r, c))  # push this value to the heap

        return mat[-1][-1]  # return ans