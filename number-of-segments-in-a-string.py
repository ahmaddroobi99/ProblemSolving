class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        if s == "":
            return 0

        lst = list(s.split(" "))
        print(lst)
        for ch in lst:
            if ch != '':
                count += 1
        return count