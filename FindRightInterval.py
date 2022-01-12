class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = [(intervals[i][0], i) for i in range(n)]
        ends = [(intervals[i][1], i) for i in range(n)]
        starts.sort()
        ends.sort()
        result = [-1 for _ in range(n)]
        i = 0
        j = 0
        while i < n and j < n:
            while j < n and ends[i][0] > starts[j][0]:
                j += 1
            if j < n:
                result[ends[i][1]] = starts[j][1]
            i += 1
        return result