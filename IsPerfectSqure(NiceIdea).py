# validate if the number is perfect squre
# binary search Algorithm


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low <= high:
            mid = (low+high) >> 1    # div by 2 the same as shift by two , Ok?
            if mid*mid > num:
                high = mid-1
            elif mid*mid < num:
                low = mid+1
            else:
                return True
        return False


s = Solution()
print(s.isPerfectSquare(963))
print(s.isPerfectSquare(10000))
