class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index < 0:
            return word
        return word[:index+1][::-1] + word[index+1:]