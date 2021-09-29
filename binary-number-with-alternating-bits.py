class Solution:
    def hasAlternatingBits(self, num: int) -> bool:
        flage = True
        while (num > 0):
            temp = num % 2
            num = num // 2
            if (num % 2 == temp):
                return False

        return flage

