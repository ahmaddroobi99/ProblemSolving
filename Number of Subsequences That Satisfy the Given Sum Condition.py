from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        ans = 0

        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += 2 ** (r - l)
                l += 1
            else:
                r -= 1

        mod = 10 ** 9 + 7
        return ans % mod
