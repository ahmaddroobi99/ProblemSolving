# class Solution:
#     def minimumDeviation(self, A: List[int]) -> int:

#         # Store all array elements
#         # in sorted order
#         s = set([])
#         N= len(A)

#         for i in range(N):
#             if (A[i] % 2 == 0):
#                 s.add(A[i])

#             # Odd number are transformed
#             # using 2nd operation
#             else:
#                 s.add(2 * A[i])

#         # (Maximum - Minimum)

#         s = list(s)
#         diff = s[-1] - s[0]

#         # Check if the size of set is > 0 and
#         # the maximum element is divisible by 2
#         while (len(s) and s[-1] % 2 == 0):

#             # Maximum element of the set
#             maxEl = s[-1]

#             # Erase the maximum element
#             s.remove(maxEl)

#             # Using operation 1
#             s.append(maxEl // 2)

#             # (Maximum - Minimum)
#             diff = min(diff, s[-1] - s[0])

#         # Print the Minimum
#         # Deviation Obtained
#         return diff
from heapq import heappush, heappop


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        h = []
        for n in nums:
            mn = mx = n
            while mn % 2 == 0:
                mn //= 2
            if mx % 2 != 0:
                mx *= 2
            heappush(h, (mn, mx))

        MX = max([i for i, j in h])
        output = float("inf")

        while len(h) == len(nums):
            x, limit = heappop(h)
            output = min(output, MX - x)
            if x < limit:
                heappush(h, (x * 2, limit))
                MX = max(MX, x * 2)

        return output

