# from math import ceil
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         diag = [row[i] for i,row in enumerate(mat)]
#         c_diag = [row[-i-1] for i,row in enumerate(mat)]
#         if len(mat[0]) % 2 == 0:
#             ans = sum(diag) + sum(c_diag)
#         else:
#             i = ceil(len(mat[0]) / 2)
#             diag[i-1] = 0
#             ans = sum(diag) + sum(c_diag)
#         return ans

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat)==1:
            return mat[0][0]
        i = 0
        j = len(mat)-1
        ret = 0
        for row in mat:
            ret+=(row[i]+row[j] if i!=j else row[i])
            i+=1
            j-=1
        return ret