class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        Mod = 10 ** 9 + 7
        c = a * b // gcd(a, b)

        def f(x):
            return ((x - 1) // a) + ((x - 1) // b) - ((x - 1) // c)

        left = 0
        right = 10 ** 14
        while left < right:
            mid = (left + right + 1) // 2
            if f(mid) > n - 1:
                right = mid - 1
            else:
                left = mid
        return left % Mod
