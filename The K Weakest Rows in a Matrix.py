class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a=[sum(i) for i in mat]
        b=[]
        for i in range(k):
            c=a.index(min(a))
            b.append(c)
            a[c]=float("inf")
        return b