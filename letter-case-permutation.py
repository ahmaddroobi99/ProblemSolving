class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]

        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o + c.lower())
                    tmp.append(o + c.upper())
            else:
                for o in output:
                    tmp.append(o + c)
            output = tmp

        return output
