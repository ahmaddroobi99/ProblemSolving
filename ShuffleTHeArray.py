class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        stack = []
        for i in range(n):
            stack.append(nums[i])
            stack.append(nums[i + n])
        return stack

