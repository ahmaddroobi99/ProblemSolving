
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        min=len(nums)/3
        op=[]
        s=set(nums)
        for num in s:
            if(nums.count(num)>min):
                op.append(num)
        return op