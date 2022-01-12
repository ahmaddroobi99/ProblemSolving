class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            cur = abs(nums[index])
            if nums[cur] < 0:
                return cur
            nums[cur] *= -1