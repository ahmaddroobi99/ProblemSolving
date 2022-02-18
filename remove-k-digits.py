class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i, N = 0, len(num)

        stack = []
        if k >= N:
            return "0"

        while (i < N):
            while (stack and k > 0 and int(stack[-1]) > int(num[i])):
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while (k > 0):
            stack.pop()
            k -= 1

        return str(int("".join(stack)))