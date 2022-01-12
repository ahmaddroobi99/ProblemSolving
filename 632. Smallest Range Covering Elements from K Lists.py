class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        allNums = []
        ht = {}
        for i, nums_ in enumerate(nums):
            ht[i] = 0
            for n in nums_:
                allNums.append((n, i))

        allNums.sort(key=lambda x: x[0])

        minRange = 1000000
        count = len(nums)
        i = 0
        a = 0
        b = 0
        for j in range(len(allNums)):
            x, y = allNums[j]
            # x is the value
            # y is in the list index
            if ht[y] == 0:
                count -= 1
            ht[y] += 1
            while count == 0:
                x1, y1 = allNums[i]
                if x - x1 < minRange:
                    a, b = x1, x
                    minRange = x - x1
                if ht[y1] == 1:
                    count += 1
                ht[y1] -= 1
                i += 1

        return [a, b]