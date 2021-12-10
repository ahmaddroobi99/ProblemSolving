class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def isNice(s):
            for ch in s:
                if ch.lower() not in s or ch.upper() not in s:
                    return False
            return True

        n = len(s)
        answ = ''
        for left in range(n - len(answ)):
            right = n
            while right - left > len(answ):
                if isNice(s[left:right]):
                    answ = s[left:right]
                right -= 1

        return answ