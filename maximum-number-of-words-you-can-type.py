class Solution:

    def canBeTypedWords(self, text: str, B: str) -> int:
        cnt = 0
        s = text.split(" ")
        for i in s:
            for j in B:
                if j in i:
                    cnt += 1
                    break

        return len(s) - cnt