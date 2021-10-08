class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        xor_result = x ^ y
        hamming_dist = 0

        for bit_shift in range(32):

            if xor_result & 1:
                hamming_dist += 1

            xor_result >>= 1

        return hamming_dist