class Solution:
    def findNthDigit(self, n: int) -> int:

        a, b, start = self.__find_index(n)
        return str(start + a - 1)[-1] if not b else str(start + a)[b - 1]

    def __find_index(self, n: int) -> (int, int, int):

        cnt_digit, cnt_zone, start = 1, 9, 1
        while n > cnt_zone * cnt_digit:
            n -= cnt_zone * cnt_digit
            cnt_digit += 1
            cnt_zone *= 10
            start *= 10
        a, b = divmod(n, cnt_digit)

        return a, b, start