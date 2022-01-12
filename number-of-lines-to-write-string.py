class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        su, c = 0, 1
        for i in s:
            x = widths[ord(i)-97]
            su += x
            if su > 100:
                su = x
                c += 1
        return [c,su]