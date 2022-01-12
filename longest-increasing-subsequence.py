

# #Dynamic Programming solution O(N^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


# Binary Search O(N logN_)
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []

        for num in nums:
            insertion_pos = bisect_left(arr, num)

            if insertion_pos == len(arr):
                arr.append(num)
            else:
                arr[insertion_pos] = num

        return len(arr)
