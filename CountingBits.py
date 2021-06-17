class Solution:

    def countBits(self, num: int) :
        c=[]
        for i in range(0,num+1):
            t=bin(i).replace("0b","")
            x=t.count('1')
            c.append(x)
        return c

s=Solution()
print(s.countBits(5))