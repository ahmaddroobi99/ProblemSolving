class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        col = len(isConnected[0])
        city=defaultdict(list)

        for r in range(row):
            for c in range(col):
                if isConnected[r][c]==1:
                    city[r].append(c)
                    city[c].append(r)

        cc=0
        vis=[0]*row

        def dfs(a):
            vis[a]=1
            if a not in city:
                return
            for j in city[a]:
                if vis[j]==0:
                    dfs(j)

        for i in range(row):
            if vis[i]==0:
                cc=cc+1
                dfs(i)
        return cc