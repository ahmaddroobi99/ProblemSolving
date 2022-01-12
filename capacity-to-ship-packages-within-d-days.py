class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            buckets = 1
            count = 0
            for w in weights:
                if count + w <= mid:
                    count += w
                else:
                    buckets += 1
                    count = w
            if buckets > days:
                left = mid + 1
            else:
                right = mid
        return right
