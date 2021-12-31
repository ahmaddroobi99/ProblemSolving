class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)

        nums=sorted(set(nums))

        res=n-1

        l=0
        for r in range(1,len(nums)):
            while nums[r]-nums[l]>=n:
                l+=1
            res=min(res,n-(r-l+1))

        return  res