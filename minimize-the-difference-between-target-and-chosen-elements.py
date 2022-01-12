class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        possibleSum = set([0])
        for m in mat:
            temp = set()
            for y in possibleSum:
                for x in sorted(set(m)):
                    temp.add(x+y)
                    if x+y>target:
                        break
            possibleSum = temp
        return min(abs(s-target) for s in possibleSum)