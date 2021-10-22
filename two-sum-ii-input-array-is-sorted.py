# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         dic = {}
#         for index, value in enumerate(numbers):
#             s = target - value
#             if s in dic:
#                 return [dic[s], index+1]
#             dic[value] = index + 1
#         return r


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # initial positions of left and right pointers
        left = 0
        right = len(numbers) - 1

        # while the left pointer is not crossing the right pointer
        while (left < right):

            if (numbers[left] + numbers[right] == target):
                return [left + 1, right + 1]
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else:
                right -= 1