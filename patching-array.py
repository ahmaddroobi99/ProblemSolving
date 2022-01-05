class Solution:
    def minPatches(self, nums, n):
        i, ct, minn = 0, 0, 1
        while minn <= n:
            if i < len(nums) and nums[i] <= minn:
                minn += nums[i]
                i += 1
            else:
                minn += minn
                ct += 1
        return ct