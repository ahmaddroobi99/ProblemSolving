class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = []
        s+='$'
        last = s[0]
        temp = 0
        for i in range(len(s)):
            if last!=s[i]:
                c.append(temp)
                last = s[i]
                temp = 1
            else:
                temp+=1
        req = 0
        for i in range(len(c)-1):
            req+=min(c[i], c[i+1])
        return req