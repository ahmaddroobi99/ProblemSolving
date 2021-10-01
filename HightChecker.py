class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        sorte=[]
        # extend appends heights to sorte
        sorte.extend(heights)
        sorte.sort()
        for i,v in enumerate(sorte):
            if sorte[i]!=heights[i]:
                count+=1
        return count