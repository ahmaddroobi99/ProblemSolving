class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        for i in range(0, len(s), 2 * k):
            a = i + k
            b = i + 2*k
            res += s[i:a][::-1] + s[a:b]
        return res