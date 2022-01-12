class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        first = []
        second = []
        if n==1 and len(trust)==0:
            return 1
        for i in trust:
            first.append(i[0])
            second.append(i[1])
        x = list((set(second)-set(first)))
        if len(x)!=0:
            x = x[0]
        else:
            return -1
        if second.count(x)<n-1:
            return -1
        return x