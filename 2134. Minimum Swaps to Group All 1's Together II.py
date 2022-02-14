# Call this number total. We should then check for every subarray of size total (possibly wrapped around), how many swaps are required to have the subarray be all 1’s.
# ~~
# The number of swaps required is the number of 0’s in the subarray.
# ~~
# To eliminate the circular property of the array, we can append the original array to itself. Then, we check each subarray of length total.
# ~~
# How do we avoid recounting the number of 0’s in the subarray each time? The Sliding Window technique can help.
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        ones = nums.count(1)  # Time: O(N)
        nums = nums + nums
        ones_in_window = 0
        res = 0
        for i in range(len(nums)):  # Time: O(N)
            if i >= ones:
                ones_in_window -= nums[i - ones]
            ones_in_window += nums[i]
            res = max(ones_in_window, res)

        return (ones - res)

# Time: O(N) + O(N)
# Space: O(2 * N) = O(N)