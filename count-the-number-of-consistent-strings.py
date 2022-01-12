class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for i in words:
            if (set(i).issubset(allowed)):
                res += 1
        return res
    #
    # count = 0
    # for i in words:
    #     for j in i:
    #         if j not in allowed:
    #             count += 1
    #             break
    # return len(words) - count