
class Solution ():


    def KnapSack(n, w, wt, profite) :
        dp = [n + 1][w + 1]
        for i in range(n):
            for j in range(w):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif wt[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j - wt[i - 1]] + profite[i - 1], dp[i - 1][j])
        print(dp[n][w])







wt =[1 ,2 ,3 ,4]
profite =[10, 20, 30, 40]
n = 4
w = 4

s = Solution()
s.KnapSack(n, w, wt, profite)
