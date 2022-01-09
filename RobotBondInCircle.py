class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        direc = [0, 1]

        for instruct in instructions:
            if instruct == "L":
                direc[0], direc[1] = -direc[1], direc[0]
            elif instruct == "R":
                direc[0], direc[1] = direc[1], -direc[0]
            else:
                pos[0], pos[1] = pos[0] + direc[0], pos[1] + direc[1]

        return pos == [0, 0] or direc != [0, 1]