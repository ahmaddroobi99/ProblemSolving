class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)

        nums.sort()
        m1 = nums[0] % x

        for i in nums:
            if i % x != m1: return -1
        median = nums[len(nums) // 2]
        print(median)
        res = 0
        for n in nums:
            res += abs(n - median) // x
            print(res)

        return res