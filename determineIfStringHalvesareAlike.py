class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = 0
        n = len(s)
        if n % 2 != 0:
            return False
        d = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        for i in range((n // 2)):
            if s[i] in d:
                a += 1

        for i in range((n // 2), n):
            if s[i] in d:
                a -= 1

        return a == 0

    