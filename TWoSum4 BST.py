class Solution:
	def findTarget(self, root: TreeNode, k: int) -> bool:

		self.array = []

		def helper(node):

			if node==None:
				return None

			helper(node.left)
			self.array.append(node.val)
			helper(node.right)

			return self.array

		helper(root)

		for i in range(len(self.array)-1):
			for j in range(i+1,len(self.array)):
				if self.array[i] + self.array[j] == k:
					return True
		return False