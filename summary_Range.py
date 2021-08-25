class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for num in nums:
            if not res or num != res[-1][-1] + 1:
                if res and len(res[-1]) >= 2:
                    res[-1] = [res[-1][0]] + [res[-1][-1]]
                res.append([num])
            else:
                res[-1].append(num)

        if res and len(res[-1]) >= 2:
            res[-1] = [res[-1][0]] + [res[-1][-1]]

        return ['->'.join(map(str, x)) for x in res]



