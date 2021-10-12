class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        # For n=1, base case
        res = [10]

        for i in range(1, n):
            combinations = 9
            for j in range(0, i):
                combinations = combinations * (9 - j)
            res.append(res[-1] + combinations)

        return res[-1]