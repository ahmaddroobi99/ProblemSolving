class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sumA = 1
        for i in nums:
            sumA *= i

        if sumA == 0:
            return 0
        elif sumA > 0:
            return 1
        else:
            return -1



