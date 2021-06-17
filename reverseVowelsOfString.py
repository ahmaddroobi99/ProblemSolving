class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for letter in s:
            if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels.append(letter)
                s = s.replace(letter, '_')
        vowels.reverse()
        for vowel in vowels:
            s = s.replace('_', vowel, 1)

        return s

s=Solution()
re=s.reverseVowels("Stringooppuiooek")
print(re)



#complixity O(2n)=O(n)


