class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        for x, y in zip(arr, arr[1:]):
            if len(ans) == 0:
                ans.append([x, y])
            elif (y - x) < ans[0][1] - ans[0][0]:
                ans = [[x, y]]
            elif (y - x) == ans[0][1] - ans[0][0]:
                ans.append([x, y])
        return ans

