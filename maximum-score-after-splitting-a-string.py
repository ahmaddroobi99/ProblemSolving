import math


class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count('1')
        res = -math.inf
        for i in range(len(s) - 1):
            if s[i] == '0':
                score += 1
            else:
                score -= 1
            res = max(res, score)
        return res