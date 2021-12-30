class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        out = []
        a = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp+=abs(a-nums[i])
        out.append(temp)
        for i in range(1,len(nums)):
            t=nums[i-1]
            temp= temp - (len(nums)-i)*(nums[i]-t)+(i)*(nums[i]-t)
            out.append(temp)
        return out