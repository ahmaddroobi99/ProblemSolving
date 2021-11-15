from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = {w:len(w) for w in dictionary}
        mini, maxi = min(d.values()), max(d.values())
        wd = sentence.split()
        rt = []
        for s in wd:
            c = s
            for k in range(mini,min(maxi,len(s))+1):
                ss = s[:k]
                if ss in d:
                    c = ss
                    break
            rt.append(c)
        return " ".join(rt)