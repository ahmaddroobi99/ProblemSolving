class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = {}

        for num in arr:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1

        return len(res) == len(set(res.values()))