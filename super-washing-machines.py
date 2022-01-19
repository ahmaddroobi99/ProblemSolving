class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        totalDresses = 0
        for d in machines:
            totalDresses += d

        N = len(machines)
        if totalDresses % N != 0:
            return -1

        goal = totalDresses / N

        maxDress = 0
        current = 0

        for dress in machines:
            current += dress - goal
            maxDress = max(abs(current), maxDress)
            maxDress = max((dress - goal), maxDress)

        return int(maxDress)
