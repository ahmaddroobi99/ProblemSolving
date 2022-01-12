class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def getangle(P1, P2):
            ydif = p2[1] - p1[1]
            xdif = p2[0] - p1[0]

            if xdif == 0:
                return sys.maxsize

            return ydif / xdif

        ans = 0
        n = len(points)
        for i in range(n):
            p1 = points[i]
            same = 0
            angles = []
            for j in range(n):
                if i != j:
                    p2 = points[j]
                    if p1 == p2:
                        same += 1
                    else:
                        angles.append(getangle(p1, p2))
            counter = Counter(angles)
            max1 = 0
            if counter.values():
                max1 = max(counter.values())

            ans = max(ans, max1 + same + 1)

        return ans





