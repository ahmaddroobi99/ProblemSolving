# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:
#         if n ==0 :
#             return False
#         for x in range (1, math.floor(math.sqrt(n))+1):
#             if not self.winnerSquareGame(n-(x*x)):
#                 return True
#         return False
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        squares = []
        curSquare = 1
        for i in range(1, n + 1):
            if i == curSquare * curSquare:
                squares.append(i)
                curSquare += 1
                dp[i] = True
            else:
                for square in squares:
                    if not dp[i - square]:
                        dp[i] = True
                        break
        return dp[n]