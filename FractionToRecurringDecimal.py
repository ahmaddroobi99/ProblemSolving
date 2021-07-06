class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # the key idea of solving this problem is how to detect repeating
        # and locate where to add parentheses
        # the answer is generate the decimal part with mod operation and recalculate
        # the remainer time by time. When meeting same remainer, there have repeating
        # and the begining of the repeating is the index where you first meet
        # the same remainer
        res = ''
        # determinate symbol with xor, remeber 0 have not negative one
        if numerator ^ denominator < 0 and numerator != 0:
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        # calculate the integral part
        res += str(int(numerator / denominator))
        remainder_index = {}
        remainder = numerator % denominator
        # calculate the decimal part
        if remainder != 0:
            res += '.'
        while remainder:
            # detect same remainer, so we can locate the repeating part
            if remainder in remainder_index:
                res = res[0:remainder_index[remainder]] + \
                    '(' + res[remainder_index[remainder]:] + ')'
                # please notice that the rest calculate is repeating, so break now
                break

            remainder_index[remainder] = len(res)
            remainder *= 10
            res += str(int(remainder / denominator))
            remainder %= denominator

        return res


s = Solution()
result = s.fractionToDecimal(3, 5)

print(result)

result = s.fractionToDecimal(3, 5)

print(result)


result = s.fractionToDecimal(2, 7)

print(result)


result = s.fractionToDecimal(15, 9)

print(result)
