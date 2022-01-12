class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ## RC ##
        ## APPROACH : BACKTRACKING ##

        ## TIME COMPLEXITY : O(N^2) ##
        ## SPACE COMPLEXITY : O(N^2) ##

        def backtrack(curr, nums):
            if (len(curr) >= 2 and curr[-1] < curr[-2]): return
            if (len(curr) >= 2 and curr[:] not in result):
                result.add(curr[:])
            for i in range(len(nums)):
                backtrack(curr + (nums[i],), nums[i + 1:])  # using tuples for curr instead of list

        result = set()
        backtrack((), nums)
        return result