class Solution:
    def minSwaps(self, s: str) -> int:
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] == ']':
                if l == 0:
                    r += 1
                else:
                    l -= 1
            else:
                l += 1
        if l % 2 == 0:
            res = l // 2
        else:
            res = (l + 1) // 2
        return res