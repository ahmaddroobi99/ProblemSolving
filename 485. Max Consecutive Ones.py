class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            rt = 0
            s = 0
            for x in nums:
                if x:
                    s+=1
                    continue
                rt = max(rt, s)
                s = 0
            return max(rt, s)