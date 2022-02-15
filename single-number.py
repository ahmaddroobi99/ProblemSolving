# class Solution:
# 	def singleNumber(self, nums: List[int]) -> int:

# 		result = 0

# 		for i in nums:
# 			result = result ^ i

# 		return result
# Approach 2 with Counting Frequency : -
class Solution:
	def singleNumber(self, nums: List[int]) -> int:

		frequency={}

		for i in nums:
			if i not in frequency:
				frequency[i]=1
			else:
				frequency[i]=frequency[i]+1

		for i in frequency:
			if frequency[i]==1:
				return i