class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        return z % gcd(x, y) == 0

    def gcd(x, y):
        if y == 0: return 0
        return gcd(y, x % y)