# Time complexity - O(n)
# Space complexity - O(n)

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        mn = min(arr)
        mx = max(arr)
        hashset = set()
        n = len(arr)

        for i in arr:
            hashset.add(i)

        diff = mx - mn

        if diff % (n - 1) != 0:
            return False

        diff //= (n - 1)

        for j in range(0, n):
            if mn not in hashset:
                return False

            mn += diff

        return True

# Time complexity - O(nlogn)
# Space complexity - O(n)

# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         arr.sort()
#         diff = arr[1]-arr[0]
#         for i in range(1,len(arr)):
#             if arr[i]-arr[i-1] != diff:
#                 return False

#         return True