class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        p1, p2, res, seenZeros = 0, 0, 0, 0

        while p2 < len(nums):
            if nums[p2] == 0:
                seenZeros += 1
                while seenZeros > k:
                    seenZeros = seenZeros - 1 if nums[p1] == 0 else seenZeros
                    p1 += 1

            res = max(res, p2 - p1 + 1)
            p2 += 1
        return res