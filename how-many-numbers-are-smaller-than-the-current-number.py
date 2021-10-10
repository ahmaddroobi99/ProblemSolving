class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        q={}
        a=nums[:]
        a.sort(reverse=True)
        for i in range(len(a)):
            q[a[i]]=i
        result=[]
        for i in range(len(nums)):
            y=q[nums[i]]
            result.append(len(a)-y-1)
        return result
