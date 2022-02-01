class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m = collections.defaultdict(int)

        for num in arr:
            m[num] += 1

        s = sorted(m[x] for x in m)
        index = 0
        while k > 0 and index < len(s):
            k -= s[index]
            index += 1

        if k != 0:
            index -= 1
        return len(s) - index
