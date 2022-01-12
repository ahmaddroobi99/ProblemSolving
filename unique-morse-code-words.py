class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        p = []
        for word in words:
            k = ''
            for char in word:
				# This below line is for finding the index of each character in the morse list
				# we know that ASCII value of a is 97 so -97 will give us the perfect index
                k += morse[ord(char)-97]
            p.append(k)
        return len(list(set(p)))