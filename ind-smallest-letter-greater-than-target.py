class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
        return letters[0]