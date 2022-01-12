class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        idx, m1, m2 = -1, -1, -1

        for i, n in enumerate(nums):
            if n > m1:
                idx, m1, m2 = i, n, m1
            elif n > m2:
                m2 = n

        return idx if (m1 >= 2*m2) else -1