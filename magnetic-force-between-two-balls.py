class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def verify(x):
            '''
            Returns true if we can put m balls in the buskets
            while maintining at least x distance between them
            '''
            count, prev = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= x:
                    prev = position[i]
                    count += 1
            return count >= m

        position.sort()
        low, high, ret = 1, (position[-1] - position[0]) // (m - 1) + 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if verify(mid):
                # this is a solution but we are looking for the maximum
                # update ret and continue looking for a even larger one
                ret = mid
                low = mid + 1
            else:
                high = mid - 1
        return ret