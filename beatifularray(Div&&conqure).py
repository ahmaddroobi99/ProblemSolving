class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def helper(n):
            if n == 1:
                return [1]

            odd = helper(n // 2 + n % 2)
            even = helper(n // 2)

            return [2 * x - 1 for x in odd] + [2 * x for x in even]

        return helper(n)

