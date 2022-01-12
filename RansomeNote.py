class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = set(ransomNote)
        for x in c:
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True