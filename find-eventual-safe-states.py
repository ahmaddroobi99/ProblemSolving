class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(i):
            if color[i]:return color[i]==1
            color[i]=2
            for n in graph[i]:
                if not dfs(n):
                    return False
            color[i]=1
            return True
        output=[]
        m=len(graph)
        color=[0]*m
        for i in range(m):
            if dfs(i):output.append(i)
        return output
