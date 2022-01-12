class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        a, b, c = 0, 1, 1
        for _ in range(1, n):
            c = a + b
            a, b = b, c
        return c