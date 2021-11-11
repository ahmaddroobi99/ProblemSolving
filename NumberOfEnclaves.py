class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rowsize = len(grid)
        colsize = len(grid[0])
        moves = 0

        def sink(row, col):
            grid[row][col] = 0

            for row_dir, col_dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                temp_row = row + row_dir
                temp_col = col + col_dir

                if (0 <= temp_row < rowsize and 0 <= temp_col < colsize) and grid[temp_row][temp_col] == 1:
                    sink(temp_row, temp_col)

        # sink lands from top and bottom borders
        for row in range(rowsize):
            if grid[row][0] == 1:
                sink(row, 0)

            if grid[row][colsize - 1] == 1:
                sink(row, colsize - 1)

        # sink lands from left and right borders
        for col in range(colsize):
            if grid[0][col] == 1:
                sink(0, col)

            if grid[rowsize - 1][col] == 1:
                sink(rowsize - 1, col)

        # looking for land to move
        for row in range(rowsize):
            for col in range(colsize):
                if grid[row][col] == 1:
                    moves += 1

        return moves