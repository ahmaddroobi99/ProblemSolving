from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d = {}
        arr.sort()
        print(arr)
        for i in range(0, len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        print(d)

        for key in d:
            if d[key] == 0:
                continue
            if key < 0:
                target = key // 2
            else:
                target = key * 2

            if target not in d:
                return False

            if key < 0 and key % 2 != 0:
                return False

            if d[key] > d[target]:
                return False
            else:
                d[target] = d[target] - d[key]
        return True
