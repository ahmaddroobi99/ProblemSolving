import numpy as np
class Solution :
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            if np.allclose(mat, target):
                return True
            mat = np.rot90(mat)

        return False

    import numpy as np
    class Solution:
        def findRotation(self, a: List[List[int]], target: List[List[int]]) -> bool:
            n = len(a[0])

            def rotate():
                for i in range(n // 2):
                    for j in range(i, n - i - 1):
                        temp = a[i][j]
                        a[i][j] = a[n - 1 - j][i]
                        a[n - 1 - j][i] = a[n - 1 - i][n - 1 - j]
                        a[n - 1 - i][n - 1 - j] = a[j][n - 1 - i]
                        a[j][n - 1 - i] = temp
                return a

            return any(target == rotate() for _ in range(4))