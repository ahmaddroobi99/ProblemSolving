# class Solution:
#     def sumOddLengthSubarrays(self, arr) -> int:
#         total = 0
#         i = 1
#         j = 0
#         while i <= len(arr):
#             while j < len(arr) and i + j <= len(arr):
#                 total += sum(arr[j:j + i])
#                 j += 1
#             i += 2
#             j = 0
#         return total

class Solution :
     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
            Sum=0
            for i in range(len(arr)):
                Sum += ((((i + 1) *
                      (len(arr) - i) +
                     1) // 2) * arr[i])
            return Sum