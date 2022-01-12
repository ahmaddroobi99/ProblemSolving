class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=y=0
        for i in moves:
            if i=="U":
                y+=1
            elif i=="D":
                y-=1
            elif i=="L":
                x+=1
            elif i=="R":
                x-=1
        if x==y==0:
            return True
        return False