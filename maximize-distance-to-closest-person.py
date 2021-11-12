class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = 0
        while seats[start] == 0:
            start += 1

        end = len(seats) - 1
        while seats[end] == 0:
            end -= 1

        dist = max(start, len(seats) - 1 - end)
        prev = start
        for i in range(start + 1, end + 1):
            if seats[i]:
                if (i - prev) // 2 > dist:
                    dist = (i - prev) // 2
                prev = i

        return dist