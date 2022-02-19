from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
	# approach 1
	# using sort()

#         out = []
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 out.append(i)
#         return out

	# approach 2
	# without using sort

        c_ele, c_small_ele = 0, 0
        for ele in nums:
            if ele == target:
                c_ele += 1
            elif ele < target:
                c_small_ele += 1
        return [i + c_small_ele for i in range(c_ele)]