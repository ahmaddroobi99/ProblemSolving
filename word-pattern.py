class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False
        d = {}

        for x in range(len(words)):
            if pattern[x] not in d:
                if words[x] in d.values():
                    return False
                d[pattern[x]] = words[x]
            else:
                if d[pattern[x]] != words[x]:
                    return False
        return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li = s.split(' ')
        di = {}
        if len(li) != len(pattern):
            return False

        for i, val in enumerate(pattern):
            if val in di and di[val] != li[i]:
                return False
            elif val not in di and li[i] in di.values():
                return False
            elif val not in di:
                di[val] = li[i]

        return True