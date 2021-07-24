class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = total_sum = nums[0]

        for i in nums[1:]:
            total_sum = max(i, total_sum + i)
            max_sum = max(max_sum, total_sum)

        return max_sum


