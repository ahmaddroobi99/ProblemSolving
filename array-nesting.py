class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)

        visited = set()
        maxd = 1
        for i in range(n):
            prev = i
            curr = nums[prev]
            if prev not in visited:
                d = 0
                while prev != curr and prev not in visited:
                    visited.add(prev)
                    prev = curr
                    curr = nums[prev]
                    d += 1

                maxd = max(maxd, d)

        return maxd