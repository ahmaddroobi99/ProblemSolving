# Idea:
# The idea is to increase the building as high as the minimum between max_height(row) and max_height(col), and sum the difference between the current building height and the intended building height.
#
# Implementation:
#
# start by initializing common variables, like sums for return value, rows and cols to define maximum row and columns
# Calculate the maximum height for each row and column, store it in max_row and max_col
# Iterate through each building, summing the difference between min of max_row and max_col
# on the particular row and column, with the building height.
# return the sum
class Solution(object):
	def maxIncreaseKeepingSkyline(self, grid):
		sums, rows, cols = 0, len(grid), len(grid[0])
		max_row, max_col = map(max, grid), map(max, zip(*grid))
		for row in range(rows):
			for col in range(cols):
				sums += min(max_row[row], max_col[col])-grid[row][col]
		return sums