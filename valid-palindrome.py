# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         str = ""
#         for i in s:
#             if i.isalnum():
#                 str += i

#         str = str.lower()
#         return str==str[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = '''!()-[]{};:'"\,<>./`?@#$%^&*_~ '''
        h = [i for i in s.lower() if i not in punc]
        return h == h[::-1]