class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i > start:
                return False
            if nums[i] + i > start:
                start = nums[i] + i

            if start >= last:
                return True

