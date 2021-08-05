class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if (i == 0 and digits[0] == 9):
                digits[0] = 0
                digits.insert(0, 1)
                return digits

            if (digits[i] < 9):
                digits[i] += 1
                return digits
            if (digits[i] == 9):
                digits[i] = 0

        return digits





