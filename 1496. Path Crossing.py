class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0,0)
        visited = {pos:True}
        for i in path:
            if i == 'N':
                pos = (pos[0],pos[1] + 1)
            elif i == 'S':
                pos = (pos[0],pos[1] - 1)
            elif i == 'E':
                pos = (pos[0] + 1,pos[1])
            else:
                pos = (pos[0] - 1,pos[1])
            if pos not in visited.keys():
                visited[pos] = True
            else:
                return True
        return False