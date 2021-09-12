class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prodNum = 1
        sumNum = 0

        while True:
            prodNum *= n % 10
            sumNum += n % 10

            n = n // 10
            if n == 0:
                break

        return prodNum - sumNum

