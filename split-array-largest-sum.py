class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isPossible(s):
            splits = 0
            cur_sum = 0

            for num in nums:
                cur_sum += num
                if cur_sum > s:
                    splits += 1
                    cur_sum = num
                    if splits > m - 1:
                        return False
            return True

        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2
            if isPossible(mid):
                high = mid
            else:
                low = mid + 1

        return low

