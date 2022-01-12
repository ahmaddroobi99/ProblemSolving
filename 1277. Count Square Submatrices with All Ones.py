class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        count = 0
        for col in range(width):
            count += matrix[0][col]

        for row in range(1, height):
            count += matrix[row][0]

        for row in range(1, height):
            for col in range(1, width):
                if matrix[row][col] == 1 and matrix[row - 1][col] > 0 and matrix[row][col - 1] and matrix[row - 1][
                    col - 1] > 0:
                    matrix[row][col] += min(matrix[row - 1][col - 1], matrix[row - 1][col], matrix[row][col - 1])
                count += matrix[row][col]

        return count