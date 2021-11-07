class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right, s, count):
            while left < right:
                if s[left] != s[right]:
                    if count == 1:
                        return False
                    return isPalindrome(left + 1, right, s, count + 1) or isPalindrome(left, right - 1, s, count + 1)
                left += 1
                right -= 1
            return True

        return isPalindrome(0, len(s) - 1, s, 0)