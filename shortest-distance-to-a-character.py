class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        left, right, output = [None] * N, [None] * N, [None] * N
        tmp = float("inf")
        for i in range(N):
            if s[i] == c:
                tmp = 0
            left[i] = tmp
            tmp += 1
        tmp = float("inf")
        for i in range(N - 1, -1, -1):
            if s[i] == c:
                tmp = 0
            right[i] = tmp
            tmp += 1

        for i in range(N):
            output[i] = min(right[i], left[i])
        return output