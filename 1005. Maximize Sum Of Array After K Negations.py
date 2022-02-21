class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] < 0 and k > 0 :
            nums[i] = -1 * nums[i]
            i += 1
            k -= 1
            if k == 0:
                return sum(nums)
        if k % 2 == 1:
            return sum(nums) - (2 * (min(nums)))
        return sum(nums)