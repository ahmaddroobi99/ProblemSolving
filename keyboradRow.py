from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiopQWERTYUIOP')
        row2 = set('asdfghjklASDFGHJKL')
        row3 = set('zxcvbnmZXCVBNM')
        result = []
        for word in words:
            w = set(list(word))
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                result.append(word)
        return result