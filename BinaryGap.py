class Solution:
    def binaryGap(self, n: int) -> int:
        gap = cur = 0

        while n > 0:
            if n & 1:
                gap = max(gap, cur)
                cur = 1
            elif cur:
                cur += 1
            n >>= 1

        return gap