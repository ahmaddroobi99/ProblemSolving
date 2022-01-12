class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs)
        lis =[0]*len(pairs)
        lis[0] = 1
        for i in range(1,len(pairs)):
            lis[i]=1
            for j in range(0,i):
                if pairs[i][0]>pairs[j][1] and lis[i]<lis[j]+1:
                    lis[i] = lis[j]+1
        return max(lis)