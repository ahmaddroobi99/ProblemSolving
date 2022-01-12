class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:

            cur = matrix[row][col]

            if target == cur:
                return True
            elif target < cur:
                col -= 1
            elif target > cur:
                row += 1

        return False

____________________________________________


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        row, col = len(matrix), len(matrix[0])
        # edge case
        if row == 0 or col == 0:
            return False
        r, c = 0, col - 1
        for i in range(row):
            if target <= matrix[i][c]:
                # binary search
                l, r = 0, col - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] == target:
                        return True
                    if target < matrix[i][mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                return False
            else:
                continue

        return False






