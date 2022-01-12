class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res, words = [], sorted(words, key=len)
        for i, w in enumerate(words):
            if any([w in word for word in words[i + 1:]]):
                res.append(w)

        return res