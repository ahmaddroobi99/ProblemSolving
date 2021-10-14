class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum=sum(arr)
        if total_sum%3!=0:
            return False
        div_sum=total_sum//3
        c=0
        s=0
        for i in range(len(arr)):
            s+=arr[i]
            if s==div_sum:
                c+=1
                s=0
            if c==3:
                return True
        return c==3