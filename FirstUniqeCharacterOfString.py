# Given
# a
# string
# s,
# return the
# first
# non - repeating
# character in it and
# return its
# index.If
# it
# does
# not exist,
# return -1.
# algo : simple i used a hashed map (dictionary in python ) to find the count of each letter the return the first 1 counted :>)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i

        return -1


s = Solution()
index = s.firstUniqChar('ahmad hamdan droobi')  # 11 which is n True ::
print(index)
