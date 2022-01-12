class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = "!?',;."
        paragraph = paragraph.lower()
        for i in s:
            paragraph =paragraph.replace(i, " ")
        paragraph = paragraph.split()
        occur = {}
        for word in paragraph:
            if word not in banned:
                if word in occur:
                    occur[word] += 1
                else:
                    occur[word] = 1
        maximum = 0
        result = None
        for k, v in occur.items():
            if v > maximum:
                maximum = v
                result = k
        return result