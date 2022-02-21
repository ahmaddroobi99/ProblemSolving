from collections import Counter
from heapq import heappushpop, heappush
from typing import List


# class Solution:
#     def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         for i,j in enumerate(nums):
#             if len(result)==k:
#                 heappushpop(result,(j,i))
#             else:
#                 heappush(result,(j,i))
#         print(result)
#         ans = []
#         result.sort(key=lambda x:x[1])
#         for i in result:
#             ans.append(i[0])
#         return ans
#
# s= Solution()
# print(s.maxSubsequence([1,2,3,6,5,8],3))


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        x = sorted(nums, reverse=True)
        s = Counter(x[:k]) # get largest k num
        print(s)
        res = []
        # To be in order so the extra step is needed
        for num in nums:
            if s[num] > 0:
                res.append(num)
                s[num] -= 1
        return res


s= Solution()
print(s.maxSubsequence([2,1,3,3], 2))
