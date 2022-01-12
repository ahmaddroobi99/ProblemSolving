class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        l = len(nums)
        tmp = 1

        for n in range(30):  # num = 0~10**9 < 2**30
            count = 0
            for k in range(l):
                if (nums[k] & tmp):  # kth bit is 1.
                    count += 1

            ans += count * (l - count)
            tmp <<= 1

        return ans

