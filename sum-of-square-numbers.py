class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low,high=0,int(c**0.5)+1
        while low<=high:
            tmp=low*low+high*high
            if tmp==c:return True
            if tmp>c:high-=1
            else:low+=1
        return False