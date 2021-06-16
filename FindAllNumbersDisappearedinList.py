# Given
# an
# array
# nums
# of
# n
# integers
# where
# nums[i] is in the
# range[1, n],
# return an
# array
# of
# all
# the
# integers in the
# range[1, n]
# that
# do
# not appear in nums.
#
# Example
# 1:
#
# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [5, 6]

#the idea is traverse in the list mul every element by -1 make it negative then add to list the positive elementin the range of 0-n
# those are the missing elements ...:)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []

        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] = -nums[temp]

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans
