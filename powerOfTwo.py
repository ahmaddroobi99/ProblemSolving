class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x=0
        while 2**x<=n:
            if(2**x==n):
                return True
            x+=1
        return False

s=Solution()
print(s.isPowerOfTwo(9999))
print(s.isPowerOfTwo(1024))


# solution 2

class Solution:
	def isPowerOfTwo(self, n: int) -> bool:
		while n:
				if n==1 or n==2:
					 return(True)
				n=n/2
				if 1<n<2:
					return(False)

print(s.isPowerOfTwo(9999))
print(s.isPowerOfTwo(1024))