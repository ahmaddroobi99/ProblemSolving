# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         total =0
#         for i in range (len (nums)-1):
#             c= 1
#             diff =nums[i+1]-nums[i]
#             for i in range(i+2,len(nums)-1,1):
#                 j=i+2
#                 if nums[j]-nums[j-1]==diff :
#                     total+=1
#                 else :
#                     break

#         return total


class Solution:
    # def numberOfArithmeticSlices(self, A: List[int]) -> int:
    #     left, right, ans = 0, 2, 0
    #     while right < len(A):
    #         while right<len(A) and A[left+1]-A[left]==A[right]-A[right-1]:
    #             ans += right-left-1
    #             right += 1
    #         left = right - 1
    #     return ans

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp, ans = defaultdict(int), 0
        for i in range(2, len(A)):
            if A[i - 2] - A[i - 1] == A[i - 1] - A[i]:
                dp[i] += dp[i - 1] + 1
        return sum(dp.values())