# class Solution:
#     def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
#         def calc(l,r,u,d):
#             ssum =0
#             c1=c2=(l+r)//2
#             expand=True
#             for row in range (u,d+1):
#                 if c1==c2:
#                     ssum+=grid[row][c1]
#                 else :
#                     ssum += grid[row][c1]+grid[row][c2]
#                 if c1==1 :
#                     expand= False
#                 if expand :
#                     c1-=1
#                     c2+=1
#                 else:
#                     c1+=1
#                     c2-=1
#             return ssum

#         m= len(grid)
#         n =len(grid[0])
#         pq=[]

#         for i in range(m):
#             for j in range(n):
#                 l=r=j
#                 d=i
#                 while l>=0 and r<= n-1 and d<= m-1 :
#                     ssum =calc(l,r,i,d)
#                     l-=1
#                     r+=1
#                     d+=2
#                     if len(pq) < 3 :
#                         if ssum not in pq :
#                             heapq.heappush(pq,ssum)
#                     else :

#                         if ssum not in pq and ssum >pq[0]:
#                             heapq.heappop(pq)
#                             heapq.heappush(pq,ssum)


#         pq.sort(reverse =True)
#         return pq

class Solution(object):
    def getBiggestThree(self, grid):
        def calc(l, r, u, d):
            ssum = 0
            expand = True
            c1 = c2 = (l + r) // 2

            for row in range(u, d + 1):
                if c1 == c2:
                    ssum += grid[row][c1]
                else:
                    ssum += grid[row][c1] + grid[row][c2]
                if c1 == l:
                    expand = False
                if expand:
                    c1 -= 1
                    c2 += 1
                else:
                    c1 += 1
                    c2 -= 1
            return ssum

        m = len(grid)
        n = len(grid[0])
        pq = []

        for i in range(m):
            for j in range(n):
                l = r = j
                d = i
                while l >= 0 and r < n and d < m:
                    ssum = calc(l, r, i, d)
                    l -= 1
                    r += 1
                    d += 2

                    if len(pq) < 3:
                        if ssum not in pq:
                            heapq.heappush(pq, ssum)
                    else:
                        if ssum not in pq and ssum > pq[0]:
                            heapq.heappop(pq)
                            heapq.heappush(pq, ssum)
        pq.sort(reverse=True)
        return pq