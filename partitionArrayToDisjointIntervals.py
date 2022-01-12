class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        next_max = 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] > next_max:
                next_max = nums[i]

            if nums[i] < left_max:
                ans = i
                if next_max > left_max:
                    left_max = next_max
        return ans + 1