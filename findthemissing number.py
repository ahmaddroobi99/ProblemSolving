class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumEx = n * (n + 1) // 2
        sumA = sum(nums)
        return sumEx - sumA
