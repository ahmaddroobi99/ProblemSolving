class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        inx = len(nums)//2
        for i in nums:
            if i!= nums[inx]:
                total+=abs(i-nums[inx])
        return total