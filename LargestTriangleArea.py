## Solution 1
import itertools
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
# use itertools.combinations to save code amount
# S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        return max(f(a, b, c) for a, b, c in itertools.combinations(points, 3))

## Solution 2
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
# use formula and don't forget to use absolute value
        res = 0
        N = len(points)
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(i + 2, N):
                    (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                    res = max(res, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return res