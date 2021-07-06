#   Gray Code Formula:
#   n <= 16
#   Gray_Code(n) = n XOR (n / 2)

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [i ^ (i // 2) for i in range(pow(2, n))]
        return result