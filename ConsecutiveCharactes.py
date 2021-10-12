class Solution:
    def maxPower(self, s: str) -> int:
        current = 1
        max_freq = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                max_freq = max(current, max_freq)
                current = 1
        return max(max_freq, current)