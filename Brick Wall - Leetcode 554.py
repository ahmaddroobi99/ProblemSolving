class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGaps = {0: 0}

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countGaps[total] = 1 + countGaps.get(total, 0)
        return len(wall ) - max(countGaps.values())