class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        count = 0

        def checker(arr):
            r1 = sum(arr[0])
            r2 = sum(arr[1])
            r3 = sum(arr[2])
            c1 = (arr[0][0]) + (arr[1][0]) + (arr[2][0])
            c2 = (arr[0][1]) + (arr[1][1]) + (arr[2][1])
            c3 = (arr[0][2]) + (arr[1][2]) + (arr[2][2])
            d1 = arr[0][0] + arr[1][1] + arr[2][2]
            d2 = arr[0][2] + arr[1][1] + arr[2][0]
            print(r1, r2, r3, c1, c2, c3, d1, d2)
            if r1 == r2 and r2 == r3 and r3 == c1 and c1 == c2 and c2 == c3 and c3 == d1 and d1 == d2:
                return True
            return False

        s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                gr = [grid[r][j:j + 3] for r in range(i, i + 3)]
                if set([gr[k][l] for k in range(3) for l in range(3)]) == s:
                    if checker(gr):
                        count += 1
        return count