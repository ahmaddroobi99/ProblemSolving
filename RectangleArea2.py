from bisect import insort
from cmath import inf


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        line = []
        for x1, y1, x2, y2 in rectangles:
            line.append((y1, x1, x2, 1))
            line.append((y2, x1, x2, 0))

        ans = yy = val = 0
        seg = []
        for y, x1, x2, tf in sorted(line):
            ans += val * (y - yy)
            yy = y
            if tf:
                insort(seg, (x1, x2))
            else:
                seg.remove((x1, x2))
            val = 0
            prev = -inf
            for x1, x2 in seg:
                val += max(0, x2 - max(x1, prev))
                prev = max(prev, x2)
        return ans % 1_000_000_007