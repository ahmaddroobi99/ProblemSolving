class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, m, n = 0, 0, len(nums1), len(nums2)
        curNums1Sum, curNums2Sum = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                curNums1Sum += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                curNums2Sum += nums2[j]
                j += 1
            else:
                curNums1Sum = curNums2Sum = max(curNums1Sum, curNums2Sum) + nums1[i]
                i += 1
                j += 1

        curNums1Sum += sum(nums1[i:])
        curNums2Sum += sum(nums2[j:])

        return max(curNums1Sum, curNums2Sum) % (10 ** 9 + 7)