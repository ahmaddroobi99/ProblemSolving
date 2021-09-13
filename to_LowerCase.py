class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for i in s:
            if ord(i) >= 65 and ord(i) <=90:
                res+=chr(ord(i)+32)
            else:
                res+=i
        return res