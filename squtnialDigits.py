class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for num in range(1, 9):
            while num <= high and num % 10 != 0:
                if num >= low:
                    res.append(num)
                num = (num * 10) + (num % 10) + 1
        return sorted(res)

