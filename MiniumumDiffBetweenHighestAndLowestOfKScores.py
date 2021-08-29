class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, k - 1
        res = float("inf")
        while right < len(nums):
            res = min(res, nums[right] - nums[left])
            left, right = left + 1, right + 1
        return res


