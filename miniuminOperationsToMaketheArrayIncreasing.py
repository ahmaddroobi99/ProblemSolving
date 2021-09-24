class Solution:

    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        count = 0
        for i in range(1, len(nums)):
            if not (nums[i] > nums[i - 1]):
                diff = (nums[i - 1] - nums[i]) + 1
                count += diff
                nums[i] = diff + nums[i]

        return count
