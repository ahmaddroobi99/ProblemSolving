class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def helper(index=1, a=[]):
            if len(a) == k:
                output.append(a.copy())
                return

            for i in range(index, n + 1):
                a.append(i)
                helper(i + 1, a)
                a.pop()

        helper()
        return output



