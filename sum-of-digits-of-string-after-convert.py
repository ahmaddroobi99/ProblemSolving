class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sumStr = ""
        for i in s:
            sumStr += str(ord(i)-96)

        while k:
            sumStr = sum([int(i) for i in str(sumStr)])
            k -= 1

        return sumStr