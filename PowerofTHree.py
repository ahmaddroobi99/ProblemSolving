def isPowerOfThree(self, n: int) -> bool:
    # 3^0
    if n == 1:
        return True

    i = 3
    while i <= n:
        if i == n:
            return True
        i *= 3

    return False
