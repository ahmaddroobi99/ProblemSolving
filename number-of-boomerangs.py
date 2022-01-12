class Solution:
    def numberOfBoomerangs(self, points):
        n = 0
        for a,b in points:
            counter = {}
            for x,y in points:
                # NOTE: x,y == a,b can only be registered once, so...
				#       radius=0 never has enough points to make a false triplet
                key = (x-a)**2 + (y-b)**2
                if key in counter:
                    n += 2*counter[key]
                    counter[key] += 1
                else:
                    counter[key] = 1
        return n

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        D={}
        n=len(points)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                count=0
                x1,y1,x2,y2=points[i][0],points[i][1],points[j][0],points[j][1]
                dist=sqrt((x1-x2)**2+(y1-y2)**2)
                if dist in D:
                    if i in D[dist]:
                        count+=D[dist][i]
                    if j in D[dist]:
                        count+=D[dist][j]
                if dist not in D:
                    D[dist]=defaultdict(int)
                D[dist][i]+=1
                D[dist][j]+=1
                ans+=count
        return 2*ans