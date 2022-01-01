from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = max(Counter(nums).values())
        left, shortest = 0, len(nums)
        counter = Counter()
        for right, num in enumerate(nums):
            counter[num]+=1
            while counter[num] == degree:
                shortest = min(shortest, right-left+1)
                counter[nums[left]]-=1
                left+=1
        return shortest