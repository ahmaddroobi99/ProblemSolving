# Idea:
# The key to this problem is realizing that we're dealing with overlapping triangular number issues. Importantly, the total number of possible subarrays that are contained within any larger subarray is the Nth triangular number, where N is the length of that larger subarray.

# So the nums array starts with the (nums.length)th triangular number total subarrays. We want to exclude any subarray that includes a number larger than right, however. The easiest way to do this is to consider numbers larger than right to be dividers, splitting nums into many subarrays. We can add the triangular number for each of these resulting subarrays together to be the total number of subarrays that exclude numbers higher than right.

# To do this, we can iterate through nums and keep track of how many contiguous numbers are less than right (mid) and each point that mid increments, we can add mid to ans, representing the increase to the next triangular number. The value for mid will then reset whenever we see a number higher than right.

# But this only does half of the problem, because we still have to also exclude any subarray that does not have any number at least left high. To do this, we can use a similar method as for mid. We can keep track of how many contiguous numbers are lower than left (low) and decrease ans by that amount every time it increments, representing the next triangular number. Similar to mid, low will reset whenever we see a number at least left high.

# Once we're done iterating, we can return ans.

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, low, mid = 0, 0, 0
        for num in nums:
            if num > right: mid = 0
            else:
                mid += 1
                ans += mid
            if num >= left: low = 0
            else:
                low += 1
                ans -= low
        return ans