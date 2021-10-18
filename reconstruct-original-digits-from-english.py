# class Solution:
#     def originalDigits(self, s: str) -> str:
#         map_1 = {
#             'z': ['0', 'e', 'r', 'o'],
#             'w': ['2', 't', 'o'],
#             'u': ['4', 'f', 'o', 'r'],
#             'x': ['6', 's', 'i'],
#             'g': ['8', 'e', 'i', 'h', 't'],
#             'o': ['1', 'n', 'e'],
#             'r': ['3', 't', 'h', 'e', 'e'],
#             's': ['7', 'e', 'v', 'e', 'n'],
#             'v': ['5', 'f', 'i', 'e'],
#             'i': ['9', 'n', 'n', 'e']
#         }

#         map_3 = {}
#         ans = []
#         for c in s:
#             if not c in map_3:
#                 map_3[c] = 1
#             else:
#                 map_3[c] += 1

#         for k in map_1.keys():
#             if k in map_3 and map_3[k]>0:
#                 ans.append(map_1[k][0]*map_3[k])
#                 for i in range(1, len(map_1[k])):
#                     map_3[map_1[k][i]] -= map_3[k]
#                 map_3[k] = 0
#         ans.sort()
#         return ''.join(ans)


DIGITS = [
    [0, 'z', []],
    [2, 'w', []],
    [4, 'u', []],
    [6, 'x', []],
    [8, 'g', []],
    [5, 'f', [4]],
    [7, 's', [6]],
    [3, 'h', [8]],
    [9, 'i', [6, 8, 5]],
    [1, 'o', [0, 2, 4]]
]


class Solution:
    def originalDigits(self, S: str) -> str:
        fmap, ans, n = [0] * 26, [0] * 10, len(S)
        for i in range(10):
            dig, char, rems = DIGITS[i]
            count = S.count(char)
            for rem in rems: count -= ans[rem]
            ans[dig] += count
        return "".join([str(i) * ans[i] for i in range(10)])