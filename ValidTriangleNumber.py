def triangleNumber(self, nums: List[int]) -> int:
    ans = 0
    nums.sort()
    for i in reversed(range(1, len(nums))):
        l, r = 0, i - 1
        while l < r:
            if nums[l] + nums[r] > nums[i]:
                ans += r - l
                r -= 1
            else:
                l += 1
    return ans