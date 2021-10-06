class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        out, empty = 0, 0
        while numBottles > 0:
            out += 1
            numBottles -= 1
            empty += 1
            if empty == numExchange:
                empty = 0
                numBottles += 1
        return out


class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        c = nb
        while (nb >= ne):
            c += nb // ne
            nb = nb // ne + nb % ne

        return c