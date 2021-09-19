from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = len(nums)
        an=[]
        for i in range(0,l):
            if nums[i] == target:
                an.append(abs(i-start))
        return min(an)