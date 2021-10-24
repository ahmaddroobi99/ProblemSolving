# One liner. Time : O(N), Space: O(N)

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         return [n for n, c in Counter(nums).items() if c == 2]
# The smart solution. Time : O(N), Space: O(1)

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         dups = []
#         for n in nums:
#             idx = abs(n) - 1
#             if nums[idx] < 0:
#                 dups.append(abs(n))
#             else:
#                 nums[idx] *= -1

#         return dups
# cyclic sort
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            idx = nums[i] - 1
            if nums[idx] != nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
            else:
                i += 1
        return [v for i, v in enumerate(nums) if v != i + 1]