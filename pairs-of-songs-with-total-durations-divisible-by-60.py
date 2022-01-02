class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
            c = 0
            d = {}
            for i in range(len(time)):
                x = time[i]%60
                a = 0
                if x>0:
                    a = 60-x
                if a in d:
                    c+=d[a]
                if x in d:
                    d[x]+=1
                else:
                    d[x]=1
            return c