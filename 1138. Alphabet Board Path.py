class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        ans = ''
        r, c = 0, 0
        for i in target:
            ch = ord(i) - ord('a')
            tr = ch // 5
            tc = ch % 5
            if c > tc:
                ans += 'L' * (c - tc)

            if tr > r:
                ans += 'D' * (tr - r)

            if r > tr:
                ans += 'U' * (r - tr)

            if tc > c:
                ans += 'R' * (tc - c)

            ans += '!'
            r = tr
            c = tc
        return ans
