class Solution:

    def findLHS(self, nums: List[int]) -> int:
        if not nums: return 0
        dict = {}
        new_nums = sorted(nums)
        for x in new_nums:
            if x - 1 in dict:
                dict[x - 1] = abs(dict[x - 1])
                dict[x - 1] += 1
            if x in dict:
                dict[x] -= 1
            else:
                dict[x] = -1
        ans = max(dict.values())
        return ans if ans > 0 else 0