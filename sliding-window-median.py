# from sortedcontainers import SortedList
class Solution:
    #     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #         res = []
    #         sl = SortedList()
    #         for i in range(len(nums)):

    #             sl.add(nums[i])

    #             if i < k-1:
    #                 continue

    #             if k % 2:
    #                 res.append(sl[k//2]*1.0)
    #             else:
    #                 res.append((sl[(k//2)-1] + sl[k//2]) / 2.0)

    #             sl.remove(nums[i-k+1])

    #         return res

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        for i in range(len(nums) - k + 1):
            subarray = []
            for j in range(i, i + k):
                subarray.append(nums[j])
            subarray.sort()
            result.append(self.findMedian(subarray))
        return result

    def findMedian(self, subarray):
        if len(subarray) % 2 == 1:
            return subarray[len(subarray) // 2]
        else:
            mid_index = len(subarray) // 2
            median = (subarray[mid_index] + subarray[mid_index - 1]) / 2
            return median