class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for s in columnTitle:
            x = ord(s) - ord('A') + 1
            res = res * 26 + x
        return res
