class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 0

        if sum(nums[1:]) == 0:
            return 0

        sm = sum(nums)
        sm -= nums[0]

        l = 0

        for i in range(length - 1):
            l += nums[i]
            sm -= nums[i + 1]
            if l == sm:
                return i + 1

        if sum(nums[:-1]) == 0:
            return n - 1

        return -1