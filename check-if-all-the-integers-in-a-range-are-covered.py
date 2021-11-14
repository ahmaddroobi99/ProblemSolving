class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        c=0
        for i in range(left, right + 1):
            for j,k in ranges:
                if j<=i and i<=k:
                    c+=1
                    break
        return c==(right-left)+1