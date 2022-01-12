class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])

        res = [[None for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = box[n - 1 - j][i]

        def gravity(k):
            start, end = m - 1, m - 1
            while start >= 0 and end >= 0:

                cnt = 0

                while end >= 0 and res[end][k] != "*":
                    if res[end][k] == "#":
                        cnt += 1
                        res[end][k] = "."
                    end -= 1

                for j in range(start, start - cnt, -1):
                    res[j][k] = "#"

                start = end
                if res[start][k] == "*":
                    start -= 1
                    end -= 1

        for i in range(n):
            gravity(i)

        return res