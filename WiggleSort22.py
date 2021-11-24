# # Sort the list
# # Find the mid and Insert mid, last element in the first two position of the list and pop the inserted elements
# # Recursively call the wiggle function with the remaining part of the list and repeat it till the list length is less than or equal to 2
# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         nums.sort()
#         self.wiggle(nums, 0)

#     def wiggle(self, nums, start):

#         if (len(nums[start:]))<=2:
#             return nums
#         mid = int(len(nums[start:])/2)
#         if len(nums[start:])%2 != 0:
#             mid = mid+1
#         i = start+mid-1
#         j = len(nums)-1

#         nums.insert(start, nums[i])
#         nums.insert(start+1, nums[j+1])
#         nums.pop(i+2)
#         nums.pop(j+1)
#         start+=2
#         self.wiggle(nums, start)

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums, reverse=True)
        if len(temp) % 2 == 0:
            mid = len(temp) // 2
        else:
            mid = (len(temp) // 2) + 1
        j = 0
        for i in range(1, len(temp), 2):
            nums[i] = temp[j]
            j += 1
            if j == mid:
                break
        for i in range(0, len(temp), 2):
            nums[i] = temp[j]
            j += 1
            if j == len(nums):
                break