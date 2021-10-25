class Solution:
    def lastRemaining(self, n: int) -> int:
        l, r, turn, step = 1, n, True, 1
        while n > 1:
            if turn:
                l += step
                r = r - step if n % 2 else r
            else:
                r -= step
                l = l + step if n % 2 else l
            turn = not turn
            n = n // 2
            step = step << 1

        return l