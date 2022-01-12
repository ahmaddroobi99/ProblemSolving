class Solution:
    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        def isSquare(x):
            sq = math.sqrt(x)
            return ((sq - math.floor(sq)) == 0)

        count = 0
        stack = []
        unique = set()
        for i, num in enumerate(A):
            if num in unique:
                continue
            else:
                unique.add(num)
                stack.append((num, A[:i] + A[i + 1:]))

        while stack:
            curr, rest = stack.pop()
            if len(rest) == 0:
                count += 1

            unique = set()
            for i, num in enumerate(rest):
                if num in unique:
                    continue
                elif isSquare(curr + num):
                    unique.add(num)
                    stack.append((num, rest[:i] + rest[i + 1:]))

        return count