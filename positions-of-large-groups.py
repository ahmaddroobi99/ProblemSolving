class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        r = 0
        n = len(s)
        ans = []
        while r < n:
            l = r
            r += 1
            while r < n and s[l] == s[r]:
                r += 1
            if r - l >= 3:
                ans.append([l, r - 1])
        return ans
