class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = sorted(set(arr))

        s = dict()
        for i in range(len(rank)):
            s[rank[i]] = i + 1

        ans = []
        for i in arr:
            num = s[i]
            ans.append(num)

        return ans

