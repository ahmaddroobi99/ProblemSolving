class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        rev=s[::-1]
        str1=' '.join([str(e) for e in rev])
        return str1

s=Solution()
print(s.reverseWords("ahmad    hamdan droobi"))
