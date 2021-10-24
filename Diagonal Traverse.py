from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        num_rows, num_cols = len(matrix), len(matrix[0])
        diagonals = [[] for _ in range(num_rows + num_cols - 1)]

        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i + j].append(matrix[i][j])

        res = diagonals[0]
        for x in range(1, len(diagonals)):
            if x % 2 == 1:
                res.extend(diagonals[x])
            else:
                res.extend(diagonals[x][::-1])

        return res

    # other solution 2

# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

#         res = []
#         self.traverse(mat, 0, 0, res, 1)
#         return res


#     def traverse(self, mat, row, col, res, direction):

#         if (row < 0 and col < 0) or (row >= len(mat) and col >= len(mat[0])):
#             return

#         if row < 0 and col >= len(mat[0]):
#             return self.traverse(mat, row+2, col-1, res, 0)

#         if col < 0 and row >= len(mat):
#             return self.traverse(mat, row-1, col+2, res, 1)

#         if row < 0:
#             return self.traverse(mat, row+1, col, res, 0)

#         if col < 0:
#             return self.traverse(mat, row, col+1, res, 1)

#         if row >= len(mat):
#             return self.traverse(mat, row-1, col+2, res, 1)

#         if col >= len(mat[0]):
#             return self.traverse(mat, row+2, col-1, res, 0)


#         res.append(mat[row][col])
#         if direction:
#             return self.traverse(mat, row-1, col+1, res, 1)
#         else:
#             return self.traverse(mat, row+1, col-1, res, 0)

#         return
