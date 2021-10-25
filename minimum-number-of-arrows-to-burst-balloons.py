class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points =sorted(points,key=lambda x :x[1])
        count =0
        ending = float('-inf')
        for baloon in points :
            if baloon [0]> ending :
                count +=1
                ending =baloon [1]
        return count 