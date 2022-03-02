from bisect import bisect
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = defaultdict(list)
        output = 0

        for i, c in enumerate(s):
            lookup[c].append(i)

        for w in words:
            prev = -1
            found = True
            for c in w:
                tmp = bisect.bisect(lookup[c], prev)
                if tmp == len(lookup[c]):
                    found = False
                    break
                else:
                    prev = lookup[c][tmp]
            if found:
                output += 1
        return output