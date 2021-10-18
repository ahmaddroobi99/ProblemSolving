# Search for a point 1 + 2 + 3 ..... + mid greater or equal to target. If there is leftover, continue adding l + 1, l + 2 until leftover is even so that one of the steps can be swapped by negative one.
# For example, if n = 2, l = 2 since 1 + 2 >= 3, then leftover is 3 - 2 = 1. We add 3, so leftover turns to be 4, which means +2 can be swapped by -2 to reach the target.
# The last while loop is guaranteed to be constant time.

class Solution:
    def reachNumber(self, target: int) -> int:
        # binary search
        target = abs(target)
        l, r = 1, target

        while l < r:
            mid = l + (r - l) // 2
            if (1 + mid) * mid // 2 < target:
                l = mid + 1
            else:
                r = mid
        leftover = (1 + l) * l // 2 - target
        while leftover % 2:
            leftover += l + 1
            l += 1
        return l
# Yet, we can do even better. The binary search process can be done in math in the following.

# class Solution:
#     def reachNumber(self, target: int) -> int:
#         target = abs(target)
#         l = math.ceil((-1 + math.sqrt(1 + 8 * target)) / 2)
#         leftover = (1 + l) * l // 2 - target
#         while leftover % 2:
#             leftover += l + 1
#             l += 1
#         return l