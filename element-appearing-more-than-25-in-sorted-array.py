from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        times = int(0.25*len(arr))
        hcount = Counter(arr)
        for k,c in hcount.items():
            if c>times:
                return k
        return


class Solution:
        def findSpecialInteger(self, arr: List[int]) -> int:
            for num in arr:
                if arr.count(num) > len(arr) / 4:
                    return num