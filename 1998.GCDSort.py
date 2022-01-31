class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        UF = {}

        def find(x):
            if x not in UF: UF[x] = x
            while x != UF[x]:
                UF[x] = UF[UF[x]]
                x = UF[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            UF[x] = y

        for x in nums:
            p = 2
            y = x
            while y not in UF and p * p <= y:
                if y % p == 0:
                    union(x, p)
                    while y % p == 0: y //= p
                p += 1
            if y != 1: union(x, y)

        return all(find(x) == find(y) for x, y in zip(sorted(nums), nums))