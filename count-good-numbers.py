class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        fours = int(n/2)
        fives = int(fours + (n%2))
        p5 = int(pow(4, fours, MOD))
        p4 = int(pow(5, fives, MOD))
        return (p4*p5) % MOD