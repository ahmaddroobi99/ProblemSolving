class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        temp = 0
        for key, value in d.items():
            if key == value:
                if key > temp:
                    temp = key

        if temp != 0:
            return temp
        else:
            return -1