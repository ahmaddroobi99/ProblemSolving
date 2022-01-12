# Solution 1:
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones_len = zeros_len = 0
        left = right = 0
        while right < len(s)+1:
            if right == len(s) or s[right] != s[left]:
                if s[left] == '0':
                    zeros_len = max(zeros_len, right-left)
                else:
                    ones_len = max(ones_len, right-left)
                left = right
            right += 1
        return ones_len > zeros_len
# Solution2:

# class Solution:
#     def checkZeroOnes(self, s: str) -> bool:
#         max_ones_len = max_zeros_len = 0
#         cur_ones_len = cur_zeros_len = 0
#         for d in s:
#             if d == '1':
#                 cur_ones_len += 1
#                 cur_zeros_len = 0
#             else:
#                 cur_zeros_len += 1
#                 cur_ones_len = 0
#             max_ones_len = max(max_ones_len, cur_ones_len)
#             max_zeros_len = max(max_zeros_len, cur_zeros_len)
#         return max_ones_len > max_zeros_len