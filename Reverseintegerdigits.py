class Solution:
    def reverse(self, x: int) -> int:

        temp = 0
        w = x
        if (x < 0):
            x = x * -1

        while (x > 0):
            t = x % 10
            temp = 10 * temp + t
            x = x // 10
        if (w < 0):
            temp = temp * -1

        if (
            (-2 ** 31) > temp and temp > 4294967296
        ):
            return 0
        else:
            return temp


s = Solution()

print(s.reverse(1534236655))
