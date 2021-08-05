class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not 4 <= len(s) <= 12:
            return []

        def helper(idx, curr):
            if len(curr) == 4:
                if idx == len(s):
                    res.append('.'.join(curr))
                return

                # recursiv e relationship
            num = ''
            for i in range(idx, min(idx + 3, len(s))):
                num += s[i]
                # no leading 0
                if num[0] == '0' and len(num) > 1:
                    break
                    # betweemn 0 and 255
                if 0 <= int(num) <= 255:
                    curr.append(num)
                    helper(i + 1, curr)
                    curr.pop()

        res = []
        helper(0, [])
        return res
