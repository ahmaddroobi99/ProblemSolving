# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting
# some (can be none) of the characters without disturbing the relative
# positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# idea  Two pointers traverse each string then deleting (replacing the not in the orignal str) then Find if it there's or not
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) == 0:
            return True
        while i < len(t) and j < len(s):

            if t[i] == s[j]:
                i = i + 1
                j = j + 1
            else:
                t = t.replace(t[i], '', 1)
        if t.find(s) == -1:
            return False
        else:
            return True


s = Solution()
bool = s.isSubsequence('ahmad', 'achmkakuddpppo')  # true

print(bool)
