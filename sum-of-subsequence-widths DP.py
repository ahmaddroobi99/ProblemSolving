class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        S = 0
        B = [1]*len(A)
        for i in range(1,len(B)):
            B[i] = 2*B[i-1]
        for i in range(len(A)):
            S += (B[i]-B[-1-i])*A[i]
        return S%((10**9)+7)