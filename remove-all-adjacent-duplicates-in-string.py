# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         p,stack=0,[]
#         while p<len(s):
#             currLetter=s[p]
#             if stack:
#                 lastLetter=stack.pop()

#                 if currLetter!=lastLetter : #if not = add both, else dont add anything
#                     stack.append(lastLetter)
#                     stack.append(currLetter)
#             else: #if stack is empty put
#                 stack.append(currLetter)
#             p+=1
#         return "".join(stack)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
