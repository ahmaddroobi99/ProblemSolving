class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n%2==1: ans.append(0)
        i=1
        while len(ans)<n:
            ans.append(i)
            ans.append(-i)
            i+=1
        return ans