class Solution:
    def beautySum(self, s: str) -> int:
        suma=0
        for i in range(0,len(s)-2):
            maxi,mini=0,0
            d={}
            j=i

            while j<len(s):
                if s[j] in d.keys():
                    d[s[j]]+=1
                else:
                    d[s[j]]=1
                j+=1
                maxi=max(d.values())
                mini=min(d.values())
                if mini!=0:
                    suma+=maxi-mini

        return suma