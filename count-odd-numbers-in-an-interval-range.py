class Solution:
    def countOdds(self, low: int, high: int) -> int:
        import math
        a = high - low + 1
        if low % 2 == 1 and high % 2 == 1:
            return math.ceil(a/2)
        return a//2