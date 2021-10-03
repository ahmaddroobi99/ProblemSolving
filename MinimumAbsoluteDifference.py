class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        max_diff = 99999999999
        l = []
        for i in range(1, len(arr)):
            curr_diff = arr[i] - arr[i - 1]
            if curr_diff == max_diff:
                l.append([arr[i - 1], arr[i]])

            elif curr_diff < max_diff:
                l.clear()
                max_diff = curr_diff
                l.append([arr[i - 1], arr[i]])

        return l
