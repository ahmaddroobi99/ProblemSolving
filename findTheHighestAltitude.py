class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = [0]

        for height in gain:
            maximum.append(maximum[-1] + height)

        return max(maximum)