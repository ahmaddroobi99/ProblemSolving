class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        distance = float('inf')
        for indx in range(len(nums) - 2):
            l, r = indx + 1, len(nums) - 1
            new_target = target - nums[indx]
            while l < r:
                sum_val = nums[l] + nums[r]
                if abs(distance) > abs(new_target - sum_val):
                    distance = new_target - sum_val

                if sum_val == new_target:
                    return target
                elif sum_val < new_target:
                    l += 1

                else:
                    r -= 1
        return target - distance


