# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


class Solution:
    def isHappy(self, n: int) -> bool:

        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)

            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10
            n = _sum

        return n == 1


s=Solution()
print(s.isHappy(2021))
print(s.isHappy(97))
print(s.isHappy(44))
print(s.isHappy(79))
print(s.isHappy(10))
print(s.isHappy(7))
print(s.isHappy(130))

