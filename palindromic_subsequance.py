class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1+(s!=s[::-1])