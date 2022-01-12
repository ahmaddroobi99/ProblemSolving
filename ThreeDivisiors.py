class Solution:
    def isThree(self, n: int) -> bool:

        count = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                if n / i == i:  # for distinct divisors
                    count += 1
                else:
                    count += 2

            if count > 3:
                return False

        return count == 3