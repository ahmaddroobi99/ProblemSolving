class Solution:
    def numPermsDISequence(self, s: str):
        l = []

        for i in range(len(s)+1):
            l.append(i)

        for i in l:
            map(i, l)
        for k, v in w:
            print(k, v)


s = Solution()
s.numPermsDISequence('did')
