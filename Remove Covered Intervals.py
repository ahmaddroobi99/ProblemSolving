class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))

        res = [intervals[0]]

        for l, r in intervals[1:]:
            preL, preR = res[-1]
            if preL <= l and preR >= r:
                continue

            res.append([l, r])
        return len(res)



