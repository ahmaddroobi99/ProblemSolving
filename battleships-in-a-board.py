# class Solution:
#     # def countBattleships(self, board: List[List[str]]) -> int:


# #         if not b:
# #             return 0

# #         n, m = len(b) , len(b[0])

# #         ans=0
# #         for i in range(n):
# #             for j in range(m):

# #                 if b[i][j] == 'X':

# #                     if (i==0 or b[i-1][j]=='.') and (j==0 or b[i][j-1]=='.'):
# #                         ans+=1

# #         return ans


#     def countBattleships(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: int
#         """
#         #dfs soln
#         row,col=len(board),len(board[0])
#         def dfs(r,c):
#             if r<0 or r>=row or c<0 or c>=col or board[r][c]=='.':
#                 return
#             board[r][c]= '.'
#             dfs(r-1,c)
#             dfs(r+1,c)
#             dfs(r,c-1)
#             dfs(r,c+1)
#         count=0
#         for i in range(row):
#             for j in range(col):
#                 if board[i][j]=='X':
#                     count+=1
#                     dfs(i,j)
#         return count

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        counter = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    self.dfs(board, i, j)
                    counter += 1
        return counter

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] != "X":
            return
        board[i][j] = "#"
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)