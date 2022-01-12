class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])  # dimensions

        def fn(low, high):
            """Return a peak element between column lo (inclusive) and hi (exlusive)."""
            if low == high: return
            mid = low + high >> 1
            if left := fn(low, mid): return left
            if right := fn(mid + 1, high): return right
            for i in range(m):
                if (i == 0 or mat[i - 1][mid] < mat[i][mid]) and (i + 1 == m or mat[i][mid] > mat[i + 1][mid]) and (
                        mid == 0 or mat[i][mid - 1] < mat[i][mid]) and (mid + 1 == n or mat[i][mid] > mat[i][mid + 1]):
                    return [i, mid]

        return fn(0, n)



    