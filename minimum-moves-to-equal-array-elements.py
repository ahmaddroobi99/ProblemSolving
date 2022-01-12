class Solution:
	def minMoves(self, nums: List[int]) -> int:
		ele = min(nums)
		sum = 0
		for num in nums:
			sum += num-ele
		return sum