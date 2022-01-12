class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        percent  = int(len(arr)*0.05)
        return sum(arr[percent:-percent])/len(arr[percent:-percent])