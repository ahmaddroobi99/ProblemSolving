from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        output = 0
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                output = max(output, dp[i][j])
        return output
