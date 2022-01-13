class Solution(object):
    def splitString(self, s):
        n = len(s)

        def go(index, last):
            if index == n:
                return True
            can = False
            for i in range(index + 1, len(s) + 1):
                if int(s[index:i]) == last - 1:
                    can = go(i, last - 1)
                if can:
                    return can
            return can

        for x in range(1, len(s)):
            if go(x, int(s[:x])):
                return True
        return False