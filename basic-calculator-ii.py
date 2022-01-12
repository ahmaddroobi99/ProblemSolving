class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        arr = []
        i = 0
        # First Make It An Array Of Proper Operations
        while i < len(s):
            if s[i] not in '*+/-':
                start = i
                while i < len(s) and s[i] not in '*+/-':
                    i += 1
                arr.append(s[start:i])
            else:
                arr.append(s[i])
                i += 1

            # handle multiple and divide
        for i in arr:
            if stack and stack[-1] == '*':
                stack.pop()
                val = stack.pop()
                ans = int(val) * int(i)
                stack.append(str(ans))
            elif stack and stack[-1] == '/':
                stack.pop()
                val = stack.pop()
                ans = int(val) // int(i)
                stack.append(str(ans))
            else:
                stack.append(i)
        if len(stack) == 1:
            return int(stack[-1])
        ans = 0
        prev = 0

        # handle plus and minus
        for i in range(1, len(stack) - 1):
            if i == 1:
                if stack[i] == '+':
                    ans += int(stack[i - 1]) + int(stack[i + 1])
                    prev = int(stack[i - 1]) + int(stack[i + 1])
                elif stack[i] == '-':
                    ans += int(stack[i - 1]) - int(stack[i + 1])
                    prev = int(stack[i - 1]) - int(stack[i + 1])
            elif i > 1:
                if stack[i] == '+':
                    ans = prev + int(stack[i + 1])
                    prev = ans
                elif stack[i] == '-':
                    ans = prev - int(stack[i + 1])
                    prev = ans

        return ans