class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        length = 1
        max_length = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] <= nums[i]:
                length = 1

            else:
                length += 1
                max_length = max(max_length, length)

        return max_length