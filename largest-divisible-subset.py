class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        res = [[]]
        for i in sorted(nums):
            temp = []
            for j in res:
                if not j or i%j[-1] == 0:
                    temp.append(j + [i])
            res.append(max(temp, key = len))
        return max(res, key = len)