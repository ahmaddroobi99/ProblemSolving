class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact, digits = [1] * n, [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * (i + 1)
            digits[i] = i + 1

        result = ""
        while len(result) < n - 1:
            repeat = fact[-2]
            next_digit = (k - 1) // repeat
            result += str(digits[next_digit])
            digits.pop(next_digit)
            fact = fact[:-1]
            k = k % repeat
            if k == 0:
                for i in range(len(digits) - 1, -1, -1):
                    result += str(digits[i])

        if len(result) < n:
            result += str(digits[0])

        return result
