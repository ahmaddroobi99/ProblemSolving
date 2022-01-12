class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		result, count = [], 0
		for i in range(len(nums)):
			result.append(count+nums[i])
			count+=nums[i]
		return result