# Count
# the
# number
# of
# prime
# numbers
# less
# than
# a
# non - negative
# number, n.
# its a bad algorithm but this is the first solution appear in my head :(

class Solution:
    def countPrimes(self, n: int) -> int:
        ctr = 0

        for num in range(n):
            if num <= 1:
                continue
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                ctr += 1

        return ctr


s = Solution()
print(s.countPrimes(10))
print(s.countPrimes(100))
print(s.countPrimes(1000))
print(s.countPrimes(10000))
print(s.countPrimes(100000))
