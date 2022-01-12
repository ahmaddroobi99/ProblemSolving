class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        per = sum(matchsticks)

        if per % 4 != 0:
            return False
        else:
            side = per // 4

        matchsticks.sort(reverse=True)

        def dfs(a, b, c, d, k):
            if k == N:
                if a == b == c == d:
                    return True
                return False

            m = matchsticks[k]

            if a + m <= side and dfs(a + m, b, c, d, k + 1):
                return True
            if b + m <= side and dfs(a, b + m, c, d, k + 1):
                return True
            if c + m <= side and dfs(a, b, c + m, d, k + 1):
                return True
            if d + m <= side and dfs(a, b, c, d + m, k + 1):
                return True
            return False

        return dfs(0, 0, 0, 0, 0)

