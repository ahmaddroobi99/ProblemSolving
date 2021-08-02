class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def rec(l, r, s, c):
            if l == r == 0:
                output.append(c)
                return

            if l > 0:
                rec(l - 1, r, s + 1, c + "(")

            if r > 0 and s > 0:
                rec(l, r - 1, s - 1, c + ")")

        rec(n, n, 0, "")
        return output





