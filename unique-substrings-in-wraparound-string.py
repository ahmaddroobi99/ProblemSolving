class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [1] * len(p)

        for i in range(1, len(p)):
            if (ord(p[i]) == (ord(p[i - 1]) + 1)) or (p[i] == 'a' and p[i - 1] == 'z'):
                dp[i] = dp[i - 1] + 1

        s = {}
        for i in range(len(p)):
            if p[i] in s:
                s[p[i]] = max(s[p[i]], dp[i])
            else:
                s[p[i]] = dp[i]

        return sum(s.values())