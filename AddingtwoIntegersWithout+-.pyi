class Solution:
    def getSum(self, a: int, b: int) -> int:
        xor =a^b
        carry =a&b
        if carry ==0:
            return xor

        else:
            return add(xor,carry<<1)

