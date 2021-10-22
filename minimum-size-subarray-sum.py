from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j, sub_sum, sub_len = 0, 0, 0, float('inf')
        while i < len(nums):
            if sub_sum < s:
                sub_sum += nums[i]
                i += 1
            while sub_sum >= s:
                if i - j < sub_len:
                    sub_len = i - j
                sub_sum -= nums[j]
                j += 1

        return 0 if sub_len == float('inf') else sub_len