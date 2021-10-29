class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		result = []

		def dfs(subset = [], index = 0):

			if index == len(nums):
				result.append(subset)
				return

			dfs(subset + [nums[index]], index + 1)
			dfs(subset, index + 1)

		dfs()
		return result