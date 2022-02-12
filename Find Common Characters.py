import collections
from typing import List


class Solution:
    #     def commonChars(self, words: List[str]) -> List[str]:

    #         lettersHashMap={}

    #         for word in words:
    #             innerHashMap={}
    #             for letter in word:
    #                 innerHashMap[letter]=innerHashMap.get(letter,0)+1
    #             for letter, count in innerHashMap.items():
    #                 lettersHashMap[letter]=lettersHashMap.get(letter,[])
    #                 lettersHashMap[letter].append(count)

    #         outputArray=[]
    #         for letter, counts in lettersHashMap.items():
    #             if len(counts)==len(words):
    #                 outputArray+=[letter]*min(counts)

    #         return outputArray

    # Approach

    # Initialize a dictionary dict1 with letter counts from word#1
    # Compare letters in dict1 with word#2: add letters in common to dict2 while reducing the count in dict1 to account for duplicates
    # Clear dict1
    # Compare letters in dict2 with word#3 in the same fashion
    # Clear dict2
    # Repeat for next words, alternating between filling/clearing dict1/2
    # Return result from the appropriate dictionary

    # Solution

    def commonChars(self, A: List[str]) -> List[str]:
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        k = 0

        for letter in A[0]:
            dict1[letter] += 1

        for word in A[1:]:
            if k % 2 == 0:
                for letter in word:
                    if dict1[letter]:
                        dict2[letter] += 1
                        dict1[letter] -= 1
                dict1.clear()
            else:
                for letter in word:
                    if dict2[letter]:
                        dict1[letter] += 1
                        dict2[letter] -= 1
                dict2.clear()
            k += 1

        if k % 2 == 0:
            result = [letter for l, cnt in dict1.items() for letter in l * cnt]
        else:
            result = [letter for l, cnt in dict2.items() for letter in l * cnt]

        return result