class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = str(x) == str(x)[::-1]
        return c


s = Solution()
print(s.isPalindrome(123321))
print(s.isPalindrome(-6205506))
