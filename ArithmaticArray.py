class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            x = temp[1] - temp[0]
            flag = False
            for j in range(1, len(temp)):
                if temp[j]-temp[j-1] != x:
                    flag = True
                    break
            if flag:
                ans.append(False)
            else:
                ans.append(True)
        return ans