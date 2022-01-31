
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        PositiveList=[]
        NegativeList=[]
        res=[]
        for i in nums:
            if(i<0):
                NegativeList.append(i)
            else:
                PositiveList.append(i)
        for i in range (len(nums)//2):
            res.append(PositiveList[i])
            res.append(NegativeList[i])
        return (res)