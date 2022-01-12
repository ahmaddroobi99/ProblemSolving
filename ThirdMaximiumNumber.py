# Using set
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]
        else:
            return nums[-1]

# Using pointers
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         nums.sort()

#         if len(nums) < 3:
#             return nums[-1]

#         i = len(nums)
#         count = 3
#         max_ele = nums[-1]

#         while i > 0:
#             if count == 1:
#                 return max_ele

#             if nums[i-1] != max_ele:
#                 max_ele = nums[i-1]
#                 count -= 1

#             i -= 1

#         if count == 1:
#             return nums[i]
#         else:
#             return nums[-1]


