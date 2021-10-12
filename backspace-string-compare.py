from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def load(s):
            stack = deque()
            for c in s:
                if c == '#': 
                    if stack: stack.pop()
                else: stack.append(c)
            return stack
        return load(s) == load(t)