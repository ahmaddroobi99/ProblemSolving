class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            if n % 2 == 1:
                count += 1
            n = n // 2

        return count






