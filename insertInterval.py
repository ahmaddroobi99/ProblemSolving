class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newIntervals = []

        # start with the new interval and fit the interval list around it
        newIntervals.append(newInterval)

        for interval in intervals:
            # there are three steps. Once the step is completed, it will not hit that
            # condition again because the intervals are sorted

            # 1. case where the new interval is greater than the current interval.
            # we would want to insert the new interval behind the current interval
            if (interval[1] < newIntervals[-1][0]):
                backup = newIntervals[-1]
                newIntervals[-1] = interval
                newIntervals.append(backup)
            # 2. once all the intervals that are less than the new interval are inserted,
            # we have to check if we need to merge. Take the widest range by taking
            # min(current interval start, last interval start) to max(current interval end, last interval end)
            # repeat this until there is no more overlap
            elif (interval[0] <= newIntervals[-1][1]):
                newIntervals[-1][0] = min(interval[0], newIntervals[-1][0])
                newIntervals[-1][1] = max(interval[1], newIntervals[-1][1])
            # 3. append the rest of the intervals. There is no more logic here because the new
            # interval has been inserted and merged.
            else:
                newIntervals.append(interval)
        return newIntervals