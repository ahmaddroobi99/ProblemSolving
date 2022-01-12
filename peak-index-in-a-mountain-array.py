class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        j = 0
        for i in range(0, len(arr)):
            if arr[i] > arr[i + 1]:
                j = i
                break

        return j