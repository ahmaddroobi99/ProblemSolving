class Solution(object):
    def thousandSeparator(self, n):

        n = str(n)[::-1]
        res = ''
        for i in range(len(n)):
            if i % 3 == 0 and i > 0:
                res = res + '.' + n[i]
            else:
                res = res + n[i]
        return ''.join(res)[::-1]