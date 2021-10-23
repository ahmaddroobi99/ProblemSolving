# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """

#         s = set()

#         for i in nums:
#             if i not in s:
#                 s.add(i)
#             else:
#                 s.remove(i)
#         return list(set(s))


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        a = []
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in nums:
            if dic[i] == 1:
                a.append(i)
        return a