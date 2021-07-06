class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = n
        s = 0
        x = x//5
        s += x
        while(x >= 5):
            x = x//5
            s += x
        return s


s = Solution()
print(s.trailingZeroes(1000))
print(s.trailingZeroes(10))
