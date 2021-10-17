class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        isInc = False
        isDes = False
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                    isInc = True
            elif nums[i - 1] > nums[i]:
                isDes = True

        return False if isInc and isDes else True