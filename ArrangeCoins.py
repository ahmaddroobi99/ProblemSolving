class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (right + left) // 2
            mid_val = (mid * (mid + 1) // 2)
            if mid_val == n:
                return mid
            elif mid_val < n:
                left = mid + 1
            else:
                right = mid - 1
        return right

