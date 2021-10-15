class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = set(nums)
        for i in nums:
            if nums.count(i) > 1 and i in s:
                s.remove(i)
        return sum(s)



class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = {}
        for i in nums:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        s1 = 0
        for k,v in s.items():
            if v == 1:
                s1 = s1 + k
        return s1
