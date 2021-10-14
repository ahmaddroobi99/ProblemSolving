class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def helpp(y):
            return (abs(r0 - y[0]) + abs(c0 - y[1]))
        res = []
        i = -1
        j = -1
        for row in range(R):
            i += 1
            j = -1
            for col in range(C):
                j += 1
                res.append([i,j])
        res.sort(key = helpp)
        return res