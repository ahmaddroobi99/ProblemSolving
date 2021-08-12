class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero, one = s.count("0"), 0
        output = zero
        for d in s:
            if d == "0":
                zero -= 1
            if d == "1":
                one += 1
            output = min(output, zero + one)

        return output




