class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        result = 1

        while (result <= x):
            i += 1
            result = i * i

        return i - 1


s = Solution()
print(s.mySqrt(1256))
