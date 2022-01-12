class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
        stack = []
        visited = set()
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] -= 1
            if s[i] not in visited:
                while stack and stack[-1]>s[i] and count[ord(stack[-1])-ord('a')]:
                    visited.remove(stack[-1])
                    stack.pop()
                visited.add(s[i])
                stack.append(s[i])
        return "".join(stack)