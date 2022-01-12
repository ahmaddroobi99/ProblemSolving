import collections
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = set(collections.Counter(s).values())
        if len(d) == 1:
            return True
        else:
            return False

        ###########################3

        class Solution:
            def areOccurrencesEqual(self, s: str) -> bool:
                dicc = {}
                for i in s:
                    if i in dicc:
                        dicc[i] += 1
                    else:
                        dicc[i] = 1
                for i in range(len(dicc.values()) - 1):
                    if list(dicc.values())[i] != list(dicc.values())[i + 1]:
                        return False
                return True

        from collections import Counter
        class Solution:
            def areOccurrencesEqual(self, s: str) -> bool:

                c = Counter(s)
                a = c[s[0]]
                for i in c:
                    if c[i] != a:
                        return False
                return True
