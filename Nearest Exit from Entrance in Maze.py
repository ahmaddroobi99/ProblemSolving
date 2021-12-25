class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows1, cols1 = len(maze) - 1, len(maze[0]) - 1
        empty = set()
        for r, row in enumerate(maze):
            for c, char in enumerate(row):
                if char == ".":
                    empty.add((r, c))
        start = tuple(entrance)
        empty.remove(start)
        states = {start}
        moves = 0
        while states:
            moves += 1
            new_states = set()
            for r, c in states:
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_cell = (r + i, c + j)
                    if new_cell in empty:
                        if (new_cell[0] == 0 or new_cell[0] == rows1 or
                                new_cell[1] == 0 or new_cell[1] == cols1):
                            return moves
                        empty.remove(new_cell)
                        new_states.add(new_cell)
            states = new_states
        return -1