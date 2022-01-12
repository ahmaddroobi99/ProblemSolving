class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = []
        for ppl, start, end in trips:
            l.append((start, ppl))
            l.append((end, -ppl))

        l.sort()

        for _, ppl in l:
            capacity -= ppl
            if capacity < 0:
                return False
        return True


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = [0 for i in range(1001)]

        for t in trips:
            t_nump = t[0]
            t_from = t[1]
            t_to = t[2]

        for i in range(t_from, t_to):
            passengers[i] += t_nump

            if passengers[i] > capacity:
                return False

        return True