import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def bs(val):
            count: int=0
            for i in quantities:
                count+=math.ceil(i/val)
            return count<=n
        l,h=1,max(quantities)
        while l<h:
            mid=l+(h-l)//2
            if bs(mid):
                h=mid
            else:
                l=mid+1
        return h