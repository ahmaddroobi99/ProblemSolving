class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        v, c = [], 0
        for i in range(left,right+1):
            f = i
            while f > 0:
                x = f % 10
                if x != 0 and i % x == 0:
                    c = 1
                    f = f // 10
                else:
                    c = 0
                    break
            if c == 1:
                v.append(i)
        return v