class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            ls = list(str(num))
            num = sum([int(i) for i in ls])
            if num <= 9:
                return num
