import collections


class Solution:
    def subarraysWithKDistinct(self, nums, k):
            return self.atMostK(nums, k) - self.atMostK(nums, k-1)

        def atMostK(self,nums,k):
            count = collections.Counter()
            res = i = 0

            for j in range(len(nums)):
                if count[nums[j]] == 0:
                    k -= 1

                count[nums[j]] += 1

                while k < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        k += 1
                    i += 1

                res += j - i + 1

            return res