class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(x):
            if x==1:
                return False
            for i in range(2,x):
                if x%i==0:
                    return False
            return True
        c=0
        for j in range(left, right+1):
            if prime(bin(j)[2:].count('1')):
                c+=1
        return c
