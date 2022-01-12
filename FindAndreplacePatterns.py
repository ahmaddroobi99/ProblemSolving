class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            dic = {}
            add = True
            for i in range(len(word)):
                cur = pattern[i]
                if cur not in dic:
                    if word[i] in dic.values():
                        add = False
                    else:
                        dic[cur] = word[i]
                else:
                    if dic[cur] != word[i]:
                        add = False
            if add:
                res.append(word)
        return res