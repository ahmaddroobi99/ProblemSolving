from collections import defaultdict

from astroid import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)
        ans = []
        for num in arr:
            count = 0
            n = num
            while num > 0:
                num = num & (num - 1)
                count += 1
            dic[count].append(n)
        for key in sorted(dic):
            for num in sorted(dic[key]):
                ans.append(num)

        return ans