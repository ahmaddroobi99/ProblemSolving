class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n>=k:
            ans = ans + n%k
            n = n//k
        ans = ans+n
        return ans