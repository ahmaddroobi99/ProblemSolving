class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + (j - i) // 2  # cal the middle point
            if target == nums[m]:
                return m
            elif target > nums[m]:
                i = m + 1
            elif target < nums[m]:
                j = m - 1
        else:
            return i