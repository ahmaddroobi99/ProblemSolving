class Solution:
    s = []

    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


s = ['a', 'h', 'm', 'a', 'd']
w = Solution()
oo = w.reverseString(s)
print(oo)
