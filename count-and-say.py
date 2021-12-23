class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(1, n):
            j = 0
            temAns = ''
            n = ans[j]
            count = 0
            while j < len(ans):
                if n == ans[j]:
                    count += 1
                else:
                    temAns += '{}{}'.format(count, n)
                    count = 1
                    n = ans[j]
                j += 1
            if count != 0:
                temAns += '{}{}'.format(count, n)

            ans = temAns
        return ans