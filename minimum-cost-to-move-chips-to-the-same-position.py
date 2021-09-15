class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        e = 0
        o = 0
        for i in position:
            if (i % 2 != 0):
                o += 1
            else:
                e += 1
        return o if o < e else e
