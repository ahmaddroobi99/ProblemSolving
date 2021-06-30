class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Count = 0
        for i in range(len(nums)-1):
            if nums[Count] != nums[i+1]:
                Count = Count + 1
                nums[Count] = nums[i+1]
        return Count+1



