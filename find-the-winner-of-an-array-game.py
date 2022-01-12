class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max, c = arr[0], 0
        for i in range(1, len(arr)):
            if (arr[i] < max):
                c = c + 1
            else:
                max, c = arr[i], 1
            if (c == k): break
        return max

# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:

#         n = len(arr)

#         if n <= k :
#             return max(arr)

#         res = 0
#         maxNum = arr[0]
#         for i in range(1,n):
#             if maxNum > arr[i]:
#                 res += 1
#             else:
#                 maxNum = arr[i]
#                 res = 1

#             if res == k:
#                 return maxNum

#         return maxNum


# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:
#         # if k is larger than or equal to the length of arr
#         # the maximum of arr must be the answer
#         if k >= len(arr):
#             return max(arr)

#         # do what is described and record the number of win
#         winner, win = arr.pop(0), 0
#         while True:
#             tmp = arr.pop(0)
#             if tmp > winner:
#                 arr.append(winner)
#                 winner, win = tmp, 1
#             else:
#                 arr.append(tmp)
#                 win += 1
#             if win == k:
#                 return winner