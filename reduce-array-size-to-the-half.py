class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        len_arr = len(arr)
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        listT = sorted(d, key=lambda x: d[x], reverse=True)
        sumT, count = 0, 0
        for i in listT:
            sumT += d[i]
            count += 1
            if len_arr - sumT <= len_arr // 2:
                return count


