class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 1, 0
        while max(i, j) < len(nums):
            if not nums[i] & 1 and nums[j] & 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
                continue
            if nums[i] & 1:
                i += 2
            if not nums[j] & 1:
                j += 2
        return nums