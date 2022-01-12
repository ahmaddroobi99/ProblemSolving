class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = len(board), len(board[0])
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        queue = [click]

        while queue:
            next_queue = []
            for (x0, y0) in queue:
                mine = 0
                for nei in neighbors:
                    x = x0 + nei[0]
                    y = y0 + nei[1]
                    if 0 <= x < row and 0 <= y < col:
                        if board[x][y] == 'M':
                            mine += 1
                if mine > 0:
                    board[x0][y0] = str(mine)
                else:
                    board[x0][y0] = 'B'
                    for nei in neighbors:
                        x = x0 + nei[0]
                        y = y0 + nei[1]
                        if 0 <= x < row and 0 <= y < col:
                            if board[x][y] == 'E':
                                board[x][y] = 'E1'  # mark seen
                                next_queue.append([x, y])
            queue = next_queue.copy()
        return board