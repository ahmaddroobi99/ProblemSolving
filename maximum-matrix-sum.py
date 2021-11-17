# In a given row, if there're even number of negatives, we can turn all into positives;
# If there're odd number, we can turn all except leave one negative
# Across rows, if there're even number of negatives, they're already all turned to positives
# If there're odd number, we can move them into one column, and turn all except leave one negative
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ct = sum(sum(c < 0 for c in r) for r in matrix)
        if ct % 2 == 0:
            return sum(abs(c) for r in matrix for c in r)
        else:
            s = sorted(abs(c) for r in matrix for c in r)
            return -s[0] + sum(s[1:])