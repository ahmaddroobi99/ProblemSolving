class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        prem = []
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if (len(prem)) == len(nums):
                res.append(prem.copy())
                return
            for n in count:
                if count[n] > 0:
                    prem.append(n)
                    count[n] -= 1

                    dfs()
                    count[n] += 1
                    prem.pop()

        dfs()
        return res