class Solution:
    def longestPalindrome(self, s: str) -> int:

        counts = Counter(s)
        res = 0
        foundOdd = False

        for val in counts.values():
            if val % 2 == 0:
                res += val
            else:
                foundOdd = True
                res += val - 1

        return res + 1 if foundOdd else res