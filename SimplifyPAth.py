# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         stack =[]
#         cur=""

#         for c in path + "/":
#             if c=="/":
#                 if cur =="..":
#                     if stack :
#                         stack.pop()
#                     elif  cur!= ""  and cur !=".":
#                         stack.append(cur)
#                     cur =""
#                 else :
#                     cur+=c

#         return "/"+ "/".join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path

        res = list()

        path_arr = path.split("/")

        for element in path_arr:
            if not element or element == ".":
                continue
            elif element == "..":
                if res:
                    res.pop()
            else:
                res.append(element)

        return "/" + "/".join(res)