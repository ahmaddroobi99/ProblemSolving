def divide(self, dividend: int, divisor: int) -> int:
    d = abs(dividend)
    div = abs(divisor)
    res = 0
    while d >= div:
        tmp = div
        n = 1
        while d >= tmp:
            d -= tmp
            res += n
            n += n
            tmp += tmp
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        res = -res

    if -2 ** 31 <= res <= 2 ** 31 - 1:
        return res
    elif res > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return -2 ** 31