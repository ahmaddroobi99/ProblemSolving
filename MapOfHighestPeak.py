class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        m,n = len(isWater),len(isWater[0])
        q = collections.deque()
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    dp[i][j] = 0
                    q.append([i,j,0])

        while q:
            x,y,c = q.popleft()
            for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
                if 0<=x+i<m and 0<=y+j<n and dp[x+i][y+j]==float('inf'):
                    dp[x+i][y+j] = c+1
                    q.append([x+i,y+j,c+1])
        return dp