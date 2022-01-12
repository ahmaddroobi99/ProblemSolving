class Solution:
    def check(self, nums: List[int]) -> bool:
        found = False
        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx - 1]:
                if found or nums[-1] > nums[0]:
                    return False
                found = True

        return True
