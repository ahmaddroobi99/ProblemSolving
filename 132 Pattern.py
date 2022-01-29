class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # i , j, k
        # i -> get val from min_list
        # j -> iterate through nums for each j val : nums[indx]
        # k -> get vals using stack
        min_list = []
        stack = []

        # Building Min list
        min_list.append(nums[0])

        for i in range(1, len(nums)):
            min_list.append(min(nums[:i]))

        # checking for valid patterns
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > min_list[j]:

                while stack and stack[-1] <= min_list[j]:
                    stack.pop()

                if stack and stack[-1] < nums[j]:
                    return True

                stack.append(nums[j])

        return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s2 = float('-inf')
        for i in nums[::-1]:
            if i<s2: return True
            while stack and i>stack[-1]:
                s2 = stack.pop()
            stack.append(i)
        return False