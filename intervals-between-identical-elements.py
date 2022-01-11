from collections import defaultdict


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)
        dic2 = defaultdict(list)

        for i in range(len(arr)):
            dic[arr[i]].append(i)

        ans = []
        for i in range(len(arr)):
            interval = 0
            if arr[i] not in dic2:
                for j in dic[arr[i]]:
                    if j != i:
                        interval += abs(i - j)
                dic2[arr[i]] = (interval, i, len(dic[arr[i]]))
            else:
                intr, ind, l = dic2[arr[i]]
                temp = i - ind
                temp = temp * (l - 2)
                interval = intr - temp
                dic2[arr[i]] = (interval, i, l - 2)

            ans += [interval]

        return ans


