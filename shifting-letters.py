class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shift = 0
        ans = ""

        for i in range(len(s) - 1, -1, -1):
            ans += chr((ord(s[i]) - ord('a') + shift + shifts[i]) % 26 + ord('a'))
            shift += shifts[i]

        return ans[::-1]
    