class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k % 2 or not k % 5: return -1
        r = length = 1
        while True:
            r = r % k
            if not r: return length
            length += 1
            r = 10*r + 1